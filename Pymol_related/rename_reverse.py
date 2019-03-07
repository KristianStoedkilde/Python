import os
directory = "/home/ksj/Documents/coluaa2013/video_interactions/tmp2/"
start_number = 1162
files =0
count = 0
for x in os.listdir(directory):
    files +=1
print "Found %i files." %files

for filename in sorted(os.listdir(directory)):
    path = os.path.join(directory, filename)
    target = os.path.join(directory, "frame" + str(start_number + files - count)+ ".png")
    os.rename(path, target)
    count +=1


