from neopixel import NeoPixel
from machine import Pin

n = 12
p = 12
np = NeoPixel(Pin(p, Pin.OUT), n)

def clear():
    for i in range(n):
        np[i] = (0, 0, 0)
        np.write()
        
clear()
