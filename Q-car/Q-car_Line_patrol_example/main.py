import time
import pca9685
import microbit as m
from machine import I2C,Pin
#Assign initial value 0 to global variables
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
def Motor_control(Right_motor_control,Left_motor_control):
    if Right_motor_control == -1:
        pca9685.duty(0,value=0,invert=False)
        pca9685.duty(1,value=4095,invert=False)
    elif Right_motor_control == 0:
        pca9685.duty(0,value=0,invert=False)
        pca9685.duty(1,value=0,invert=False)
    elif Right_motor_control == 1:
        pca9685.duty(0,value=4095,invert=False)
        pca9685.duty(1,value=0,invert=False)
    else: 
        print("The value range in[-1,0,1]")
    if Left_motor_control == -1:
        pca9685.duty(2,value=4095,invert=False)
        pca9685.duty(3,value=0,invert=False)
    elif Left_motor_control == 0:
        pca9685.duty(2,value=0,invert=False)
        pca9685.duty(3,value=0,invert=False)
    elif Left_motor_control == 1:
        pca9685.duty(2,value=0,invert=False)
        pca9685.duty(3,value=4095,invert=False)
    else:
        print("The value range in[-1,0,1]")
def Line_patrol_control():
    #The following code implements the line patrol of Q-car
    if right_IR>200 and left_IR>200:
        Motor_control(1,1)
        m.display.show(m.Image.ARROW_N)
    elif right_IR>200 and left_IR<=200:
        Motor_control(1,0)
        m.display.show(m.Image.ARROW_NE)
    elif left_IR>200 and right_IR<=200:
        Motor_control(0,1)
        m.display.show(m.Image.ARROW_NW)
    elif right_IR<=200 and left_IR<=200:
        Motor_control(-1,0)
        m.display.show(m.Image.ARROW_SE)
        time.sleep_ms(300)
        Motor_control(1,1)
        m.display.show(m.Image.ARROW_N)
        time.sleep_ms(300)

while True:
    Line_patrol_IR()
    Line_patrol_control()