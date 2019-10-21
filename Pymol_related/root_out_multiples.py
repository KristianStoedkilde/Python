#!/usr/bin/python

import sys

#  USAGE: python root_out_multiples.py 'input.fasta' 'output.faste
#  Read a fasta file and remove any multiples of a sequence

name_list = []
sequence_list = []

input_file = str(sys.argv[1])
output_file = str(sys.argv[2])

output_f = open(output_file, "w+")

#Read lines and add to lists
with open(input_file) as f:
    content = f.readlines()

#Read lines and add to lists
    for line in content:
        if line.startswith('>'):
            name_list.append(line.strip())
            new_entry = True
        elif line.startswith('\n'):
            continue
        else:
            if (new_entry == True):
                sequence_list.append(line.strip())
                new_entry = False
            else:
                sequence_list[-1] = sequence_list[-1] + line.strip()
            if not line:
                break    

    multiples = 0    
    unique = 0            
    for x in range(0,len(sequence_list)):

        for y in range(x+1,len(sequence_list)):
            if (sequence_list[x] == sequence_list[y]):
                multiples += 1
                break

        else:
            unique += 1
            output_f.write(name_list[x] + "\r\n")
            output_f.write(sequence_list[x] + "\r\n")

    output_f.close()
    print ("Threw away %s sequences and kept %s uniques." %(str(multiples), str(unique)))  

  