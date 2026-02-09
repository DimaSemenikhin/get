import RPi.GPIO as r
import time
r.setmode(r.BCM)
led = 26
r.setup(led,r.OUT)
state=0
period=0.5
while True:
    r.output(led,state)
    state = not state
    time.sleep(period)
    