import smbus
import time
import matplotlib.pyplot as plt


class MCP3021():
    def __init__(self,dynamic_range,verbose=True):
        self.bus=smbus.SMBus(1)
        self.dynamic_range=dynamic_range
        self.address=0x4D
        self.verbose=verbose

    def deinit(self):
        self.bus.close()

    def get_number(self):
        data=self.bus.read_word_data(self.address,0)
        lower_data_byte=data>>8
        upper_data_byte=data&0xFF
        number=(upper_data_byte<<6)|(lower_data_byte>>2)
        #if self.verbose:
            #print(f"Принятые данные: {data}, Старший байт: {upper_data_byte:x}, Младший байт: {lower_data_byte:x},Число: {number}")
        return number
    def get_voltage(self):
        print(f"Напряжение на входе: {self.get_number()/(2**10)*5.1}")
        return self.get_number()/(2**10)*5


def plot1(adc,time1):
        time_start=time.time()
        times=[]
        dots=[]
        sampling_periods=[]
        time_last=time_start
        while (time.time()-time_start)<time1:
            cur=adc.get_voltage()
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
    mcp=MCP3021(3.15)
    #while True:
    #    mcp.get_voltage()

    plot1(mcp,10)

finally:
    mcp.deinit()