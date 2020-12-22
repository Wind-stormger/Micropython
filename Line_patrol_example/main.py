import time
import pca9685
import microbit as m
from machine import I2C,Pin

Duty_cycle_R = 0 #Assign initial value 0 to global variables
Duty_cycle_L = 0
right_IR = 0
left_IR = 0

i2c=I2C(sda=Pin(21),scl=Pin(22),freq=10000) #I2C initialization
pca9685 = pca9685.PCA9685(i2c,address=0x40) #Reference to pca9685 object,I2C address of pca9685
pca9685.freq(freq=50) #Set the frequency of pca9685
def Line_patrol_IR():
    global right_IR,left_IR #Declare global variables
    m.pin14.write_digital(1) #pin14 controls the infrared pair tube, high level conduction
    right_IR = m.pin1.read_analog() #Pin1 receives the analog value of the right infrared pair tube
    left_IR = m.pin2.read_analog() #Pin2 receives the analog value of the left infrared pair tube
    print("R:" + str(right_IR), "L:" + str(left_IR)) #Serial port output left and right infrared pair tube voltage analog value
def PWM_motor():
    global Duty_cycle_R,Duty_cycle_L #Declare global variables
    #The PWM duty cycle of the left and right motors ranges from - 100 to 100
    #> 0 forward rotation
    #= 0 stall
    #< 0 reverse rotation
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

    