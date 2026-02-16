import RPi.GPIO as r
import time
r.setmode(r.BCM)
dac_bits=[16,20,21,25,26,17,27,22]
r.setup(dac_bits,r.OUT)
r.output(dac_bits,0)