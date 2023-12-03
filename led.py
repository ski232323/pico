#This code permirts to glow a led that is connected to pin1
from machine import Pin
from time import sleep
led1 = Pin(1, Pin.OUT)

led1.on()

