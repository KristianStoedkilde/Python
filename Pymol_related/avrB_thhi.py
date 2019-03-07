import sys
#read lines from stdin
my_pdb = "thhi_final_070813_mod.pdb"
chains = [' A',' B',' C',' D',' E',' F',' G',' H',' I',' J',' K',' L',' M',' N',' O',' P',' Q',' R',' S',' T',' U',' V',' W',' X',' Y',' Z','AA','AB','AC','AD']

pATOM = 0 #total ATOM count
lATOM = 0 #total HETA count
  
###
 
for my_chain in chains:
    f = open(my_pdb,'r')
    pB = 0 #ATOM b factor
    lB = 0 #HETA b factor
    n = 0 #ATOM count 
    m = 0 #HETA count
    while 1:
        next = f.readline()
        if (next[0:4] == "ATOM") and (next[20:22] == my_chain):
            pB += float(next[60:66])
            n += 1
            pATOM +=1
        if (next[0:4] == "HETA") and (next[20:22] == my_chain):
            lB += float(next[60:66])
            m += 1
            lATOM +=1
         
        if not next:
            break
    
    print "Average protein B-factor: %.2f (%s). " % (pB/n,my_chain);
    if m != 0:
        print "Average ligand/ion B-factor: %.2f (%s)." % (lB/m,my_chain);
    f.close()
    
print "Total number of protein atoms: %i. Total number of ions: %i. " % (pATOM, lATOM)
 
