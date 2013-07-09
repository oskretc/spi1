import RPi.GPIO as GPIO 
import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=(10000000)
spi.mode=1
spi.cshigh=False
print spi.max_speed_hz
print spi.mode
print spi.cshigh
print spi.lsbfirst
print spi.bits_per_word

#spi.writebytes([0x40,0x00,0xA4])     # All as 
#spi.writebytes([0x40,0x01,0xA5])     # All as 
#print spi.xfer([0x41,0x00,0x00])
#print spi.xfer([0x41,0x01,0x00])
print "Setting Bank=1"
spi.writebytes([0x40,0x0A,0x80])     # bank=1
print "port A"
spi.writebytes([0x40,0x00,0xA4])
print spi.xfer([0x41,0x00,0x00])
print "port B"
print spi.xfer([0x41,0x10,0x00])
print "writing to A.0"
for x in range(1,10):
    spi.writebytes([0x40,0x09,0x01])
    spi.writebytes([0x40,0x0A,0x01])
    spi.writebytes([0x40,0x09,0x00])
    spi.writebytes([0x40,0x0A,0x00])

#spi.writebytes([0x40,0x01,0x01])
#time.sleep(1)
#spi.writebytes([1,255,254]) # turn all lights on
#time.sleep(1)
    
    
print spi.close()
