# 发送端
import triodecar
import radio
from microbit import *

# 创建对象
triodecar = triodecar.Triodecar()
# 打开无线电
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

