import os
os.system ("sudo pigpiod")
import time
import pigpio
 
gservo = 13
servo1 = 19
bservo = 26

pi=pigpio.pi()

pi.write(gservo, 1)
pi.write(servo1, 1)
pi.write(bservo, 1)

def pick():
    pi.set_servo_pulsewidth(gservo, 1490)
    time.sleep(.05)
    #close
    pi.set_servo_pulsewidth(gservo, 1450) 
    time.sleep(.6)
    pi.set_servo_pulsewidth(gservo, 1490)
    time.sleep(.05)

    pi.set_servo_pulsewidth(servo1, 1490)
    time.sleep(.05)
    #back
    pi.set_servo_pulsewidth(servo1, 1440) 
    time.sleep(.8)
    pi.set_servo_pulsewidth(servo1, 1490)
    time.sleep(.05)
    
    #up
    pi.set_servo_pulsewidth(bservo, 1600)
    time.sleep(1)

    pi.set_servo_pulsewidth(servo1, 0);
    pi.set_servo_pulsewidth(gservo, 0);
    pi.set_servo_pulsewidth(bservo, 0);
    
def place():
    #down
    pi.set_servo_pulsewidth(bservo, 1400) 
    time.sleep(1)
    
    pi.set_servo_pulsewidth(servo1, 1490)
    time.sleep(.05)
    #fro
    pi.set_servo_pulsewidth(servo1, 1540)
    time.sleep(.4)
    pi.set_servo_pulsewidth(servo1, 1490)
    time.sleep(.05)

    pi.set_servo_pulsewidth(gservo, 1490)
    time.sleep(.05)
    #open
    pi.set_servo_pulsewidth(gservo, 1550)
    time.sleep(.2)
    pi.set_servo_pulsewidth(gservo, 1490)
    time.sleep(.05)

    pi.set_servo_pulsewidth(servo1, 0);
    pi.set_servo_pulsewidth(gservo, 0);
    pi.set_servo_pulsewidth(bservo, 0);
