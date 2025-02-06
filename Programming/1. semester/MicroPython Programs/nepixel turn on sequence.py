from neopixel import NeoPixel
from machine import Pin
from time import sleep

n = 12
p = 12
np = NeoPixel(Pin(p, Pin.OUT), n)

def clear():
    for i in range(n):
        np[i] = (0, 0, 0)
        np.write()

clear()

while True:
    np[0] = (0, 0, 80)
    sleep(0.1)
    np.write()
    np[1] = (0, 80, 0)
    sleep(0.1)
    np.write()
    np[2] = (80, 0, 0)
    sleep(0.1)
    np.write()
    np[3] = (0, 0, 160)
    sleep(0.1)
    np.write()
    np[4] = (0, 160, 0)
    sleep(0.1)
    np.write()
    np[5] = (160, 0, 0)
    sleep(0.1)
    np.write()
    np[6] = (0, 0, 240)
    sleep(0.1)
    np.write()
    np[7] = (0, 240, 0)
    sleep(0.1)
    np.write()
    np[8] = (240, 0, 0)
    sleep(0.1)
    np.write()
    np[9] = (0, 0, 255)
    sleep(0.1)
    np.write()
    np[10] = (0, 255, 0)
    sleep(0.1)
    np.write()
    np[11] = (255, 0, 0)
    sleep(0.1)
    np.write()
    sleep(0.5)
    clear()
    sleep(0.1)