import triodecar
from microbit import *

#创建对象
triodecar = triodecar.Triodecar()
# 通过“对象.方法”调用方法
triodecar.direction_stop()
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.ARROW_N, delay=0, wait=True, loop=False, clear=False)
        triodecar.direction_foward()
        sleep(100)
    if button_a.is_pressed():
        display.show(Image.ARROW_W, delay=0, wait=True, loop=False, clear=False)
        triodecar.direction_right()
    if button_b.is_pressed():
        display.show(Image.ARROW_E, delay=0, wait=True, loop=False, clear=False)
        triodecar.direction_left()

        