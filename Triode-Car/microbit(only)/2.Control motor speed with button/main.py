import triodecar
from microbit import *

#创建对象
triodecar = triodecar.Triodecar()
# 通过“对象.方法”调用方法
triodecar.direction_stop()
#创建一个整数变量并设置初始值为0
speed = 0

while True:
    
    while button_a.was_pressed():
        speed += 1
        break
    
    while button_b.was_pressed():
        speed -= 1
        break
    #当变量speed值小于0或大于10时将值设为0
    while speed < 0 or speed > 10:
        speed = 0
        break
    #变量speed值同时控制左右电机的转速
    triodecar.left_motor_speed(speed)
    triodecar.right_motor_speed(speed)
    display.show(speed, delay=500, wait=True, loop=False, clear=False)