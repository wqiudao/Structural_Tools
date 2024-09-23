import json
from pymol import cmd

"""
Set colors for atoms in the loaded PDB file based on the atom_plddts values from the JSON file.
Parameters:
- `json_file`: Path to the JSON file containing the atom_plddts values

color_atoms_by_plddt json_file

"""


def color_atoms_by_plddt(json_file):

	with open(json_file, 'r') as f:
		data = json.load(f)
	plddts = data["atom_plddts"]
	atoms = cmd.get_model("all").atom
	if len(atoms) != len(plddts):
		print("Warning: The number of atoms does not match the number of plddts data!")
		return
	for i, atom in enumerate(atoms):
		plddt = plddts[i]
		if plddt >= 90:
			color_name = "neptunium"
		elif 70 <= plddt < 90:
			color_name = "cyan"
		elif 50 <= plddt < 70:
			color_name = "gold"
		else:
			color_name = "phosphorus"
		atom_selection = f"id {atom.index}"
		cmd.color(color_name, atom_selection)
cmd.extend("color_atoms_by_plddt", color_atoms_by_plddt)










