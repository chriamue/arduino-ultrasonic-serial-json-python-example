import serial
import io
import json
import time

ser = serial.Serial('/dev/ttyACM0', 9600)
sendStr = json.dumps({'led': True, 'beep': True}, separators=(',',':'))
time.sleep(3)
ser.write(sendStr + "\n")
ser.write(sendStr + "\n")
ser.flushInput()
while True:
    readStr = ser.readline()
    print(readStr)
    readJson = json.loads(readStr)
    print(readJson)
    if readJson['range'] < 25:
        sendStr = json.dumps({'led': True, 'beep': True}, separators=(',',':'))
        ser.write(sendStr + "\n")