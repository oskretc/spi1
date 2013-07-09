import serial
import time
usbport = '/dev/ttyAMA0'
ser = serial.Serial(usbport, 9600, timeout=1)
data=[0x30,0x31]
strdata=''.join(chr(e) for e in data)
ser.write(strdata)
ser.timeout = 2
#time.sleep(2)

#while True:
#           response=ser.read()
#           time.sleep=2
#           print (" read data: python \n")
#           print (response)
  
ser.close()