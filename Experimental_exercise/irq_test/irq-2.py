from machine import Pin
import time
import micropython

micropython.alloc_emergency_exception_buf(100)

p0 = Pin(0,Pin.IN,Pin.PULL_UP)
trig_locks = [0]
trig_timeticks_list = [0,0]
count = [0,0,0,0]

def p0_irq(pin):
    count[1] = count[1] + 1
    if pin.value()==0 and trig_locks[0]==0:
        count[2] = count[2] + 1
        trig_timeticks_list[0]=time.ticks_ms()
        trig_locks[0]=1
    elif pin.value()==1 and trig_locks[0]==1:
        count[3] = count[3] + 1
        trig_timeticks_list[1]=time.ticks_diff(time.ticks_ms(),trig_timeticks_list[0])
        trig_locks[0]=0
        if trig_timeticks_list[1] >= 20:
            count[0] = count[0] + 1

p0.irq(handler=p0_irq,trigger= Pin.IRQ_FALLING)

while True:
    #print("RAM used = {RAM_used}KB".format(RAM_used = gc.mem_alloc()/1024))
    print("\r",count,end="")
    time.sleep_ms(5)