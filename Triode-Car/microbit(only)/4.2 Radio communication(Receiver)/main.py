# 无线电接收端
import triodecar
import radio
from microbit import *

# 创建对象
triodecar = triodecar.Triodecar()
# 启用无线电模块
# 使用无线电将增加功耗并占用大量内存，需要斟酌代码容量，保证设备供电
radio.on()
incoming = 0

while True: 
    incoming = radio.receive()
    print(incoming)
    if incoming == "left":
        triodecar.direction_left()
    elif incoming == "right":
        triodecar.direction_right()
    elif incoming == "stop":
        triodecar.direction_stop()
    else:
        triodecar.direction_stop()
    sleep(100)
