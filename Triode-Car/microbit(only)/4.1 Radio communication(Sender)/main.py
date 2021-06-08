# 发送端
import triodecar
import radio
from microbit import *

# 创建对象
triodecar = triodecar.Triodecar()
# 启用无线电模块
# 使用无线电将增加功耗并占用大量内存，需要斟酌代码容量，保证设备供电
radio.on()
message = 0

while True:
    if button_a.is_pressed():
        message = "left"
    elif button_b.is_pressed():
        message = "right"
    else:
        message = "stop"
    radio.send(message)
    sleep(100)
