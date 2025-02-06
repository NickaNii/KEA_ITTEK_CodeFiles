from machine import Pin, PWM
import time

# Definer PWM-pinnen (tilpass etter hvilken pinne du bruker)
servo = PWM(Pin(14), freq=50)  # 50Hz for servo

# Funksjon for å sette servovinkel
def set_servo_angle(angle):
    min_duty = 1000  # Minimum puls (1 ms)
    max_duty = 9000  # Maksimum puls (2 ms)
    duty = min_duty + (angle / 180) * (max_duty - min_duty)
    servo.duty_u16(int(duty))

# Test: Beveg servoen fra 0 til 180 grader og tilbake
while True:
    for angle in range(0, 181, 10):  # 0 til 180 grader
        set_servo_angle(angle)
        time.sleep(0.1)
    for angle in range(180, -1, -10):  # 180 til 0 grader
        set_servo_angle(angle)
        time.sleep(0.1)