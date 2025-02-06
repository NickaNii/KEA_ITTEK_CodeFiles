from machine import Pin, PWM
from time import sleep

MOTOR_PIN = 14
motor_pin = Pin(MOTOR_PIN, Pin.OUT)
motor_pwm = PWM(motor_pin, duty=0)

def motor(pwm_object, duty, silence_duration):
    pwm_object.freq(5000)
    pwm_object.duty(duty)
    sleep(silence_duration)
    pwm_object.duty(0)
    
while True:
    motor(motor_pwm, 800, 3)
    motor(motor_pwm, 1023, 3)
    motor(motor_pwm, 0, 3)

