# 1，使用pymol软件，打开pdb文件
# 2，在软件的右下角，将 selecting 模式改为 C-alphas，保持不动
# 3，选中目标残基，运行下面的代码（注意每个残基命名要不相同）
# pink
set cartoon_fancy_helices, 0
set cartoon_fancy_helices, 1


# set cartoon_cylindrical_helices, 1
# set cartoon_fancy_helices, 0
# set cartoon_cylindrical_helices, 0
# set cartoon_oval_length , 0.5 # default is 1.20
# set cartoon_oval_width , 0.2  # default is 0.25

File->Exort Image As PNG ->ray trace with transparent background
Action->orient





pink

orange
limon







from pymol import cmd
from pymol.cgo import *


sele_index=0


residue_xyzs= cmd.get_coords('sele',1)
print(residue_xyzs)
sele_index=sele_index+1  # rename
cmd.load_cgo([COLOR, 1,0,0, SPHERE,residue_xyzs[0][0],residue_xyzs[0][1],residue_xyzs[0][2],1.5,], 'residue'+str(sele_index))    


residue_xyzs= cmd.get_coords('sele',1)
print(residue_xyzs)
sele_index=sele_index+1  # rename
cmd.load_cgo([COLOR, 1,0.5,0, SPHERE,residue_xyzs[0][0],residue_xyzs[0][1],residue_xyzs[0][2],1,], 'residue'+str(sele_index))    





residue_xyzs= cmd.get_coords('sele',1)
print(residue_xyzs)
sele_index=sele_index+1  # rename
cmd.load_cgo([COLOR, 0,0,1, SPHERE,residue_xyzs[0][0],residue_xyzs[0][1],residue_xyzs[0][2],1,], 'residue'+str(sele_index))    




residue_xyzs= cmd.get_coords('sele',1)
print(residue_xyzs)
sele_index=sele_index+1  # rename
cmd.load_cgo([COLOR, 0,0.5,1, SPHERE,residue_xyzs[0][0],residue_xyzs[0][1],residue_xyzs[0][2],1,], 'residue'+str(sele_index))    


set cartoon_fancy_helices, 1
set cartoon_cylindrical_helices, 1

set cartoon_fancy_helices, 0
set cartoon_cylindrical_helices, 0


set cartoon_oval_length , 0.5 # default is 1.20


set cartoon_oval_width , 0.2  # default is 0.25



File->Exort Image As PNG ->ray trace with transparent background



# print(residue_xyzs)

# sele_index=1
# sphere_residue = [COLOR, 1,0,0, SPHERE,residue_xyzs[0][0],residue_xyzs[0][1],residue_xyzs[0][2],1,]
# cmd.load_cgo(sphere_residue, 'residue'+str(sele_index))    


# sphere_residue = [COLOR, 1,0,0, SPHERE,residue_xyzs[0][0],residue_xyzs[0][1],residue_xyzs[0][2],1,]


# residue_xyzs= cmd.get_coords('sele',1)

# print(residue_xyzs[0][0])

# sele_index=1
# sphere_residue = [COLOR, 1,0,0, SPHERE,residue_xyzs[0][0],residue_xyzs[0][1],residue_xyzs[0][2],1,]
# cmd.load_cgo(sphere_residue, 'residue'+str(sele_index))    

# xyz_x = { v[0] for v in residue_xyzs}
# xyz_y = { v[1] for v in residue_xyzs}
# xyz_z = { v[2] for v in residue_xyzs}

# sele_index=3
# sphere_residue = [COLOR, 1,0,0, SPHERE,xyz_x,xyz_y,xyz_z,1,]
# cmd.load_cgo(sphere_residue, 'residue'+str(sele_index))    

# sele_index=3
# sphere_residue3 = [COLOR, 1,0,0, SPHERE,9.923,-0.7,-23.215,2,]
# cmd.load_cgo(sphere_residue3, 'residue'+str(sele_index))    


# sele_index=3
# sphere_residue = [COLOR, 1,0,0, SPHERE,max(xyz_x),max(xyz_y),max(xyz_z),1,]
# cmd.load_cgo(sphere_residue, 'residue'+str(sele_index))    




# sphere_residue2 = [COLOR, 1,0,0, SPHERE,max(xyz_x),max(xyz_y),max(xyz_z),1,]
# cmd.load_cgo(sphere_residue2, 'residue'+str(sele_index+1))    















# print(','.join(str(v) for v in cmd.get_coords('sele',1)[atom_index]))


# residue_xyzs= cmd.get_coords('sele',sele_index)

# print(residue_xyzs)

# xyz_x = { v[0] for v in residue_xyzs}
# xyz_y = { v[1] for v in residue_xyzs}
# xyz_z = { v[2] for v in residue_xyzs}



# sphere_residue2 = [COLOR, 0,0,1, SPHERE,min(xyz_x),min(xyz_y),min(xyz_z),2,]
# cmd.load_cgo(sphere_residue2, 'residue'+str(sele_index))    

