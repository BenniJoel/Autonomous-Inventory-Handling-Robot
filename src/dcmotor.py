import RPi.GPIO as gpio
import time
import pandp

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(16,gpio.OUT)
    gpio.setup(18,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    
    gpio.setup(19,gpio.OUT)
    gpio.setup(21,gpio.OUT)
    gpio.setup(23,gpio.OUT)
    
def backward(tf):
    init()
    print("Going Backwards")
    gpio.output(16,gpio.HIGH)
    gpio.output(18,gpio.LOW)
    gpio.output(22,gpio.HIGH)
    
    gpio.output(19,gpio.HIGH)
    gpio.output(21,gpio.LOW)
    gpio.output(23,gpio.HIGH)
    
    time.sleep(tf)
    gpio.cleanup()
    
def forward(tf):
    init()
    print("Going Forwards")
    gpio.output(16,gpio.LOW)
    gpio.output(18,gpio.HIGH)
    gpio.output(22,gpio.HIGH)
    
    gpio.output(19,gpio.LOW)
    gpio.output(21,gpio.HIGH)
    gpio.output(23,gpio.HIGH)
    
    time.sleep(tf)
    gpio.cleanup()
    
def right(tf):
    init()
    print("Turning Right")
    gpio.output(16,gpio.HIGH)
    gpio.output(18,gpio.LOW)
    gpio.output(22,gpio.HIGH)
    
    gpio.output(19,gpio.LOW)
    gpio.output(21,gpio.HIGH)
    gpio.output(23,gpio.HIGH)
    
    time.sleep(tf)
    gpio.cleanup()
    
def left(tf):
    init()
    print("Turning Left")
    gpio.output(16,gpio.LOW)
    gpio.output(18,gpio.HIGH)
    gpio.output(22,gpio.HIGH)
    
    gpio.output(19,gpio.HIGH)
    gpio.output(21,gpio.LOW)
    gpio.output(23,gpio.HIGH)
    
    time.sleep(tf)
    gpio.cleanup()
    
def stopdc():
    init()
    print("Stopping DC")
    gpio.output(22,gpio.LOW)
    gpio.output(23,gpio.LOW)
    gpio.cleanup()

#180 right(4.35)
#90 right(2.22)
#45 right(1.1)