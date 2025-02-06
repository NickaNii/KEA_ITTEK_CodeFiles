from machine import Pin
from time import sleep

pb1 = Pin(6, Pin.IN) # Pin objekt


while True:
    # pin objekts value() + gemmer resultat før variabel
    first = pb1.value()
    sleep(0.01)
    second = pb1.value()
    # ikke trykket (1) til trykket (0)
    if first == 1 and second == 0:
        print("Knap! trykket!! jaha!!")
        # kan evt køre kode når knappen trykkes
        
    # hvis knap går fra (0) ti (1)
    if first == 0 and second == 1:
        print("DU GAV SLIP PÅ KNAPPEN!!")