from __future__ import division
from pymol import cmd
import time

nframes = 309
frame = 130
count = 1

cmd.set("stick_transparency",1)

while (frame <= nframes):
    cmd.set("cartoon_transparency",(0.005*count)) 
    cmd.set("stick_transparency",(1-(0.00555*count)))
    cmd.set("stick_transparency",0,"disulfE")
    cmd.set("stick_transparency",0,"HemB")
    start_time = time.time()
    cmd.ray(2400)
    elapsed_time = time.time() - start_time
    if frame < 10:
        cmd.png("frame00" + str(frame))
    elif frame <100:
        cmd.png("frame0" + str(frame))
    else:
        cmd.png("frame" + str(frame))
    total = (elapsed_time * (nframes-frame)/60)
    print ("Done with image "+str(frame)+"/"+str(nframes) + ". Expected time left %.0f min." % total)
    frame += 1
    count += 1
#ffmpeg -f image2 -i frame%d.png -s 2000x1000 interaction.mp4
