from machine import Pin, UART
uart1 = UART(1, baudrate=115200, tx=17, rx=18)
#uart1.init(115200, bits=8, parity=None, stop=1)

def test():
    import time
    for i in range(50):
        time.sleep(0.1)
        uart1.write('hello world!')
        print(uart1.read(uart1.any()))
import os
os.dupterm(uart1)
print(os)