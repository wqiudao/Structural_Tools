#!/home/miniconda3/miniconda3/envs/CRISPR_Cas_Finder/bin/python 
#  chmod -R +x bin_dali
#
# pdb2dalidb.py was designed to make `dali.pl` easier to use, by wqiudao widthin 2024.
# bin_dali
# The `bin_dali` folder contains all the executable files of the Dali suite, and the execution of `pdb2dalidb.py` depends on the `bin_dali` folder.


# pdb2dalidb.py
# `pdb2dalidb.py` takes a PDB file and the path to a reference database in Dali format. It calls `dali.pl` and restores the names of the reference PDBs from the reference database.

# `dali.hash`: Maps old names to new  filenames
# `dali.list`: Lists the new filenames for import.pl and dali.pl

import os,random,sys,shutil,subprocess,re

from collections import defaultdict

id2pdb=defaultdict(str) # hash filename




# def pdb2dalidb(pdb,ref_dali_db,getcwd_pdb):  #single pdb file to dali


	# dali_ref_list=${ref_dali_db}/dali.list
	# dali2symbol=${ref_dali_db}/dali.hash

	# dest_directory=pdb+'_dali_rs'
	# if os.path.exists(dest_directory):
		# shutil.rmtree(dest_directory)
	# os.makedirs(dest_directory)		

	# os.chdir(dest_directory)

	
	# perl_script = os.path.dirname(os.path.abspath(__file__))+'/bin_dali/dali.pl'


	# result = subprocess.Popen(
		# ['perl', perl_script, '--pdbfile1', filename, '--pdbid', new_names_dali2symbol[filename], '--dat', dest_directory, '--clean'],stdout=subprocess.PIPE,stderr=subprocess.PIPE
	# )





 # time dali.pl --pdbfile1 $filename  --db ${dali_ref_list} --dat1 .   --dat2  ${dali_DATA} --title ${pdb_symbol} --outfmt "summary,alignments,equivalences,transrot"  --clean > ${pdb_symbol}.log  2>&1




def recover_name(pdb2id, query):
	
	pdb2id_file=open(pdb2id)
	reads=pdb2id_file.readline()
	while reads:
		readss=re.split(r',',reads)
		if len(readss)>1:
			pdb_symbol=re.search(r'(\S+).pdb',readss[0])
			pdb_id=re.search(r'(\d+).pdb',readss[1])
			if pdb_symbol and pdb_id:
				# print(pdb_symbol.group(1))
				# print(pdb_id.group(1)) ___
				id2pdb[pdb_id.group(1)+'A']=pdb_symbol.group(1).split('___')[0]
				id2pdb[pdb_id.group(1)+'-A']=pdb_symbol.group(1).split('___')[0]
		
		# print(readss)
		
		
		reads=pdb2id_file.readline()
	pdb2id_file.close()
	query_symbol=open(query+".symbol.txt",'w')
	# print(id2pdb)
	
	query_file=open(query)


	reads=query_file.readline()
	while reads:
		for old_name in id2pdb:
			new_name=id2pdb[old_name]
			reads = re.sub(r'\b' + re.escape(old_name) + r'\b', new_name, reads)
		query_symbol.write(reads)
		reads=query_file.readline()
	query_file.close()
	query_symbol.close()
	
	
	
	




