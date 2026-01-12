import cv2 
import numpy as np 
from djitellopy import Tello
from cvzone.FaceMeshModule import FaceMeshDetector 
import keypressmodule as kp 
import time 

drone = Tello()
drone.connect() 
drone.streamon()
print(drone.get_battery())
kp.init()


fbRange = [6200,6800]
pid =[0.4,0.4,0]
w,h = 360, 240 

pError = 0 

faceCascade = FaceMeshDetector(maxFaces=1)

def findFace(img):
    img, faces = faceCascade.findFaceMesh(img)
    frame_height, frame_width, _ = img.shape
    myFaceListC = []
    myFaceListArea = []

    if faces: 
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374] 
        w, _ = faceCascade.findDistance(pointLeft,pointRight)
        nose = face[1]
        cx , cy = nose
        W = 6.3
        f = 840
        d = (W*f)/w 
        area = int(d) 
        myFaceListC.append([cx,cy])
        myFaceListArea.append(area)

    if len(myFaceListArea) != 0 :
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i] , myFaceListArea[i]]    
        
    else :
            
        return img , [[0,0],0]

def trackFace(info,w,pid,pError):

    area = info[1]
    x , y = info[0]
    fb = 0  

    error = x - w//2
    speed = pid[0] * error + pid[1] * (error-pError) 
    speed = int(np.clip(speed,-100,100))

    
    if area>80 and area<140  :
        fb = 0
        print('stopping')

    if area<80 and area !=0: 
        fb =-20
        print('backward')
    if area>140:
        fb = 20 
        print('forward') 
    
    if x==0 :
        speed = 0
        error = 0 
    drone.send_rc_control(0,fb,0,speed) 
    return error


while True :
    img = drone.get_frame_read().frame
    img = cv2.resize(img,(w,h))
    img,info = findFace(img) 
    pError = trackFace(info,w , pid , pError)
    if kp.getKey('t'):
        drone.takeoff()
        drone.send_rc_control(0,0,50,0)
        time.sleep(2.2) 
    if kp.getKey('q'): 
        drone.land()
    cv2.imshow('output',img)
    k = cv2.waitKey(1)

    if k == 27:
        quit() 