#For the time being, this code only applies to microbit V1
#"PCA9685.py" must be loaded into the microbit before running
from microbit import i2c
import PCA9685
pca9685 = PCA9685.PCA9685(i2c)
pca9685.duty( 0, value=0, invert=False)