def pdb2dalidb(pdb,ref_dali_db,getcwd_pdb):

	filename=f'{getcwd_pdb}/{pdb}'
	
	print(filename)
	dali_ref_list=f'{ref_dali_db}/dali.list'
	dali2symbol=f'{ref_dali_db}/dali.hash'


	dest_directory=pdb.split(".")[0]+'_dali_rs'
	
	
	if os.path.exists(dest_directory):
		shutil.rmtree(dest_directory)
	os.makedirs(dest_directory)		
	shutil.copy(filename, dest_directory)
	
	

	

	print(dali_ref_list)
	print(dali2symbol)
	print(f"{os.getcwd()}")


	perl_script = os.path.dirname(os.path.abspath(__file__))+'/bin_dali/dali.pl'

	os.chdir(dest_directory)
	result = subprocess.Popen(
		['perl', perl_script, '--pdbfile1', pdb, '--db', dali_ref_list, '--dat1','.', '--dat2', ref_dali_db, '--title', pdb, '--outfmt','summary,alignments,equivalences,transrot', '--clean'],stdout=subprocess.PIPE,stderr=subprocess.PIPE
	)




 # time dali.pl --pdbfile1 $filename  --db ${dali_ref_list} --dat1 .   --dat2  ${dali_DATA} --title ${pdb_symbol} --outfmt "summary,alignments,equivalences,transrot"  --clean > ${pdb_symbol}.log  2>&1


		

	# # # Êä³ö Perl ½Å±¾µÄ½á¹û
	# # print(stdout)
	# # print(stderr)  # Èç¹ûÓÐ´íÎó£¬¿ÉÒÔ´òÓ¡´íÎóÐÅÏ¢

	stdout, stderr = result.communicate()

	# # Êä³ö½á¹û
	print(stdout.decode('utf-8'))
	print(stderr.decode('utf-8'))  # Èç¹ûÓÐ´íÎó£¬¿ÉÒÔ´òÓ¡´íÎóÐÅÏ¢


	recover_name(dali2symbol, "mol1A.txt")

	# new_names_dali=set()
	# new_names_dali2symbol={}
	
	# dest_directory=src_directory+'_dali'
	# # log_file=src_directory+'_dali.log'
	# log_file=f'{dest_directory}/{src_directory}_dali.hash'
	# list_file=f'{dest_directory}/{src_directory}_dali.list'

	# if os.path.exists(dest_directory):
		# shutil.rmtree(dest_directory)
	# os.makedirs(dest_directory)	
	# pdb_files_with_random = {}

	# for root, dirs, files in os.walk(src_directory):
		# for file in files:
			# if file.endswith('.pdb'):
		 
				# random_number += 1
				# new_filename = f"{random_number}.pdb"
				
				 
				# src_file_path = os.path.join(root, file)
				# dest_file_path = os.path.join(dest_directory, new_filename)
				
				# shutil.copy(src_file_path, dest_file_path)
				# new_names_dali.add(dest_file_path)
				# new_names_dali2symbol[dest_file_path]=str(random_number)
				# pdb_files_with_random[file] = new_filename

	 
	# log_file=open(log_file, 'w')
	# list_file=open(list_file, 'w')
	# for old_name, new_name in pdb_files_with_random.items():
		# log_file.write(f"Old Name: {old_name}, New Name: {new_name}\n")
		# list_file.write(f"{new_name.split('.')[0]}A\n")

		
	# log_file.close()
	# list_file.close()
	# # print(new_names_dali)
	# # print(new_names_dali2symbol)

		
	# perl_script = os.path.dirname(os.path.abspath(__file__))+'/bin_dali/import.pl'


	# for filename in new_names_dali:

		# print(filename)
		# print(new_names_dali2symbol[filename])
		
		# # µ÷ÓÃ Perl ½Å±¾£¬²¢´«µÝÃüÁîÐÐ²ÎÊý  dest_directory
		# result = subprocess.Popen(
			# ['perl', perl_script, '--pdbfile', filename, '--pdbid', new_names_dali2symbol[filename], '--dat', dest_directory, '--clean'],stdout=subprocess.PIPE,stderr=subprocess.PIPE
		# )

		# # # Êä³ö Perl ½Å±¾µÄ½á¹û
		# # print(stdout)
		# # print(stderr)  # Èç¹ûÓÐ´íÎó£¬¿ÉÒÔ´òÓ¡´íÎóÐÅÏ¢

		# stdout, stderr = result.communicate()

		# # Êä³ö½á¹û
		# print(stdout.decode('utf-8'))
		# print(stderr.decode('utf-8'))  # Èç¹ûÓÐ´íÎó£¬¿ÉÒÔ´òÓ¡´íÎóÐÅÏ¢
 
	# ref_dalie_data=f"{os.getcwd()}/{dest_directory}"
	# print(f"ref_dalie_data={ref_dalie_data}")
	
	# log_file=open(dest_directory+".dali_ref.log", 'w')
	# log_file.write(f"ref_dalie_data={ref_dalie_data}\n")	
	# log_file.close()
 
	
# import.pl --pdbfile HEPN_REF_PDB_Cas13_abdhx_dali/1002.pdb  --pdbid 1002  --dat HEPN_REF_PDB_Cas13_abdhx_dali --clean 



if __name__ == "__main__":
	if len(sys.argv) != 3:
		print(f"Usage: python {sys.argv[0]} pdb ref_dali_db")
		sys.exit(1)


 
	pdb = sys.argv[1]
	ref_dali_db = sys.argv[2]
	
	pdb2dalidb(pdb,ref_dali_db,f"{os.getcwd()}")
	 














































# #DaliLite ¨¨¨ª?t?T?¡§???t??¡À?D???¨®D????¡Á?¡¤?¡ê??¨´¨®D¡ê??a??3¨¬D¨°¡ê?¡ã??¨´¨®D???t?¡ä??¨°?¡¤Y2¡é????????¡Á?¡¤?¡ê?¨ª?¨º¡À¡ê?¨¦¨²3¨¦??¨®|¦Ì????t¡ê?1?o¨®D?¨º1¨®?

# import sys,re

# # import os
# # import random
# # import shutil

# from collections import defaultdict

# id2pdb=defaultdict(str) #¡ä?¡ä¡é???¨²¨ºy¦Ì??-¨º???3?¦Ì?¨¢D¡À¨ª



# # Old Name: Cas13f10___Cas13f10.ranked_0.pdb, New Name: 1001.pdb
# # Old Name: Cas13a_652829192_Lachnosp___ium_NK4Aaa.ranked_0.pdb, New Name: 1002.pdb


