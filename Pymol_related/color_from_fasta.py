from pymol import cmd

g1 = {'D','E'}
g2 = {'F','W','Y'}
g3 = {'H','K','R'}
g4 = {'I','L','M','V'}
g5 = {'N','Q'}
g6 = {'S','T'}
all_aa = {'D','E','F','W','Y','H','K','R','I','L','M','V','N','Q','S','T','-'} 

s1 = "---AEGLKTKDEVEKACHLAQQLKEVSITLGVIYRTTERHSVQVEAHKTAIDKHADAVSRAVEALTRVDVALQRLKELGKANDTKAVKIIENITSARENLALFNNETQAVLTARDHVHKHRAAALQGWSDAKEKGDAAAEDVWVLLNAAKKGNGSADVKAAAEKCSRYSSSSTSETELQKAIDAAANVGGLSAHKSKYGDVLNKFKLSNASVGAVRDTSGRGGKHMEKVNNVAKLLKDAEVSLAAAAAEIEEVKNAHETKAQEE"

s2 = "GEIKVELEDSDDVAAACELRAQLAGVSIASGILLRPAVIRNATTEFSRKKSEDILAKGGAAVERASA---AVDRVSGL-DKTNETAQKVRKAAAVAHHALEHVKEEVEIVAKKVNEIIELTAGATEHAKGAKANGDASAVKVSNLLARAKESENQYVKEAAEECSESTNYDVTAKSLAAALDKLPG-VKEDNAVKTTFQSILTSLDNLDKDVKSVEQRAEELETALEKAERQLEKAEKAAEEAETESSKV--------------"

'''USAGE:
   obj - obj to color
   first - set to true (1) if the object corresponds to the s1 sequence. Set to false (0) if the object corresponds to s2 
   start - first aa residue number
   end - last aa residue number
'''

def color_from_fasta(obj, first, start, end):
    res = int(start)
    for i in range (0,len(s1)):
        if int(first) == 1 and s1[i] == '-':
            continue
        if int(first) == 0 and s2[i] == '-':
            continue
        if s1[i] not in all_aa or s2[i] not in all_aa:
            string= "grey90"
        elif s1[i] == s2[i]: 
            string="cbfa_green"
        elif s1[i] in g1 and s2[i] in g1 or s1[i] in g2 and s2[i] in g2 or s1[i] in g3 and s2[i] in g3 or s1[i] in g4 and s2[i] in g4 or s1[i] in g5 and s2[i] in g5 or s1[i] in g6 and s2[i] in g6:    
            string="cbfa_yellow"
        else:
            string="grey90"
        cmd.color(string, '%s and resi %s'%(obj, res))
        res += 1
cmd.extend("color_from_fasta", color_from_fasta)
