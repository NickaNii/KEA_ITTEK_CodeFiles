from servo import Servo
import time

motor=Servo(pin=14) # To be changed, depending on pin used
motor.move(0)       # turn servo 0°
time.sleep(0.3)
motor.move(90)      # turn servo 90°
time.sleep(0.3)
motor.move(180)     # turn servo 180°
time.sleep(0.3)
motor.move(90)      # turn servo 90°
time.sleep(0.3)
motor.move(0)       # turn servo 0°
time.sleep(0.3)