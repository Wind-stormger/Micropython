#For the time being, this code only applies to microbit V1&V2
from microbit import pin12,pin13,running_time
from machine import time_pulse_us
import utime
def Ultrasonic_ranging():
    Trig, Echo = pin12,pin13
    global Distance
    start_time=0
    if (running_time()-start_time>100):
        Trig.write_digital(0)
        Trig.write_digital(1)
        utime.sleep_us(2)
        Trig.write_digital(0)
        t1=time_pulse_us(Echo,1,5000)
        t2 = t1/1000000
        print("\r"+":{:5.2f}cm".format(t2*34300/2),end='')
        Distance=int(t2*34300/2)
while True:
    Ultrasonic_ranging()