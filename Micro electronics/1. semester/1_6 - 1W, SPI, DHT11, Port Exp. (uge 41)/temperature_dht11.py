# A simple DHT11 test program 
from machine import Pin
from time import sleep
import dht 

########################################
# CONFIGURATION
dht11_pin = 19                         # The DHT11 pin

########################################
# OBJECTS
dht11 = dht.DHT11(Pin(dht11_pin))      # The DHT11 object

########################################
# PROGRAM
while True:
    # Make the measurement
    dht11.measure()               
    temp = dht11.temperature()         # Get the temperature
    hum = dht11.humidity()             # Get the humidity
        
    # Print the result
    print('Temperatur: %3d °C' % temp)
    print('Fugtighed : %3d %%' % hum)
  
    sleep(1)                           # Wait for 1 s then loop around

