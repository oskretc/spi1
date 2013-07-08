import RPi.GPIO as GPIO 
from time import sleep
 
LED_PIN = 25
 
print "Setting up GPIO" 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(LED_PIN,GPIO.OUT) 
 
def enable_led(should_enable):
    if should_enable:
        GPIO.output(LED_PIN, False)
    else:
        GPIO.output(LED_PIN, True)
        
        
for x in range (1,10000):
    enable_led(True) 
    enable_led(False)

# enable_led(False) 
# print "LED is OFF" 
# sleep(.1) 
# enable_led(True) 
# print "LED is ON" 
# sleep(.1) 
# enable_led(False) 
# print "LED is OFF" 
# sleep(.1) 
# enable_led(True) 
# print "LED is ONNN" 
# sleep(.1) 
GPIO.cleanup()
