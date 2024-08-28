#!/home/miniconda3/miniconda3/envs/CRISPR_Cas_Finder/bin/python 
#  chmod -R +x bin_dali
#
# makedalidb.py was designed to make `import.pl` easier to use, by wqiudao widthin 2024.
# bin_dali
# The `bin_dali` folder contains all the executable files of the Dali suite, and the execution of `makedalidb.py` depends on the `bin_dali` folder.


# makedalidb.py 
# The `makedalidb.py` script takes a folder containing PDB files and renames them according to the DaliLite four character alphanumeric code. It also generates a hash table that records the correspondence between the old and new filenames.

# `dali.hash`: Maps old names to new  filenames
# `dali.list`: Lists the new filenames for import.pl and dali.pl



import os,random,sys,shutil,subprocess

def makedalidb(src_directory,random_number=1000):
	new_names_dali=set()
	new_names_dali2symbol={}
	
	dest_directory=src_directory+'_dali'
	# log_file=src_directory+'_dali.log'
	log_file=f'{dest_directory}/dali.hash'
	list_file=f'{dest_directory}/dali.list'

	if os.path.exists(dest_directory):
		shutil.rmtree(dest_directory)
	os.makedirs(dest_directory)	
	pdb_files_with_random = {}

	for root, dirs, files in os.walk(src_directory):
		for file in files:
			if file.endswith('.pdb'):
		 
				random_number += 1
				new_filename = f"{random_number}.pdb"
				
				 
				src_file_path = os.path.join(root, file)
				dest_file_path = os.path.join(dest_directory, new_filename)
				
				shutil.copy(src_file_path, dest_file_path)
				new_names_dali.add(dest_file_path)
				new_names_dali2symbol[dest_file_path]=str(random_number)
				pdb_files_with_random[file] = new_filename

	 
	log_file=open(log_file, 'w')
	list_file=open(list_file, 'w')
	for old_name, new_name in pdb_files_with_random.items():
		log_file.write(f"Old Name: {old_name}, New Name: {new_name}\n")
		list_file.write(f"{new_name.split('.')[0]}A\n")

		
	log_file.close()
	list_file.close()
	# print(new_names_dali)
	# print(new_names_dali2symbol)

		
	perl_script = os.path.dirname(os.path.abspath(__file__))+'/bin_dali/import.pl'


	for filename in new_names_dali:

		print(filename)
		print(new_names_dali2symbol[filename])
		
		# µ÷ÓÃ Perl ½Å±¾£¬²¢´«µÝÃüÁîÐÐ²ÎÊý  dest_directory
		result = subprocess.Popen(
			['perl', perl_script, '--pdbfile', filename, '--pdbid', new_names_dali2symbol[filename], '--dat', dest_directory, '--clean'],stdout=subprocess.PIPE,stderr=subprocess.PIPE
		)

		# # Êä³ö Perl ½Å±¾µÄ½á¹û
		# print(stdout)
		# print(stderr)  # Èç¹ûÓÐ´íÎó£¬¿ÉÒÔ´òÓ¡´íÎóÐÅÏ¢

		stdout, stderr = result.communicate()

		# Êä³ö½á¹û
		print(stdout.decode('utf-8'))
		print(stderr.decode('utf-8'))  # Èç¹ûÓÐ´íÎó£¬¿ÉÒÔ´òÓ¡´íÎóÐÅÏ¢
 
	ref_dali_db=f"{os.getcwd()}/{dest_directory}"
	print(f"ref_dali_db={ref_dali_db}")
	
	log_file=open(dest_directory+".dali_ref.log", 'w')
	log_file.write(f"ref_dali_db={ref_dali_db}\n")	
	log_file.close()
 
	
# import.pl --pdbfile HEPN_REF_PDB_Cas13_abdhx_dali/1002.pdb  --pdbid 1002  --dat HEPN_REF_PDB_Cas13_abdhx_dali --clean 



if __name__ == "__main__":
	if len(sys.argv) != 2:
		print(f"Usage: python {sys.argv[0]} folder_with_pdb_files")
		sys.exit(1)
		
	src_directory = sys.argv[1]
	
	makedalidb(src_directory)
	
	# print(os.path.dirname(os.path.abspath(__file__)))
	
	print(f"Files copied and renamed. Log saved to {src_directory}_dali")
























