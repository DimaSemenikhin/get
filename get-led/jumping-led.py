import RPi.GPIO as r
import time
r.setmode(r.BCM)
leds=[16,5,25,17,27,23,22,24]
r.setup(leds,r.OUT)
r.output(leds,0)
light_time=0.2
while True:
    for led in leds:
        r.output(led,1)
        time.sleep(light_time)
        r.output(led,0)
    for led in reversed(leds): 
        r.output(led,1)
        time.sleep(light_time)
        r.output(led,0)