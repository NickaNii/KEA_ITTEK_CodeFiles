from machine import Pin, PWM
import time

pwm1 = PWM(Pin(26, Pin.OUT))
pwm1.freq(50)

while True:
    for i in range(50,150,5):
        pwm1.duty(i)
        time.sleep(1)
    
    for i in range(150,50,-5):
        pwm1.duty(i)
        time.sleep(1)