import RPi.GPIO as r
r.setmode(r.BCM)
r.setup(26,r.OUT)
r.setup(6,r.IN)
while True:
    r.output(26,not r.input(6))