import dcmotor
import time

def Centrize(centroidX):
    
    if centroidX <= 50:
        dcmotor.left(.5)
        time.sleep(.00001)
    if centroidX <= 100:
        dcmotor.left(.35)
        time.sleep(.00001)
    if centroidX <= 150:
        dcmotor.left(.25)
        time.sleep(.00001)
    if centroidX <= 185:
        dcmotor.left(.15)
        time.sleep(.00001)
    if centroidX <= 180:
        dcmotor.left(.025)
        time.sleep(.001)
        
    if centroidX >= 350:
        dcmotor.right(.5)
        time.sleep(.00001)    
    if centroidX >= 300:
        dcmotor.right(.35)
        time.sleep(.00001)    
    if centroidX >= 250:
        dcmotor.right(.25)
        time.sleep(.00001)
    if centroidX >= 215:
        dcmotor.right(.15)
        time.sleep(.00001)
    if centroidX >= 200:
        dcmotor.right(.025)
        time.sleep(.001)
        
        