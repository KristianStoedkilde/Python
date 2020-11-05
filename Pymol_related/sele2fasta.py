from pymol import cmd

d = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
     'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
     'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', 
     'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}

def three2one(x):
    if len(x) % 3 != 0: 
    	raise ValueError('Input length should be a multiple of three')

    y = ''
    for i in range(int(len(x)/3)):
            y += d[x[3*i:3*i+3]]
    return y

def sele2fasta():
	if cmd.count_atoms("sele") == 0:
		print("Nothing selected")
		return

	stored.list=[]
	cmd.iterate("sele" + " and (name ca)","stored.list.append((resi,resn))")
	sequence = ""
	for i in range(len(stored.list)):
		if (str(stored.list[i][1]) == "CYSS"):
			sequence = sequence+ "CYS"
		else:
			sequence = sequence+ str(stored.list[i][1])
	print (three2one(sequence))	
cmd.extend("sele2fasta", sele2fasta)