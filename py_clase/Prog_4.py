import serial as connector
import time

arduino = connector.Serial("COM2", baudrate=9600, timeout=1)

while(True):
    arduino.write('3'.encode())
    time.sleep(1)

'''
arduino.write("1".encode())

arduino.close()
'''
