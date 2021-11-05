from machine import Pin
from neopixel import NeoPixel
import time


pin_18 = Pin(18, Pin.OUT)# set GPIO18 to output to drive NeoPixels
#pin_48 = Pin(48, Pin.OUT)# for ESP32S3-DevKit-1 GPIO48
np = NeoPixel(pin_18, 1,bpp=3, timing=1)# create NeoPixel driver on GPIO18 for 1 pixels
red,green,blue=25,0,0
np[0] = (red,green,blue) # set the first pixel
np.write()# write data to all pixels

while True:
#rainbow cycle display
    for green in range (1,26):
        np[0] = (red,green,blue)
        np.write()
        time.sleep_ms(200)

    for red in range (24,-1,-1):
        np[0] = (red,green,blue)
        np.write()
        time.sleep_ms(200)

    for blue in range (1,26):
        np[0] = (red,green,blue)
        np.write()
        time.sleep_ms(200)

    for green in range (24,-1,-1):
        np[0] = (red,green,blue)
        np.write()
        time.sleep_ms(200)

    for red in range (1,26):
        np[0] = (red,green,blue)
        np.write()
        time.sleep_ms(200)

    for blue in range (24,-1,-1):
        np[0] = (red,green,blue)
        np.write()
        time.sleep_ms(200)

