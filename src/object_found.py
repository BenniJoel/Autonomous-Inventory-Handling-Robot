import time
import dcmotor

def towards_object(a):
    if a<40:
        dcmotor.forward(4)
        time.sleep(.00001)
    elif a<70:
        dcmotor.forward(1)
        time.sleep(.00001)
    elif a<110:
        dcmotor.forward(.5)
        time.sleep(.00001)
    elif a<=135:
        dcmotor.forward(.2)
        time.sleep(.00002)