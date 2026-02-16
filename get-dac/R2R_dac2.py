import RPi.GPIO as r
class R2R_DAC():
    def __init__(self,gpio_bits,dynamic_range,verbose=False):
        self.gpio_bits=gpio_bits
        self.dynamic_range=dynamic_range
        self.verbose=verbose

        r.setmode(r.BCM)
        r.setup(self.gpio_bits,r.OUT,initial=0)
    def deinit(self):
        r.output(self.gpio_bits,0)
        r.cleanup()
    def set_number(self,number):
        dac= [int(i) for i in bin(number)[2:].zfill(8)]
        for i in range(8):
            r.output(self.gpio_bits[i],dac[i])
    def set_voltage(self,value):
        if not ((0<=value) and (value<=self.dynamic_range)):
            print("Напряжение выходит за динамический диапазон ЦАП (0.00-3.15B)")
            print("устанавливаем 0.0В")
            self.set_number(0)
            return 0
        self.set_number(int(value/self.dynamic_range*255))


if __name__=="__main__":
    try:
        dac=R2R_DAC([16,20,21,25,26,17,27,22],3.15,True)
        while True:
            try:

                voltage=float(input("введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("вы ввели не число")
    finally:
        dac.deinit()
