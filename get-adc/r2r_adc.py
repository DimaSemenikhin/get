import RPi.GPIO as r
import time as time
import matplotlib.pyplot as plt


class R2R_ADC:
    def __init__(self,dynamic_range,compare_time=0.001,verbose=False):
        self.dynamic_range=dynamic_range
        self.compare_time=compare_time
        self.verbose=verbose

        self.bits_gpio=[26,20,19,16,13,12,25,11]
        self.comp_gpio=21

        r.setmode(r.BCM)
        r.setup(self.bits_gpio,r.OUT,initial=0)
        r.setup(self.comp_gpio,r.IN)

    def deinit(self):
        r.output(self.bits_gpio,0)
        r.cleanup()

    def number_to_dac(self,number):
        dac= [int(i) for i in bin(number)[2:].zfill(8)]
        for i in range(8):
            r.output(self.bits_gpio[i],dac[i])
    def sequencial_counting(self):
        for i in range(256):
            self.number_to_dac(i)
            time.sleep(self.compare_time)
            if r.input(self.comp_gpio)==1:
                print("Значение АЦП",i-1 ,"Напрежяние на входе ",(i-1)/256*self.dynamic_range)
                return((i-1)/256*self.dynamic_range)
                break
    def succesive_approximation_adc(self):
        cur=0
        cur_check=0
        for i in range(8):
            cur_check+=2**(7-i)
            self.number_to_dac(cur_check)
            time.sleep(self.compare_time)
            if r.input(self.comp_gpio)==0:
                cur=cur_check
            else:
                cur_check-=2**(7-i)
        return cur
    def get_sar_voltage(self):
        cur=self.succesive_approximation_adc()
        print("Значение",cur,'напряжение на входе',cur/256*self.dynamic_range)
        return cur
        


    

def plot(adc,time1):
        time_start=time.time()
        times=[]
        dots=[]
        sampling_periods=[]
        time_last=time_start
        while (time.time()-time_start)<time1:
            cur=adc.sequencial_counting()
            times.append(time.time()-time_start)
            sampling_periods.append(time.time()-time_last)
            time_last=time.time()
            

            dots.append(cur)
        plt.figure(figsize=(10,6))
        plt.plot(times,dots)
        plt.show()

        plt.figure(figsize=(10,6))
        #plt.xlim(0,0.06)
       
        plt.xlabel("Период измерения, с")
        plt.ylabel("Количество измерений")
        plt.hist(sampling_periods)
        plt.show()

def plot2(adc,time1):
        time_start=time.time()
        times=[]
        dots=[]
        sampling_periods=[]
        time_last=time_start
        while (time.time()-time_start)<time1:
            cur=adc.get_sar_voltage()
            times.append(time.time()-time_start)
            sampling_periods.append(time.time()-time_last)
            time_last=time.time()
            

            dots.append(cur)
        plt.figure(figsize=(10,6))
        plt.plot(times,dots)
        plt.show()
        plt.figure(figsize=(10,6))
        #plt.xlim(0,0.06)
       
        plt.xlabel("Период измерения, с")
        plt.ylabel("Количество измерений")
        plt.hist(sampling_periods)
        plt.show()


try:
    adc=R2R_ADC(3.15,compare_time=0.001)
    #plot(adc,5)

    #while True:
    #    cur=adc.sequencial_counting()
    
    #while True:
    #    adc.get_sar_voltage()

    plot2(adc,5)


finally:
    adc.deinit()