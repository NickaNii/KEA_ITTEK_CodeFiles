from machine import I2C, Pin
from time import sleep

################
#Objects & variables
i2c = I2C(0)                        #SDA: 19, SCL: 18

################
# program
print("\nRunning I2C scanner on I2C H/W 0\n")

while True:
    devicesIdentified = i2c.scan()
    
    devicesCount = len(devicesIdentified)
    print("Total number of devices: %d" % devicesCount)
    
    if devicesCount == 112:         # 16 reserved addresses, so not 128
        print("Looks like the I2C buss pull-up resistors are missing")
    else:
        for i in range(devicesCount):
            print("Device found at address: 0x%02X" % devicesIdentified[i])
            
    print()
    
    sleep(1)