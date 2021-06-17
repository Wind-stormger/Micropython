#用micro:bit的AB按钮控制triodecar电机
'''
一切与硬件交互直接相关的东西都存在于 microbit函数库中，
一般直接从中引用全部功能。
'''
from microbit import *

'''
使用def来创建自定义函数，将可能重复应用的某些功能的代码写入其中以便调用。
micro:bit的pin14引脚控制着triodecar的左电机，pin15引脚控制着右电机，
引脚输出高电平将使电机停转，低电平将使电机运行。
'''
def direction_stop():
    pin14.write_digital(1)
    pin15.write_digital(1)
def direction_foward():
    pin14.write_digital(0)
    pin15.write_digital(0)
'''右电机转，左电机停转，triodecar向左行驶。'''
def direction_left():
    pin14.write_digital(1)
    pin15.write_digital(0) 
'''右电机停转，左电机转，triodecar向右行驶。'''
def direction_right():
    pin14.write_digital(0)
    pin15.write_digital(1)
'''开始主循环，进入循环后如果不执行break语句将在系统关机前永远循环下去'''
while True:
    '''if条件判断，若满足条件则执行。
    当按钮A和按钮B都被按下时，显示北向箭头，控制triodecar向前行驶。'''
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.ARROW_N, delay=0, wait=True, loop=False, clear=False)
        direction_foward()
    '''elif表示“否则如果”，“不满足if的条件但满足这个条件”的意思。
    此处即为：若仅按钮A被按下，则显示西向箭头，控制triodecar向右行驶。'''
    elif button_a.is_pressed():
        display.show(Image.ARROW_W, delay=0, wait=True, loop=False, clear=False)
        direction_right()
    '''若仅按钮B被按下，则显示东向箭头，控制triodecar向左行驶。'''
    elif button_b.is_pressed():
        display.show(Image.ARROW_E, delay=0, wait=True, loop=False, clear=False)
        direction_left()
    '''else为if和elif都判定为否的情况下将执行。
    此处为：若按钮A或按钮B都没被按下，则显示困倦图标，控制triodecar停车。'''
    else:
        display.show(Image.ASLEEP, delay=0, wait=True, loop=False, clear=False)
        direction_stop()
