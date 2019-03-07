import sys
#read lines from stdin
my_pdb = "thhi_final_070813.pdb"
new_file = my_pdb[:-4] + "_mod.pdb"
###
list = ['NAG','HEM','OXY','HOH','FUC']   
count =0
n = 0
f = open(my_pdb,"r")
output = open(new_file, "a")

for next in f.readlines():
    count +=1
    if (next[0:4] == "ATOM" and next[17:20] in list):
        next = next.replace('ATOM', 'HETA')
        n +=1
    output.write(next)
    if not next:
        break
print "Changed %i entries. Total number of lines %i.\nChanges written to %s " % (n,count,new_file);
    
f.close()
output.close()
