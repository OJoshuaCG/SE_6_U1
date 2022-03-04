'''
Plantilla proxima para el archivo marduino.py
El cual servira para inicializar el arduino, conectar y desconectarlo al cerrar aplicacion.
'''

import sys
# Modulo/clase arduino
import marduino as mard 
from PyQt5 import uic, QtWidgets

qtCreatorFile = "Prog_5.ui" # Nombre del archivo .ui aqui.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals y Configuraciones Iniciales
        self.btn_conectar.clicked.connect(self.conectar)
        #self.btn_accion.clicked.connect(self.accion)
	 
        #Instanciamos un objeto de la clase marduino
        self.arduino = mard.c_arduino()


    def conectar(self):
        # Inicializamos el arduino
        # Conexion a un puerto en LINUX
        # Enviar el COM que se ocupa en el dispositivo
        self.arduino.connect("/dev/ttyACM0")

    def closeEvent(self, event):
        self.arduino.disconnect()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
