import RPi.GPIO as r
import time
r.setmode(r.BCM)
leds=[16,12,25,17,27,23,22,24]
period=0.2

r.setup(leds,r.OUT)
def d2c(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]
num=0
up=9
down=10
r.setup(up,r.IN)
r.setup(down,r.IN)
while True:
    
    if r.input(up):
        time.sleep(0.2)
        if r.input(down):
            num=255
            time.sleep(0.2)
            
        else:
            num+=1
            print(num,d2c(num))
            time.sleep(0.2)
            if num==256:
                num=0
    if r.input(down):
        time.sleep(0.2)
        if r.input(up):
            num=255
            time.sleep(0.2)
        else:
            num-=1
            print(num,d2c(num))
            time.sleep(0.2)
    if num>=0 and num<256:
        for i in range(len(leds)):
            r.output(leds[i],d2c(num)[i])
    

        