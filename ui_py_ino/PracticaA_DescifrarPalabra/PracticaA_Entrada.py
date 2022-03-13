# ------------ LIBRERÍAS ------------
import serial as connector
import sys
import time
from PyQt5 import uic, QtWidgets

# ------------ CÓDIGO ------------
qtCreatorFile = "PracticaA_Interfaz.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_conectar.clicked.connect(self.conectar)
        self.btn_enviar.clicked.connect(self.enviar)
        self.pg_progreso.setMinimum(0)
        self.pg_progreso.setMaximum(100)

        # Área de las variables
        self.arduino = None

    # Área de los Slots
    def conectar(self):
        if self.arduino == None:
            com = 'COM' + self.le_com.text()
            self.le_com.setDisabled(True)

            self.arduino = connector.Serial(com, baudrate=9600, timeout=10)

            print('Conexión Inicializada')
            self.btn_conectar.setText('DESCONECTAR')
        elif self.arduino.isOpen():
            print('Conexión Terminada')
            self.btn_conectar.setText('RECONECTAR')
            self.arduino.close()
        else:
            print('Conexión Restablecida')
            self.btn_conectar.setText('DESCONECTAR')
            self.arduino.open()

    def enviar(self):
        if self.arduino != None:
            if self.arduino.isOpen():
                self.le_palabra.setDisabled(True)
                palabra = self.le_palabra.text()
                avance = 0
                for i in range(len(palabra)):
                    self.arduino.write(str(ord(palabra[i])).encode())
                    avance = avance + (100 / len(palabra))
                    # print(ord(palabra[i]))
                    self.pg_progreso.setValue(int(avance))
                    time.sleep(5)

                    self.arduino.write('0'.encode())

                    time.sleep(2)
                else:
                    self.le_palabra.setDisabled(False)

                print('El dato ha sido enviado correctamente')
            else:
                print('La conexión está cerrada actualmente')
        else:
            print('Aún no se ha realizado la conexión con Arduino')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())