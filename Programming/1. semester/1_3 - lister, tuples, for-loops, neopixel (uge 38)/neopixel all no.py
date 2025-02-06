from neopixel import NeoPixel
from time import sleep
from machine import Pin

n = 12 # number of pixels in the Neopixel ring
p = 12 # pin attached to Neopixel ring
np = NeoPixel(Pin(p, Pin.OUT), n) # create NeoPixel instance

np[0]=(0,50,0)
np[1]=(0,50,0)
np[2]=(0,50,0)
np[3]=(0,0,50)
np[4]=(0,0,50)
np[5]=(0,0,50)
np[6]=(50,0,0)
np[7]=(50,0,0)
np[8]=(50,0,0)
np[9]=(75,50,0)
np[10]=(75,50,0)
np[11]=(75,50,0)
np.write()