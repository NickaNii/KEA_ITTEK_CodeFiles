# Potmeter test program
from machine import ADC, Pin, PWM
from time import sleep
#######################################
# Config
pin_potmeter = 34

#######################################
# Objects 
potmeter_adc = ADC(Pin(pin_potmeter))
potmeter_adc.atten(ADC.ATTN_11DB)      # FULL RANGE: 3,3V, 12 bits

#######################################
# Program
print("ADC and potmeter test\n")

while True:
    adc_val = potmeter_adc.read()
    print(adc_val)
    
    sleep(0.2)