from machine import SoftI2C,Pin
from ssd1306 import SSD1306_I2C

class OLED_Show:
    def __init__(self, sda_pin=15, scl_pin=16):        
        self.i2c = SoftI2C(sda=Pin(sda_pin), scl=Pin(scl_pin))
        self.oled = SSD1306_I2C(128, 64, self.i2c, addr=0x3c)
        self.init_display()

    def init_display(self):
        self.oled.text("Hello,I am wind.", 0,  32)    
        self.oled.show()
        
def main():
    oled_show = OLED_Show()

if __name__=="__main__":
    main()