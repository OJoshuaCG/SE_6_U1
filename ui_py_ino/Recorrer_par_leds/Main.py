import sys
import arduino as ard #Modulo personalizado
import serial as connector
from PyQt5 import uic, QtWidgets

qtCreatorFile = "Window.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals y Configuraciones Iniciales
        self.btn_conectar.clicked.connect(self.conectar)
        self.btn_accion.clicked.connect(self.accion)
        self.arduino = ard.c_arduino()
        self.btn_accion.setEnabled(False)

    # Área de los Slots
    def conectar(self):
        com = "COM"+self.txt_com.text()
        #print(com)
        # Inicializamos el arduino
        # Conexion a un puerto en LINUX /dev/tty
        # Enviar el COM que se ocupa en el dispositivo
        self.arduino.connect(com,self.btn_conectar)
        self.txt_com.setText("")
        if(self.arduino.verifyConnection()):
            # Si esta conectado...
            self.btn_accion.setEnabled(True)


    def accion(self):
        if self.arduino != None:
            print(self.btn_accion.text())
            if self.btn_accion.text() == "INICIAR":
                self.arduino.write("1")
                self.btn_accion.setText("PAUSAR")
            elif self.btn_accion.text() == "PAUSAR":
                self.arduino.write("0")
                self.btn_accion.setText("REUNADAR")
            elif self.btn_accion.text() == "REUNADAR":
                self.arduino.write("2")
                self.btn_accion.setText("PAUSAR")

        else:
            print("Aun no se ha realizado la conexion con arduino")


    def closeEvent(self, event):
        self.arduino.disconnect()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())