from machine import Pin, Timer

led=Pin(1,Pin.OUT) # # broche en sortie

note=440 # La

timer=Timer() # déclare un objet timer

def loop(timer): # fonction exécutée en boucle
    led.toggle()

timer.init(freq=note/2, callback=loop)