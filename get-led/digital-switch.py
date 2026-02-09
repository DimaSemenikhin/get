import RPi.GPIO as r
import time

r.setmode(r.BCM)
led=23
r.setup(led,r.OUT)
r.setup(13,r.IN)
state=0
while True:
    if r.input(13)==1:
        state = not state
        r.output(led, state)
        time.sleep(0.2)
