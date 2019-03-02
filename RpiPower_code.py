import time
import urllib as url
import serial

ArduinoSerial=serial.Serial("/dev/ttyACM0",115200)
time.sleep(2)

while True:
  s=ArduinoSerial.readline()
  print s
  temp=url.urlopen("https://api.thingspeak.com/update?api_key=3JI4R908LM4LUFJC&field1="+str(s))
  time.sleep(15)
