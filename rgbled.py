#connct to pin 1 and 2 and 3
from picozero import RGBLED
from time import sleep

rgb = RGBLED(red = 1, green = 2, blue = 3)
rgb.color = (0,220,250)
    
