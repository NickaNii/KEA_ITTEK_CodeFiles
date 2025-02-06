from machine import Pin, PWM
from time import sleep

motor_l_pin = Pin(12, Pin.OUT)
motor_r_pin = Pin(14, Pin.OUT)
motor_l = PWM(motor_l_pin, duty=0)
motor_r = PWM(motor_r_pin, duty=0)

def turn(pwm_object, duty, on_time = 1):
    print(f"Turning motor{pwm_object}\nwith duty {duty} for {on_time} second")
    pwm_object.freq(5000)
    pwm_object.duty(duty)
    sleep(on_time)
    pwm_object.duty(0)
    print(f"Done")


turn(motor_l, 800, 3)
turn(motor_r, 1023, 3)
#for i in range (1023):
    #turn(motor_l, 1023-i, 0.1) #Lowest duty: 371     