# def recover_name(pdb2id, query):
	
	# pdb2id_file=open(pdb2id)
	# reads=pdb2id_file.readline()
	# while reads:
		# readss=re.split(r',',reads)
		# if len(readss)>1:
			# pdb_symbol=re.search(r'(\S+).pdb',readss[0])
			# pdb_id=re.search(r'(\d+).pdb',readss[1])
			# if pdb_symbol and pdb_id:
				# # print(pdb_symbol.group(1))
				# # print(pdb_id.group(1)) ___
				# id2pdb[pdb_id.group(1)+'A']=pdb_symbol.group(1).split('___')[0]
				# id2pdb[pdb_id.group(1)+'-A']=pdb_symbol.group(1).split('___')[0]
		
		# # print(readss)
		
		
		# reads=pdb2id_file.readline()
	# pdb2id_file.close()
	# query_symbol=open(query+".symbol.log",'w')
	# # print(id2pdb)
	
	# query_file=open(query)


	# reads=query_file.readline()
	# while reads:
		# for old_name in id2pdb:
			# new_name=id2pdb[old_name]
			# reads = re.sub(r'\b' + re.escape(old_name) + r'\b', new_name, reads)
		# query_symbol.write(reads)
		# reads=query_file.readline()
	# query_file.close()
	# query_symbol.close()
	
	
	
	
	
	
	
	# # print(newick_string)
	# # # ¨º1¨®??y?¨°¡À¨ª¡ä?¨º?¨¬????¨²¦Ì???
	# # for old_name in id2pdb:
		# # new_name=id2pdb[old_name]
		# # # print(old_name)
		# # # print(new_name)
		# # newick_string = re.sub(r'\b' + re.escape(old_name) + r'\b', new_name, newick_string)

	# # newick_file=open(query+".tree",'w')
	# # newick_file.write(newick_string)
	# # newick_file.close()
# def copy_pdb_files_with_random_names(src_directory, dest_directory, log_file_path,random_number=1000):
    # # ¨¨¡¤¡À¡ê??¡À¨º????¡ä??¨²

	# if os.path.exists(dest_directory):
		# shutil.rmtree(dest_directory)
	# os.makedirs(dest_directory)	
	# pdb_files_with_random = {}

	# for root, dirs, files in os.walk(src_directory):
		# for file in files:
			# if file.endswith('.pdb'):
				# # ¨¦¨²3¨¦????¨ºy¦Ì????¨²¨ºy¡Á¡Â?aD????t??
				# random_number += 1
				# new_filename = f"{random_number}.pdb"
				
				# # 11?¨¬?¡ä???to¨ª??¡À¨º???t¦Ì?¨ª¨º???¡¤??
				# src_file_path = os.path.join(root, file)
				# dest_file_path = os.path.join(dest_directory, new_filename)
				
				# # ?¡ä?????t¦Ì???¡À¨º????¡ê?2¡é¨°????¨²¨ºy?¨¹??
				# shutil.copy(src_file_path, dest_file_path)
				
				# # ¡À¡ê¡ä??¨¦???t??o¨ªD????t??¦Ì???¨®|1??¦Ì
				# pdb_files_with_random[file] = new_filename

	# # ??D??¨¦???t??¦Ì???¨®|1??¦ÌD¡ä¨¨?¦Ì?log???t?D
	# log_file=open(log_file_path, 'w')
	# list_file=open(log_file_path+'.list', 'w')
	# for old_name, new_name in pdb_files_with_random.items():
		# log_file.write(f"Old Name: {old_name}, New Name: {new_name}\n")
		# list_file.write(f"{new_name.split('.')[0]}A\n")
	# log_file.close()
	# list_file.close()
 		

# if __name__ == "__main__":
	# if len(sys.argv) != 3:
		# print("Usage: python script.py <pdb2id> <1001A.txt>")
		# sys.exit(1)

	# # ¡ä¨®?¨¹¨¢?DD??¨¨??¡ä?????¡é??¡À¨º????o¨ª¨¨??????t?¡¤??

	# recover_name(sys.argv[1], sys.argv[2])

	# # print(f"Files copied and renamed. Log saved to {log_file_path}")











# # import os

# # def get_pdb_files(directory):
    # # pdb_files = []
    # # # ¡À¨¦¨¤¨²????
    # # for root, dirs, files in os.walk(directory):
        # # for file in files:
            # # # ?¨¬2¨¦???t¨¤??1??¨º?¡¤??a .pdb
            # # if file.endswith('.pdb'):
                # # # ?????t??¡ê¡§¡ã¨¹¨¤¡§?¡¤??¡ê?¨¬¨ª?¨®¦Ì?¨¢D¡À¨ª?D
                # # pdb_files.append(os.path.join(root, file))
    # # return pdb_files

# # # ¨º?¨¤y¡êo?¨´¨¦¨¨??¨°a¡À¨¦¨¤¨²¦Ì?????¨º? "example_directory"
# # directory_path = "alphfold_PDB_ranked_0"
# # pdb_files = get_pdb_files(directory_path)

# # # ¨º?3??¨¢1?
# # for pdb_file in pdb_files:
    # # print(pdb_file)




