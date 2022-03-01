import sys
# Modulo/clase arduino
import marduino as mard 
from PyQt5 import uic, QtWidgets

qtCreatorFile = "ui_py_ino/ej_p05_suma/ui_suma.ui" # Nombre del archivo .ui aqui.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals y Configuraciones Iniciales
        self.btn_conectar.clicked.connect(self.conectar)
        self.btn_enviar.clicked.connect(self.enviar)        

        #self.btn_accion.clicked.connect(self.accion)
	 
        #Instanciamos un objeto de la clase marduino
        self.arduino = mard.c_arduino()
        self.port = "/dev/ttyS0"


    def conectar(self):
        # Inicializamos el arduino
        # Conexion a un puerto en LINUX
        # Enviar el COM que se ocupa en el dispositivo
        self.arduino.connect(self.port)        

    def enviar(self):
        if not(self.arduino.verifyConnection()):
            #print('Aun no se ha realizado la conexion')
            self.msgWindow("Advertencia", "Aun no se ha realizado la conexion")
            return
        
        a = self.txt_1.text()
        b = self.txt_2.text()
        if not(a.isdigit() and b.isdigit()):
            #print('Ingrese numeros')            
            self.msgWindow("Advertencia", "Ingrese SOLO numeros")
            return

        a, b = int(a), int(b)
        res = a + b
        self.arduino.write(res)
               

    def closeEvent(self, event):
        self.arduino.disconnect()


    def msgWindow(self, title, mensaje):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle(title)
        msgbox.setText(mensaje)        
        msgbox.exec_()        



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())