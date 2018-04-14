from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2

import dcmotor
import color_centrize
    
def Green():
    print("[INFO] starting video stream...")
    #vs = VideoStream(src=0).start()
    vs = VideoStream(usePiCamera=True).start()
    time.sleep(0.5)
    fps = FPS().start()
    a = 0
    while True:
        frame = vs.read()
        frame = imutils.rotate_bound(frame, 180)
        frame = imutils.resize(frame, width=400)
        #for i in range(0,300):
            #print(frame[i][200])
        #qw
        lower = np.array([0, 108, 70])
        upper = np.array([3, 140, 100])
        #hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(frame, lower, upper)
        mask = cv2.erode(mask, None, iterations = 2)
        mask = cv2.dilate(mask, None, iterations=5)
        color = cv2.bitwise_and(frame, frame, mask = mask)
    
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None
        
        if len(cnts) == 0:
            dcmotor.left(2)
            time.sleep(.1)
        
        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            rect = cv2.minAreaRect(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            if rect[1][0] > 10:
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                frame = cv2.drawContours(frame,[box],0,(0,0,255),2)
            center = center[0]
            if(center<=190 or center>=210): 
                color_centrize.Centrize(center)
            elif(rect[1][0]<=200):
                if rect[1][0]<=100:
                    dcmotor.forward(3)
                elif rect[1][0]<=200:
                    dcmotor.forward(1)
            if(center>=190 and center<=210 and rect[1][0]>=150):
                a = 1
        if a == 1:
            break
        
        cv2.imshow("Frame", frame)
        cv2.imshow("Color", color )
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break
        fps.update()

    fps.stop()
    print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    cv2.destroyAllWindows()
    vs.stop()
    return a

####################################################################



def Blue():
    print("[INFO] starting video stream...")
    #vs = VideoStream(src=0).start()
    vs = VideoStream(usePiCamera=True).start()
    time.sleep(0.5)
    fps = FPS().start()
    b = 0
    while True:
        frame = vs.read()
        frame = imutils.rotate_bound(frame, 180)
        frame = imutils.resize(frame, width=400)
        #for i in range(0,300):
            #print(frame[i][200])
        #fsh
        lower = np.array([15, 70, 0])
        upper = np.array([115, 155, 20])
        #hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(frame, lower, upper)
        mask = cv2.erode(mask, None, iterations = 1)
        mask = cv2.dilate(mask, None, iterations=3)
        color = cv2.bitwise_and(frame, frame, mask = mask)
    
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None
        
        if len(cnts) == 0:
            dcmotor.left(2)
            time.sleep(.1)
        
        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            rect = cv2.minAreaRect(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            if rect[1][0] > 10:
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                frame = cv2.drawContours(frame,[box],0,(0,0,255),2)
            center = center[0]
            if(center<=190 or center>=210): 
                color_centrize.Centrize(center)
            elif(rect[1][0]<=200):
                if rect[1][0]<=100:
                    dcmotor.forward(3)
                elif rect[1][0]<=220:
                    dcmotor.forward(1)
            if(center>=190 and center<=210 and rect[1][0]>=220):
                b = 1
        if b == 1:
            dcmotor.forward(1)
            break
        
        cv2.imshow("Frame", frame)
        cv2.imshow("Color", color )
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord("q"):
            break
        fps.update()

    fps.stop()
    print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    cv2.destroyAllWindows()
    vs.stop()
    return b
