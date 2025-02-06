from machine import Pin, PWM
from time import sleep
# opretter instans af HCSR04 klassen
buzzer_PIN = Pin(14, Pin.OUT)
buzzer_PWM = PWM(buzzer_PIN, duty=0)

# starter event loop
while True:
    print("Low")
    buzzer_PWM.freq(50)
    buzzer_PWM.duty(50)
    sleep(5)
    print("High")
    buzzer_PWM.freq(50)
    buzzer_PWM.duty(100)
    sleep(5)