from __future__ import division
from pymol import cmd
import time
import shutil
import sys
import os
import re
from math import *

#Define ray tracing resolution
ray_x=320 #Use 2400 for high quality 
ray_y=160 #Use 1200 for high quality 

#define folder
folder = "movie/"
#define number of frames for the zoom
frames = 129
#define starting number
frame_number = 1

#set start view and end view
end_view = [\
  0.891403615,   -0.018484199,    0.452862412,\
    -0.452767789,   -0.081376761,    0.887922168,\
     0.020441070,   -0.996518254,   -0.080908760,\
     0.000452877,   -0.000771314, -161.017028809,\
    18.092020035,  -12.228412628,   58.962657928,\
    -8.321262360,  316.117614746,  -20.000000000]
start_view = [\
    0.891403615,   -0.018484199,    0.452862412,\
    -0.452767789,   -0.081376761,    0.887922168,\
     0.020441070,   -0.996518254,   -0.080908760,\
     0.000452877,   -0.000771314, -406.672210693,\
    18.092020035,  -12.228412628,   58.962657928,\
   237.333831787,  561.772583008,  -20.000000000]

#Set the camera view according to 18-point matrix
def setView (x):    
    view=""
    for i in range(len(x)):
        view+=`x[i]`
        if (i != (len(x)-1)):
            view+=","
    cmd.set_view(view)

def changeView (frames,start_view,end_view):        
    
    setView(x)
    ray()
    
    #get quaternions for interpolation between starting and target scenes
    qstart = mat2quat(x[0:9])
    qend = mat2quat(y[0:9])
	
    start_time = time.time()
    frame=1
    while frame <= frames:                    
        n=[]
        
        qcur = slerp(qstart, qend, frame/frames)
        matcur = quat2mat(qcur)

        for i in range(9):
            update=matcur[i]
            if abs(update) < 0.001:
		update = 0
            n.insert(i, update)
        
        for i in range(len(x)):	    
	    if (i>8):
		update=x[i] + (y[i] - x[i]) * (frame/frames)
		if abs(update) < 0.001:
                    update = 0
                n.insert(i, update)
                
        setView(n)
        frame+=1    
        cmd.ray(ray_x,ray_y)
        #Save image 
   	if frame < 10:
            cmd.png(folder + "frame00" + str(frame_number))
   	elif frame < 100:
            cmd.png(folder + "frame0" + str(frame_number))
    	else:
            cmd.png(folder + "frame" + str(frame_number))
    	frame_number+1
 	
	elapsed_time = time.time() - start_time
	total = (elapsed_time * (frames-frame_number)/60)
        print ("Done with image "+str(frame_number)+ "/" + str(frames) + ". Expected time left %.0f min." % total)
        frame += 1
    

#----------------------------------------------------------
#Methods to perform Spherical Linear Interpolation (SLERP)
#The code has been translated to python from sources 
#available at http://www.euclideanspace.com/maths/
#          algebra/realNormedAlgebra/quaternions/slerp/
#----------------------------------------------------------
def slerp(qa, qb, t):
    qm=[]
    
    #Calculate angles between quaternions
    cosHalfTheta = qa[0] * qb[0] + qa[1] * qb[1] 
                           + qa[2] * qb[2] + qa[3] * qb[3]
    #if qa=qb or qa=-qb then theta = 0 and we can return qa
    
    if (cosHalfTheta < 0):
        for i in range(4):
            qb[i] = -qb[i];
        cosHalfTheta = -cosHalfTheta
    
    if (abs(cosHalfTheta) >= 1.0):        
        for i in range(4):
            qm.insert(i,qa[i])
        return qm
    
    #Calculate temporary values
    halfTheta = acos(cosHalfTheta)
    sinHalfTheta = sqrt(1.0 - cosHalfTheta*cosHalfTheta)
    
    if (fabs(sinHalfTheta) < 0.000005):
    #fabs is floating point absolute
        for i in range(4):
            qm.insert(i, qa[i] * 0.5 + qb[i] * 0.5)        
        return qm

    ratioA = sin((1 - t) * halfTheta) / sinHalfTheta
    ratioB = sin(t * halfTheta) / sinHalfTheta
    #calculate Quaternion
    for i in range(4):
        qm.insert(i, qa[i] * ratioA + qb[i] * ratioB)
    return qm

def mat2quat(m):

    tr = m[0] + m[4] + m[8]

    if (tr > 0):
      S = sqrt(tr+1) * 2;
      qw = 0.25 * S;
      qx = (m[7] - m[5]) / S;
      qy = (m[2] - m[6]) / S; 
      qz = (m[3] - m[1]) / S; 
    
    elif ((m[0] > m[4])&(m[0] > m[8])):
      S = sqrt(1 + m[0] - m[4] - m[8]) * 2
      qw = (m[7] - m[5]) / S;
      qx = 0.25 * S;
      qy = (m[1] + m[3]) / S; 
      qz = (m[2] + m[6]) / S; 
    
    elif (m[4] > m[8]):
      S = sqrt(1 + m[4] - m[0] - m[8]) * 2
      qw = (m[2] - m[6]) / S;
      qx = (m[1] + m[3]) / S; 
      qy = 0.25 * S;
      qz = (m[5] + m[7]) / S; 
    
    else:
      S = sqrt(1 + m[8] - m[0] - m[4]) * 2
      qw = (m[3] - m[1]) / S;
      qx = (m[2] + m[6]) / S;
      qy = (m[5] + m[7]) / S;
      qz = 0.25 * S;
    
    return [qx,qy,qz,qw]
        

def quat2mat( Q ):
    
    xx = Q[0]*Q[0]
    xy = Q[0]*Q[1]
    xz = Q[0]*Q[2]
    xw = Q[0]*Q[3]
    yy = Q[1]*Q[1]
    yz = Q[1]*Q[2]
    yw = Q[1]*Q[3]
    zz = Q[2]*Q[2]
    zw = Q[2]*Q[3]
    
    
    M = [1.0 - 2*yy - 2*zz,
         2*xy - 2*zw,
         2*xz + 2*yw,
        2*xy + 2*zw,
        1 - 2*xx - 2*zz,
        2*yz - 2*xw,
        2*xz - 2*yw,
        2*yz + 2*xw,
        1 - 2*xx - 2*yy]
    
    return M


