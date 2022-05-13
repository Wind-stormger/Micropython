from machine import Pin
import utime
import micropython

micropython.alloc_emergency_exception_buf(100)
d0 = Pin(0,Pin.IN) 
d16 = Pin(16, Pin.OUT)

count = 0
lev = 1
ms = 0
speed = 0

list1 = [count,lev,ms,speed]

def return_value(count,d0,lev,ms,speed):
    return count,d0,lev,ms,speed


def callback(p):
    count = list1[0]
    lev = list1[1]
    ms = list1[2]
    speed = list1[3]
    
    count = count+1
    list1[0] = count
    if lev == 1:
        ms = utime.ticks_us()
        list1[2] = ms
        d0.irq(trigger=Pin.IRQ_FALLING , handler=callback)
        lev = 0
        list1[1] = lev
    else:
        speed = utime.ticks_us()-ms
        list1[3] = speed
        d0.irq(trigger=Pin.IRQ_RISING , handler=callback)
        lev = 1
        list1[1] = lev

d16.value(0)
d0.irq(handler=callback,trigger=Pin.IRQ_RISING)
trig_count = 0
while(True):
    count = list1[0]
    lev = list1[1]
    ms = list1[2]
    speed = list1[3]
    d16.value(0)
    utime.sleep_ms(10)
    d16.value(1)
    utime.sleep_ms(10)
    trig_count = trig_count+1
    print('count:%d,trig_count:%d, speed:%d'%(count, trig_count, speed))
