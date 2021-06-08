# 接收端
import triodecar
import radio
from microbit import *

# 创建对象
triodecar = triodecar.Triodecar()
# 打开无线电
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
