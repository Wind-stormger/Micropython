from machine import Pin, ADC, I2C, SoftSPI,PWM
from time import sleep_ms
import machine
import gc
import random
from st7789 import ST7789,color565
from time import sleep_ms

spi = SoftSPI(baudrate=10000000, polarity=1, phase=0, sck=Pin(10,Pin.OUT), mosi=Pin(11,Pin.OUT), miso=Pin(8))#sck=D0, mosi=D1

display=ST7789(spi,
        reset=Pin(12, Pin.OUT),
        dc=Pin(13, Pin.OUT),
        cs=Pin(9, Pin.OUT),
        backlight=Pin(14, Pin.OUT),
        rotation=0 )

display.fill(0)
display.rect(0,0,240,280,color565(255,0,0))
#display.text( "ABCD", 50, 50, color=(255,255,255), background=(0,0,0))

