import utime
from microbit import i2c,pin12,pin13
import PCA9685
pca9685 = PCA9685.PCA9685(i2c)
def Ultrasonic_ranging():
    Trig, Echo = pin12,pin13
    global Distance
    Trig.write_digital(0)
    Trig.write_digital(1)
    utime.sleep_us(10)
    Trig.write_digital(0)
    while(Echo.read_digital()==0):
        pass
    t1 = utime.ticks_us()
    while(Echo.read_digital()==1):
        pass
    t2 = utime.ticks_us()
    t3 = utime.ticks_diff(t2,t1)/10000
    print("\r"+":{:5.0f}cm".format(t3*340/2),end='')
    Distance=int(t3*340/2)
while True:
    Ultrasonic_ranging()