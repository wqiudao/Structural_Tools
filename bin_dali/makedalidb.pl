#!/usr/bin/perl
#
# This program was modified based on "import.pl" by wqiudao widthin 2024.

# makedalidb.pl 
# The `makedalidb.pl` script takes a folder containing PDB files and renames them according to the DaliLite four character alphanumeric code. It also generates a hash table that records the correspondence between the old and new filenames.

# `dali.hash`: Maps old names to new  filenames
# `dali.list`: Lists the new filenames for import.pl and dali.pl


use FindBin qw($Bin);
use lib "$FindBin::Bin"; # modules and scripts in same directory
use strict;
use mpidali;
use warnings;
use 5.010;
use Getopt::Long qw(GetOptions);

my $DALIDATDIR="./DAT";
my $PDBDIR="/data/pdb";
my $rsync;
my $help;
my $infile;
my $listfile;
my $short;
my $verbose;
my $clean;
my $tmpfile="$$\.tmp";
my @tmpfiles=('puu.default', 'units.puu', 'subunits.puu', 'domains.puu');

my $USAGE= <<"EOB";
Convert PDB entrys into Dali format.

$0 --pdbfolder <path>

* Options:
	--pdbfolder <path>	The folder containing the PDB files



EOB

GetOptions('pdbfolder=s' => \$pdbfolder) or die $USAGE;










# GetOptions(
	# 'h|help' => \$help,
	# 'dat=s' => \$DALIDATDIR,
	# 'pdbfile=s' => \$infile,
	# 'pdblist=s' => \$listfile,
	# 'pdbid=s' => \$short,
	# 'rsync' => \$rsync,
	# 'verbose' => \$verbose,
	# 'clean' => \$clean,
	# 'pdbmirrordir=s' => \$PDBDIR) or die $USAGE;

if($help) { die $USAGE; }
if(! ($infile || $listfile || $rsync) ) { die $USAGE; }
# main
if(!$DALIDATDIR) { $DALIDATDIR="./"; }
&checkdir($DALIDATDIR);
my @list;
if($rsync) { 
	if(!$PDBDIR) { $PDBDIR="./"; }
	&checkdir($PDBDIR);
	(@list)=&mirror($PDBDIR,$DALIDATDIR); 
} elsif($listfile) {
	&lock();
	open(LIST,"<$listfile") || die "Can't open file: $listfile\n";
	while(<LIST>) {
		my($infile)=/^(\S+)/;
		my($short)=/pdb(\w{4})\.ent/;
		&import_one($infile,$short,$DALIDATDIR,$tmpfile,$verbose);
	}
	close(LIST);
	&unlock();
} else { 
	&lock(); # lock directory (units.puu, subunits.puu, domains.puu)
	&import_one($infile,$short,$DALIDATDIR,$tmpfile,$verbose); 
	push(@list,$short);
	&unlock();
}

# clean up
system("rm -f $tmpfile");
if($clean) {
	system("rm -f @tmpfiles");
	# remove dssp files
	foreach my $cd (@list) { 
		my $fn="$cd\.dssp";
		system("rm -f $fn");
	}
}

exit();

sub checkdir {
	my($dir)=@_;
	if(-d $dir) { return } else { warn "# Directory $dir does not exist - creating it!\n"; system('mkdir $dir'); }
}

sub mirror {
	my($PDBDIR,$DALIDATDIR)=@_;
	# call rsync
	my $mirrorlog="pdb_update.log";
	my @list;
	my $cmd="rsync -rlpt -v -z --delete --port=33444 rsync.rcsb.org::ftp_data/structures/divided/pdb/ $PDBDIR > $mirrorlog";
	if($verbose) { warn "# Starting rsync\n$cmd\n"; }
	system($cmd);
	(@list)=`grep ent.gz $mirrorlog`;
	if($verbose) { warn "# rsync done, $#list new entries in $mirrorlog\n"; }
	# import new
	&lock(); # lock directory (units.puu, subunits.puu, domains.puu)
	foreach (@list) {
		chomp;
		my $pdbfile="$PDBDIR\/$_";
		my($short)=/pdb(\w{4})\.ent/;
		if($verbose) { warn "# importing $short from $_\n"; }
		&import_one($pdbfile,$short,$DALIDATDIR,$tmpfile,$verbose);
	}
	&unlock();
	return(@list);
}

