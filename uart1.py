import serial
import time
from decimal import *


usbport = '/dev/ttyAMA0'
ser = serial.Serial(usbport, 19200, timeout=1)
data=[0x00,0x00]
strdata=''.join(chr(e) for e in data)
ser.write(strdata)
ser.timeout = 0.1
response=ser.read(2)
time.sleep=0.1
data=[0x3D,0x33]
strdata=''.join(chr(e) for e in data)
ser.write(strdata)

#time.sleep(.002)


response=ser.read(2)
ser.close()
#time.sleep=2


for data in response:

    try:
        i = ord(str(data))
    except ValueError:
        i = 0
    print i

#print i
print (" read data: python \n")
print len(response)
#print int(response[0])+1





  
