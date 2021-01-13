#For the time being, this code only applies to microbit V1
#"PCA9685.py" must be loaded into the microbit before running
from microbit import i2c,display,Image,sleep,pin1,pin2,pin12,pin13,pin14
import utime
import PCA9685
pca9685 = PCA9685.PCA9685(i2c)
def Line_patrol_IR():
    global right_IR,left_IR #Declare global variables
    pin14.write_digital(1) #pin14 controls the infrared pair tube, high level conduction
    right_IR = pin1.read_digital() #Pin1 receives the analog value of the right infrared pair tube
    left_IR = pin2.read_digital() #Pin2 receives the analog value of the left infrared pair tube
    #print("R:" + str(right_IR), "L:" + str(left_IR)) #Serial port output left and right infrared pair tube voltage analog value
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
    t3 = utime.ticks_diff(t2,t1)/1000000
    #print("\r"+":{:5.2f}cm".format(t3*34300/2),end='')
    Distance=int(t3*34300/2)
def Line_patrol_control():
    #The following code implements the line patrol of Q-car
    if  Distance>10 and right_IR==1 and left_IR==1:
        pca9685.set_pwm(0, 0, 2047)
        pca9685.set_pwm(1, 0, 0)
        pca9685.set_pwm(2, 0, 0)
        pca9685.set_pwm(3, 0, 2047)
        display.show(Image.ARROW_N)
    elif Distance>10 and right_IR==1 and left_IR==0:
        pca9685.set_pwm(0, 0, 2047)
        pca9685.set_pwm(1, 0, 0)
        pca9685.set_pwm(2, 0, 0)
        pca9685.set_pwm(3, 0, 0)
        display.show(Image.ARROW_NE)
    elif Distance>10 and left_IR==1 and right_IR==0:
        pca9685.set_pwm(0, 0, 0)
        pca9685.set_pwm(1, 0, 0)
        pca9685.set_pwm(2, 0, 0)
        pca9685.set_pwm(3, 0, 2047)
        display.show(Image.ARROW_NW)
    elif Distance>10 and right_IR==0 and left_IR==0:
        pca9685.set_pwm(0, 0, 0)
        pca9685.set_pwm(1, 0, 2047)
        pca9685.set_pwm(2, 0, 0)
        pca9685.set_pwm(3, 0, 0)
        display.show(Image.ARROW_SE)
        sleep(300)
        pca9685.set_pwm(0, 0, 2047)
        pca9685.set_pwm(1, 0, 0)
        pca9685.set_pwm(2, 0, 0)
        pca9685.set_pwm(3, 0, 2047)
        display.show(Image.ARROW_N)
        sleep(300)
    if Distance<=10:
        pca9685.set_pwm(0, 0, 0)
        pca9685.set_pwm(1, 0, 0)
        pca9685.set_pwm(2, 0, 0)
        pca9685.set_pwm(3, 0, 0)
        display.show(Image.SAD)
        sleep(1000)
while True:
    Ultrasonic_ranging()
    Line_patrol_IR()
    Line_patrol_control()