from pynput.keyboard import Key, Controller
import serial as s
import time as t

nombrePuerto = "/dev/ttyACM0"   # Linux
#nombrePuerto = "COM2"          # Windows
arduino = s.Serial(nombrePuerto, baudrate=9600, timeout=1)
teclado = Controller()


while True:
    val = arduino.readline().decode()
    val = val.replace("\n", "")
    val = val.replace("\r", "")
    print(val)
    
    if val=='1':
        teclado.press('A')
        teclado.release('A')
    else:
        pass
    
    t.sleep(.1)
    # Son segundos



