import RPi.GPIO as r
import time
r.setmode(r.BCM)
dac_bits=[16,20,21,25,26,17,27,22]
r.setup(dac_bits,r.OUT)
dynamic_range=3.15
def voltage_to_number(value):
    if not ((0<=value) and (value<=dynamic_range)):
        print("Напряжение выходит за динамический диапазон ЦАП (0.00-3.15B)")
        print("устанавливаем 0.0В")
        return 0
    return int(value/dynamic_range*255)

def number_to_decimal(value):
    dac= [int(i) for i in bin(value)[2:].zfill(8)]
    for i in range(8):
        r.output(dac_bits[i],dac[i])

try:
    while True:
        try:
            voltage=float(input("Введите напряжение в Вольтах: "))
            number=voltage_to_number(voltage)
            number_to_decimal(number)
        except ValueError:
            print("вы ввели не число.")
finally:
    r.output(dac_bits,0)
    r.cleanup()