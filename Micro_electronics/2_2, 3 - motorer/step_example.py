# copied and edited from microcontollerslab.com
# setup for step motor
from machine import Pin
from time import sleep

# Objects
IN1 = Pin(26,Pin.OUT)
IN2 = Pin(25,Pin.OUT)
IN3 = Pin(33,Pin.OUT)
IN4 = Pin(32,Pin.OUT)

pins = [IN1, IN2, IN3, IN4]

cw_rotate = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
ccw_rotate = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]

while True:
    for step in cw_rotate:
        for i in range(len(pins)):
            pins[i].value(step[i])
            sleep(0.001)