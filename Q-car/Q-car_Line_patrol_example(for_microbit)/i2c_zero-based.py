from microbit import sleep, i2c
import PCA9685
pca9685 = PCA9685.PCA9685(i2c)
pca9685.set_pwm_freq(freq_hz=50)