from machine import SoftSPI,Pin
from ssd1306 import SSD1306_SPI

spi = SoftSPI(baudrate=10000000,
              polarity=1,
              phase=0,
              sck=Pin(17,Pin.OUT),
              mosi=Pin(16,Pin.OUT),
              miso=Pin(10))#sck=D0, mosi=D1
oled = SSD1306_SPI(128, 64, spi, dc=Pin(14),res=Pin(15), cs=Pin(13))#dc=DC, res=RES, cs=CS&GND

def display():
    oled.text("Hello,I am wind.", 0,  32)    
    oled.show()

if __name__=="__main__":
    display()