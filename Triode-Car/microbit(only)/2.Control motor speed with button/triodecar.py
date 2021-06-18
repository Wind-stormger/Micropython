from microbit import *
#定义类
class Triodecar:

#初始化方法
    def __init__(self):
        pass
    
#添加方法
    def direction_stop(self):
        pin14.write_digital(1)
        pin15.write_digital(1)
    
    def direction_foward(self):
        pin14.write_analog(512)
        pin15.write_analog(512)
    
    def direction_left(self):
        pin14.write_digital(1)
        pin15.write_analog(512)
    
    def direction_right(self):
        pin14.write_analog(512)
        pin15.write_digital(1)

    def left_motor_speed(self,value):
        if value>=0 and value<=10:
            pin14.write_analog(int(1023-1023/10*value))
        else:
            print('value range from 0 to 10')

    def right_motor_speed(self,value):
        if value>=0 and value<=10:
            pin15.write_analog(int(1023-1023/10*value))
        else:
            print('value range from 0 to 10')

    def left_LDR(self):
        return pin2.read_analog()
    
    def right_LDR(self):
        return pin1.read_analog()
