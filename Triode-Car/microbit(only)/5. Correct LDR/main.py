import triodecar
import math
from microbit import *

# 创建对象
triodecar = triodecar.Triodecar()

D_value = 0

# 显示东向箭头，调整可调电阻使左光敏电阻的电压模拟值到450~550的范围内后显示正确图标
while True:
    display.show(Image.ARROW_E, delay=0, wait=True, loop=False, clear=False)
    sleep(100)
    print(triodecar.left_LDR())
    if triodecar.left_LDR() >= 450 and triodecar.left_LDR() <= 550 :
        display.show(Image.YES, delay=0, wait=True, loop=False, clear=False)
        sleep(1000)
        print(triodecar.left_LDR())
        if triodecar.left_LDR() >= 450 and triodecar.left_LDR() <= 550 :
            break
# 显示西向箭头，调整可调电阻使右光敏电阻的电压模拟值到450~550的范围内后显示正确图标
while True:
    display.show(Image.ARROW_W, delay=0, wait=True, loop=False, clear=False)
    sleep(100)
    print(triodecar.right_LDR())
    if triodecar.right_LDR() >= 450 and triodecar.right_LDR() <= 550 :
        display.show(Image.YES, delay=0, wait=True, loop=False, clear=False)
        sleep(1000)
        print(triodecar.right_LDR())
        if triodecar.right_LDR() >= 450 and triodecar.right_LDR() <= 550 :
            break
# 计算左右光敏电阻的电压模拟值的差值的绝对值，取其十位数显示，调整可调电阻到差值的绝对值小于等于10时显示一个开心的笑脸
while True:
    D_value = int(math.fabs(triodecar.left_LDR() - triodecar.right_LDR()))
    display.show(D_value//10, delay=0, wait=True, loop=False, clear=False)
    sleep(100)#microbit V1 添加此段延时会死机
    print(D_value)
    if D_value <= 10:
        display.show(Image.YES, delay=0, wait=True, loop=False, clear=False)
        sleep(1000)
        D_value = int(math.fabs(triodecar.left_LDR() - triodecar.right_LDR()))
        print(D_value)
        if D_value <= 10:
            display.show(D_value//10, delay=0, wait=True, loop=False, clear=False)
            sleep(1000)
            display.show(Image.HAPPY, delay=0, wait=True, loop=False, clear=False)
            break