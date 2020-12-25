import time
import pca9685
import microbit as m
from machine import I2C,Pin
Duty_cycle_R = 0 
Duty_cycle_L = 0

Count_R=0
IR_R=0

i2c=I2C(sda=Pin(21),scl=Pin(22),freq=10000) #I2C initialization
pca9685 = pca9685.PCA9685(i2c,address=0x40) #Reference to pca9685 object,I2C address of pca9685
pca9685.freq(freq=50)

def PWM_motor():
    global Duty_cycle_R,Duty_cycle_L #Declare global variables
    #The PWM duty cycle of the left and right motors ranges from - 100 to 100
    #> 0 forward rotation
    #= 0 stall
    #< 0 reverse rotation
    #The duty function is called from the pca9685 library to realize the control of the PWM output on the specified pin on pca9685
    #duty(index, value=None, invert=False)
    #"index" specifies the pin number of pca9685
    #The range of "value" is 0-4095, this means that the PWM duty cycle of pin output is 0-100%
    #When "invert" is "True", the control effect on PWM duty cycle will be reversed to 100%-0%
    pca9685.duty(0,value=int(2047-2047/100*Duty_cycle_R),invert=False)
    pca9685.duty(1,value=int(2048+2047/100*Duty_cycle_R),invert=False)
    pca9685.duty(2,value=int(2048+2047/100*Duty_cycle_L),invert=False)
    pca9685.duty(3,value=int(2047-2047/100*Duty_cycle_L),invert=False)
     
def Speed_measurement():
    global IR_R,Count_R
    m.pin14.write_digital(1)
    IR_R=m.pin5.read_digital()
    IR_L=m.pin11.read_digital()
    if IR_R==0:
        t1=time.ticks_us()
        IR_R=m.pin5.read_digital()
        print("hello1")
        if IR_R==1:
            Count_R=Count_R+1
            print("hello2")
            print(time.ticks_us()-t1)
    print("Count_R:" + str(Count_R))
    time.sleep_ms(10)
    #print("R:" + str(m.pin5.read_digital()), "L:" + str(m.pin11.read_digital()))
while True:
    Duty_cycle_R = 80 
    Duty_cycle_L = 80
    #PWM_motor()
    
    Speed_measurement()
    