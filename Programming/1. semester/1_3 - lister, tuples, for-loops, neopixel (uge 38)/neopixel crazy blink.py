from neopixel import NeoPixel
from machine import Pin
from time import sleep

n = 12
p = 12
np = NeoPixel(Pin(p, Pin.OUT), n)

while True:
    np[0] = (255, 255, 255)
    np[3] = (255, 0, 0)
    np[6] = (0, 255, 0)
    np[11] = (0, 255, 255)

    np.write()
    sleep(0.1)

    np[0] = (0, 0, 0)
    np[3] = (0, 255, 0)
    np[6] = (0, 0, 0)
    np[11] = (0, 0, 255)

    np.write()
    sleep(0.1)
    
    np[0] = (0, 255, 0)
    np[3] = (0, 0, 100)
    np[6] = (40, 0, 0)
    np[11] = (0, 120, 255)

    np.write()
    sleep(0.1)
    
    np[0] = (255, 255, 255)
    np[3] = (255, 255, 255)
    np[6] = (255, 255, 255)
    np[11] = (255, 255, 255)

    np.write()
    sleep(0.1)