import serial as connector

arduino = connector.Serial("COM2", baudrate=9600, timeout=1)

valor = arduino.readline()
valor = valor.decode()

print(valor)
