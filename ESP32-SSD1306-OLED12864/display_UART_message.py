from machine import SoftI2C,UART,Pin
import ssd1306 #引入ssd1306模块，ssd1306.py
import re
i2c = SoftI2C(sda=Pin(15), scl=Pin(16))
#设置I2C的SDA与SCL所在的引脚

oled = ssd1306.SSD1306_I2C(128, 64,i2c,addr=0x3c)
#创建一个ssd1306.SSD1306_I2C类的对象，初始化并设置屏幕像素，i2c引脚,i2c地址

uart1 = UART(1, tx=17, rx=18)
#选择UART接口，指定TX与RX使用的引脚

uart1.init(115200, bits=8, parity=None, stop=1)
#初始化，设置波特率，设置字符位数，设置奇偶校验，设置停止位

while True:
    uart1.any()#检索是否收到信息，否则返回0，是则返回信息
    if not uart1.any()==0:
        oled.fill(0)
        read = uart1.read()
        print(read)
        only_text=re.sub('\r'+'\n',' ', read)
        oled.text(only_text, 0,  32)
        #设置在屏幕中将要显示的文字内容，设置起始像素点坐标
        oled.show()
        #将内容输出到oled屏幕上

