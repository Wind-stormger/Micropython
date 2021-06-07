import triodecar
from microbit import *

#创建对象
triodecar = triodecar.Triodecar()

while True:
    # 用format格式化输出检测到的左右两光敏电阻的电压模拟值
    print("{0}|{1}".format(triodecar.left_LDR(),triodecar.right_LDR()) )
    sleep(250)