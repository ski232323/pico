#This code allows to glow a led that is connected to pin1 and to pin 3 GND
from machine import Pin
from time import sleep
led1 = Pin(1, Pin.OUT)
led1.toggle()



