from machine import Pin
from neopixel import NeoPixel
import time

from machine import Pin
from neopixel import NeoPixel
import time

pin_18 = Pin(18, Pin.OUT)#将GPIO18作为WS2812的信号传输线
#pin_48 = Pin(48, Pin.OUT)
np = NeoPixel(pin_18, 25,bpp=3, timing=1)
#np = NeoPixel(pin_14, 25,bpp=3, timing=1)
# 在GPIO18上创建一个NeoPixel对象，设置数量25，bpp=3为RGB模式，4为RGBW模式，timing=1为800kHz，0为400kHz

def rainbow(num=1,level=25,delay=100):
    
    def write_all(num,delay,red,green,blue):
        for j in range (num):
            np[j] = (red,green,blue)
        np.write()
        time.sleep_ms(delay)
    
    red,green,blue = level,0,0
    
    rainbow_step_list2 = [(0,1,0),(-1,0,0),(0,0,1),(0,-1,0),(1,0,0),(0,0,-1)]
    
    for step in rainbow_step_list2:
        for i in range (level):
            red+=step[0]
            green+=step[1]
            blue+=step[2]
            write_all(num,delay,red,green,blue)
            #print(red,green,blue)

while True:
    rainbow(num=25,level=50,delay=1)
    #print("RAM used = {RAM_used}KB".format(RAM_used = gc.mem_alloc()/1024))
    #gc.collect()