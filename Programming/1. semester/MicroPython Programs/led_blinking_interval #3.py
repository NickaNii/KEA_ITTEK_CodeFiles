# del 3
# import necessary systems and functions
from machine import Pin
from time import sleep

# define LED variable values
R_PIN = 26
Y_PIN = 12
G_PIN = 13

# define variable LED values
led1 = Pin(R_PIN, Pin.OUT)
led2 = Pin(Y_PIN, Pin.OUT)
led3 = Pin(G_PIN, Pin.OUT)

pb1 = Pin(4, Pin.IN) # define pushbutton 

Interval = float(input("Interval:"))

print(Interval)

while True:
    print("1")
    led1.on()
    print("2")
    led2.off()
    print("3")
    led3.on()
    sleep(Interval)
    print("-1")
    led1.off()
    print("-2")
    led2.on()
    print("-3")
    led3.off()
    sleep(Interval)
    