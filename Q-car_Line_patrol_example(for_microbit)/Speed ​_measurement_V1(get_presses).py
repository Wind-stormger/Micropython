#For the time being, this code only applies to microbit V1
#"PCA9685.py" must be loaded into the microbit before running
from microbit import sleep,pin14,button_a,button_b
def Speed_measurement():
    pin14.write_digital(1)
    sleep(5000)
    IR_R=button_a.get_presses()
    IR_L=button_b.get_presses()
    RPM_R=IR_R
    RPM_L=IR_L
    print("\r"+"RPM_R:{:3.0f}r/min".format(RPM_R),
          "RPM_L:{:3.0f}r/min".format(RPM_L),end='')
while True:
    Speed_measurement()
