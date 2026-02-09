import RPi.GPIO as r
import time
r.setmode(r.BCM)
r.setup(26,r.OUT)
led=26

pwm=r.PWM(led,200)
duty=0.0
pwm.start(duty)
period=0.05
while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(period)

    duty+=1
    if duty>100.0:
        duty=0.0