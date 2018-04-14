import dcmotor
import time

def Centrize(center):
    
    if center <= 50:
        dcmotor.left(.75)
        time.sleep(.00001)
    if center <= 100:
        dcmotor.left(.5)
        time.sleep(.00001)
    if center <= 150:
        dcmotor.left(.25)
        time.sleep(.00001)
    if center <= 185:
        dcmotor.left(.1)
        time.sleep(.00001)
    if center <= 190:
        dcmotor.left(.02)
        time.sleep(.001)
        
    if center >= 350:
        dcmotor.right(.75)
        time.sleep(.00001)    
    if center >= 300:
        dcmotor.right(.5)
        time.sleep(.00001)    
    if center >= 250:
        dcmotor.right(.25)
        time.sleep(.00001)
    if center >= 215:
        dcmotor.right(.1)
        time.sleep(.00001)
    if center >= 210:
        dcmotor.right(.02)
        time.sleep(.001)
        