from microbit import *
'''
设计一个控制电机转速的函数。
创建的函数可以添加参数（自变量）。
调用函数时输入自变量即可如同套用一个公式一样使用函数。
write_analog()取值范围为0-1023，将控制microbit对应引脚输出1024级占空比的PWM。
若我们设计将电机转速等分为10级，则应该将1023分10等份再乘以函数自变量。
占空比越大，转速越慢，占空比越低，转速越快。
若设计转速从0-10逐级增大，则应1023-1023-1023/10*value。
int()将使其数值取整。
'''
def left_motor_speed(value):
    if value>=0 and value<=10:
        pin14.write_analog(int(1023-1023/10*value))
    else:
        print('Values range from 0 to 10')
def right_motor_speed(value):
    if value>=0 and value<=10:
        pin15.write_analog(int(1023-1023/10*value))
    else:
        print('Values range from 0 to 10')
        
'''创建一个变量并设置初始值为0'''
speed = 0

while True:
    '''执行到break即退出循环，此处用类似于if
    当按钮A被按下过一次，speed变量加1'''
    while button_a.was_pressed():
        speed += 1
        break
    '''当按钮B被按下过一次，speed变量减1'''
    while button_b.was_pressed():
        speed -= 1
        break
    '''当变量speed值小于0或大于10时将值设为0'''
    while speed < 0 or speed > 10:
        speed = 0
        break
    '''变量speed值同时控制左右电机的转速'''
    left_motor_speed(speed)
    right_motor_speed(speed)
    '''显示speed值'''
    display.show(speed, delay=500, wait=True, loop=False, clear=False)
    