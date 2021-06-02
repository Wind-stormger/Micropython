import triodecar
from microbit import *
triodecar.direction_stop()
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        triodecar.direction_foward()
    if button_a.is_pressed():
        triodecar.direction_right()
    if button_b.is_pressed():
        triodecar.direction_left()
