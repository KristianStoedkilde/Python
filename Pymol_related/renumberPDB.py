#Renumber PDB file. 
# arg1 : file
# arg2 : change in number

import sys

input_file = str(sys.argv[1])
renumberValue = str(sys.argv[2])

new_file = input_file[:-4] + "_renumbered.pdb"
  
f = open(input_file,"r")
output = open(new_file, "w")

for next in f.readlines():
    if (next[0:4] == "ATOM"):
    	newNumber = int(next[23:26]) + int(renumberValue)
        next = next[0:22] + str(newNumber).rjust(4,' ') + next[27:78]
    output.write(next)
    if not next:
        break
print "Pdb renumbered by %s written to %s." % (renumberValue, new_file);
    
f.close()
output.close()
