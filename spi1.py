import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=(1000000)
spi.mode=1


spi.writebytes([0x33,0x55,0x22])     # turn all lights off
#time.sleep(1)
#spi.writebytes([1,255,254]) # turn all lights on
#time.sleep(1)
    
    
print spi.close()