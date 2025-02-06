from machine import Pin, SPI
import time

from portExp_MCP23S08 import PortExp_MCP23S08

#############################################
# CONFIGURATION AND OBJECTS
# SPI BUS AND MCP23S08
hspi = SPI(1, 1000000)                      # Create the SPI bus object running at 1 MHz
pin_portexp_cs = 15                         # The MCP23S08 CS pin number
portexp_addr = 0                            # The MSP23S08 subaddress, not a real SPI thing!
portExp = PortExp_MCP23S08(hspi, pin_portexp_cs, portexp_addr)

# LED PINS
gp_led2         = 2                         # LED2: active low
gp_led3         = 3                         # LED3: active high

#############################################
# VARIABLES
# Non blocking flow control
timeLastToggle = 0
timeToggle = 500

#############################################
# PROGRAM
# Configure the port expander
portExp.write_register(portExp.IODIR, 0xF0) # Bulk setting of GP7:4 as input and GP3:0 as output, datasheet 1.6.1

print("Port Expander and LED 2 and LED 3 test program\n")

while True:
    if time.ticks_diff(time.ticks_ms(), timeLastToggle) > timeToggle:
        res = portExp.gp_get_value(gp_led2)
        if res == portExp.OFF:
            portExp.gp_set_value(gp_led2, portExp.ON)
            portExp.gp_set_value(gp_led3, portExp.ON)
        else:        
            portExp.gp_set_value(gp_led2, portExp.OFF)
            portExp.gp_set_value(gp_led3, portExp.OFF)
        
        timeLastToggle = time.ticks_ms()