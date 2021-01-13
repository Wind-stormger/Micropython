import time
import pca9685
import microbit as m
from machine import I2C,Pin
i2c=I2C(sda=Pin(21),scl=Pin(22),freq=10000) #I2C initialization
pca9685 = pca9685.PCA9685(i2c,address=0x40) #Reference to pca9685 object,I2C address of pca9685
pca9685.reset()
pca9685.freq(freq=50)
pca9685.pwm(0, on=0, off=0)
pca9685.pwm(1, on=0, off=0)
pca9685.pwm(2, on=0, off=0)
pca9685.pwm(3, on=0, off=0)