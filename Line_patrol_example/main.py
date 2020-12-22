import time
import pca9685
import microbit as m
from machine import I2C,Pin
Duty_cycle_R = 0
Duty_cycle_L = 0
right_IR = 0
left_IR = 0
i2c=I2C(sda=Pin(21),scl=Pin(22),freq=10000)
pca9685 = pca9685.PCA9685(i2c,address=0x40)
pca9685.freq(freq=50)
def Line_patrol_IR():
    global right_IR,left_IR
    m.pin14.write_digital(1)
    right_IR = m.pin1.read_analog()
    left_IR = m.pin2.read_analog()             
    print("R:" + str(right_IR), "L:" + str(left_IR))
def PWM_motor():
    global Duty_cycle_R,Duty_cycle_L
    print(Duty_cycle_R,Duty_cycle_L)    
    pca9685.duty(0,value=int(2047-2047/100*Duty_cycle_R),invert=False)
    pca9685.duty(1,value=int(2048+2047/100*Duty_cycle_R),invert=False)
    pca9685.duty(2,value=int(2048+2047/100*Duty_cycle_L),invert=False)
    pca9685.duty(3,value=int(2047-2047/100*Duty_cycle_L),invert=False)
def PWM_control():
    global Duty_cycle_R,Duty_cycle_L
    if right_IR>200 and left_IR>200:
        Duty_cycle_R = 80
        Duty_cycle_L = 80
        PWM_motor()
    elif right_IR>200 and left_IR<=200:
        Duty_cycle_R = 80
        Duty_cycle_L = 0
        PWM_motor()
    elif left_IR>200 and right_IR<=200:
        Duty_cycle_R = 0
        Duty_cycle_L = 80
        PWM_motor()
    
    elif right_IR<=200 and left_IR<=200:
        Duty_cycle_R = -80
        Duty_cycle_L = 0
        PWM_motor()
        time.sleep_ms(200)
        Duty_cycle_R = 0
        Duty_cycle_L = 80
        PWM_motor()
        time.sleep_ms(200)

while True:
    Line_patrol_IR()
    PWM_control()

    