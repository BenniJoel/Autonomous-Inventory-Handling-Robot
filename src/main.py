x=0
y=0
while True:
    try:
        import object_detection as od
        import color
        import os
        os.system ("sudo pigpiod")
        import pandp
        import time
        import pigpio
        import dcmotor
        import placenter

        gservo = 13
        servo1 = 19
        bservo = 26
 
        pi=pigpio.pi()

        pi.write(gservo, 1)
        pi.write(servo1, 1)
        pi.write(bservo, 1)

        a=1#color.Green()
        print(a)
        if a==1:
            #down
            #pi.set_servo_pulsewidth(bservo, 1400) 
            #time.sleep(1)
    
            #pi.set_servo_pulsewidth(servo1, 1490)
            #time.sleep(.05)
            #fro
            #pi.set_servo_pulsewidth(servo1, 1540)
            #time.sleep(.4)
            #pi.set_servo_pulsewidth(servo1, 1490)
            #time.sleep(.05)
            
            f = 1#od.Object()
            print(f)
            if f==1:
                #pandp.pick()
                b = 1#color.Blue()
                
                dcmotor.backward(y)
                dcmotor.left(2.2)
                
                dcmotor.forward(3-x)
                x+=1
                if x == 3:
                    x=0
                    y+=1
                    if y == 3:
                        y=0
                #placenter.Center()
                
                print(b)
                #if b == 1:
                    #pandp.place()
                    #dcmotor.backward(1)
                    
                    #pi.set_servo_pulsewidth(servo1, 1490)
                    #time.sleep(.05)
                    #back
                    #pi.set_servo_pulsewidth(servo1, 1440) 
                    #time.sleep(.8)
                    #pi.set_servo_pulsewidth(servo1, 1490)
                    #time.sleep(.05)
    
                    #up
                    #pi.set_servo_pulsewidth(bservo, 1600)
                    #time.sleep(1)
                
        pi.set_servo_pulsewidth(servo1, 0);
        pi.set_servo_pulsewidth(gservo, 0);
        pi.set_servo_pulsewidth(bservo, 0);
                    
    except KeyboardInterrupt:
        pi.set_servo_pulsewidth(servo1, 0);
        pi.set_servo_pulsewidth(gservo, 0);
        pi.set_servo_pulsewidth(bservo, 0);
        dcmotor.stopdc()
        break
    
            
