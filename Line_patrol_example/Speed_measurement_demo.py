import time
import pca9685
import microbit as m
from machine import I2C,Pin
IR_R=0
IR_R_2=0
Count_R=0
once_time=0
start_time=0
i2c=I2C(sda=Pin(21),scl=Pin(22),freq=10000) #I2C initialization
pca9685 = pca9685.PCA9685(i2c,address=0x40) #Reference to pca9685 object,I2C address of pca9685
pca9685.freq(freq=50)

def Motor_control(Right_motor_control,Left_motor_control):
    R0=int(2047-2047/100*Right_motor_control)
    R1=int(2048+2047/100*Right_motor_control)
    L0=int(2048+2047/100*Left_motor_control)
    L1=int(2047-2047/100*Left_motor_control)
    pca9685.duty(0,value=R0,invert=False)
    pca9685.duty(1,value=R1,invert=False)
    pca9685.duty(2,value=L0,invert=False)
    pca9685.duty(3,value=L1,invert=False)
     
def Speed_measurement_R():#Test the RPM of the right motor
    global IR_R,IR_R_2,Count_R,start_time,once_time
    m.pin14.write_digital(1)
    IR_R=m.pin5.read_digital()
    if IR_R != IR_R_2:
        IR_R_2 = IR_R
        Count_R=Count_R+1
        #print("Count_R:{:2.0f}".format(Count_R))
        if Count_R==1:            
            start_time=time.ticks_ms()
        if Count_R==24:
            once_time=time.ticks_ms()-start_time
            RPM_R=60000/once_time
            print("\r"+"RPM_R:{:3.0f}r/min".format(RPM_R)+
                  "|"+"once_time:{:5.0f}ms".format(once_time),end='')
            Count_R=0
    else:
        Count_R=Count_R
        #return RPM_R

while True:
    
    Motor_control(100,0)
    
    Speed_measurement_R()
    #a=Speed_measurement_R()
    #print(a)
    