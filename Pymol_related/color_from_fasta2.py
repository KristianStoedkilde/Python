from pymol import cmd

similar_aa = [['D','E'],['F','W','Y'],['H','K','R'],['I','L','M','V'],['N','Q'],['S','T'],['G','A']]
all_aa = ['D','E','F','W','Y','H','K','R','I','L','M','V','N','Q','S','T','G','A''-'] 

#Colors
conserved = "green"
partially_conserved = "lightorange"
similar = "yellow"
dissimilar = "grey90"

' USAGE: Needs fasta file. Objects to be colored must have EXACT same name as in the fasta file. '
' Starting residues of each object must be parsed as list. The list must be arranged as in the fasta file '
' Example: color_from_fasta2("alignment.fasta", start_residues = (36, 3)) '
' Kristian Stoedkilde-Joergensen. October 2013 '

def all_conserved(sequence_list, i):
    if all(sequence_list[x][1][i] is sequence_list[0][1][i] for x in range(1,len(sequence_list))):
        return True
    else:
        return False

def partial_conserved(sequence_list, i):
    for u in range(1,len(sequence_list)):
        if (sequence_list[u][1][i] == sequence_list[0][1][i]):
            return True
    return False

def color_from_fasta2(fasta_file, start_residues = None):

    sequence_list = []

#Load in fasta file
    with open(fasta_file) as f:
        content = f.readlines()

#put in nested list, > indicates sequence name, else sequence. If blank line, continue.
    for line in content:
        if line.startswith('>'):
            sequence_list.append([line[1:].strip(),''])
        elif line.startswith('\n'):
            continue
        else:
            sequence_list[-1][1] += line.strip()
            if not line:
                break

#Sanity check to see if number of sequences in fasta matches number of start residues parsed to the function
    if len(sequence_list) != len(start_residues):
        print "\n\nERROR: Number of fasta sequences (%i) does not match start residues (%i).\n\n" % (len(sequence_list), len(start_residues))
        return

#loop over length of main sequence
    for i in range (0,len(sequence_list[0][1])):
        
#Does main sequence have a gap?
        if sequence_list[0][1][i] == "-":
            for u in range(1,len(sequence_list)):
                cmd.color(dissimilar,"%s and resi %s" % (sequence_list[u][0],start_residues[u]+i-sequence_list[u][1][0:i].count("-")))

#aa is not in list?
        elif sequence_list[0][1][i] not in all_aa:
            for u in range(0,len(sequence_list)):
                cmd.color(dissimilar,"%s and resi %s" % (sequence_list[u][0],start_residues[u]+i-sequence_list[u][1][0:i].count("-")))

#Full conservation?  
        elif all_conserved(sequence_list,i):
            for u in range(0,len(sequence_list)):
                cmd.color(conserved,"%s and resi %s" % (sequence_list[u][0],start_residues[u]+i-sequence_list[u][1][0:i].count("-")))

#Partial conservation?     
        elif partial_conserved(sequence_list,i):
            cmd.color(partially_conserved,"%s and resi %s" % (sequence_list[0][0],start_residues[0]+i-sequence_list[0][1][0:i].count("-")))
            for u in range(1,len(sequence_list)):
                if (sequence_list[u][1][i] == sequence_list[0][1][i]):
                    cmd.color(partially_conserved,"%s and resi %s" % (sequence_list[u][0],start_residues[u]+i-sequence_list[u][1][0:i].count("-")))
        else:
            cmd.color(dissimilar,"%s and resi %s" % (sequence_list[0][0],start_residues[0]+i-sequence_list[0][1][0:i].count("-")))
            for u in range(1,len(sequence_list)):
                cmd.color(dissimilar,"%s and resi %s" % (sequence_list[u][0],start_residues[u]+i-sequence_list[u][1][0:i].count("-")))
#Similar residues?
                for y in range (0, len(similar_aa)):
                    if (sequence_list[u][1][i] in similar_aa[y] and sequence_list[0][1][i] in similar_aa[y]):
                        cmd.color(similar,"%s and resi %s" % (sequence_list[u][0],start_residues[u]+i-sequence_list[u][1][0:i].count("-")))
                        cmd.color(similar,"%s and resi %s" % (sequence_list[0][0],start_residues[0]+i-sequence_list[0][1][0:i].count("-")))
                   
cmd.extend("color_from_fasta2", color_from_fasta2)
