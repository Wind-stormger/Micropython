from microbit import *

def direction_stop():
    pin14.write_digital(1)
    pin15.write_digital(1)
    
def direction_foward():
    pin14.write_analog(512)
    pin15.write_analog(512)
    
def direction_left():
    pin14.write_digital(1)
    pin15.write_analog(512)
    
def direction_right():
    pin14.write_analog(512)
    pin15.write_digital(1)
