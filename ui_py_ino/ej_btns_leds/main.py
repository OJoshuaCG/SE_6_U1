import sys
# Modulo/clase arduino
import arduino as ard 
import time
from PyQt5 import uic, QtWidgets
from pynput.keyboard import Key, Controller

qtCreatorFile = "line_edit.ui" # Nombre del archivo .ui aqui.

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
        self.arduino = ard.c_arduino()
        

   
    def conectar(self):
        com = self.txt_com.text()
        print(com)
        # Inicializamos el arduino
        # Conexion a un puerto en LINUX /dev/tty
        # Enviar el COM que se ocupa en el dispositivo
        self.arduino.connect(com)
        self.txt_com.setText("")
        if(self.arduino.verifyConnection()):
            # Si esta conectado...            
            self.le_texto.setEnabled(True)
            self.le_texto.setFocus()            
            self.readButton()

            
    def readButton(self):
        #val = val.replace("\n", "")
        teclado = Controller()
        for i in range(5):
            teclado.press('A')
            teclado.release('A')


        # while True:
        #     dataReaded = self.arduino.read()
        #     time.sleep(1)
        

    def closeEvent(self, event):
        self.arduino.disconnect()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
