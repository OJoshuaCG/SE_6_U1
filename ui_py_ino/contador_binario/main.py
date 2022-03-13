import sys
# Modulo/clase arduino
import arduino as ard 
from PyQt5 import uic, QtWidgets#, QtCore

qtCreatorFile = "contador.ui" # Nombre del archivo .ui aqui O ruta.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals y Configuraciones Iniciales
        self.btn_conectar.clicked.connect(self.conectar)
        self.btn_contador.clicked.connect(self.enviarContador)
	 
        #Instanciamos un objeto de la clase aarduino
        self.arduino = ard.c_arduino()        

   
    def conectar(self):
        com = self.txt_com.text()
        #print(com)
        # Inicializamos el arduino
        # Conexion a un puerto en LINUX /dev/tty
        # Enviar el COM que se ocupa en el dispositivo
        self.arduino.connect(com, self.btn_conectar)
        self.txt_com.setText("")
        if(self.arduino.verifyConnection()):
            # Si esta conectado...            
            self.txt_numero.setEnabled(True)
            self.btn_contador.setEnabled(True)


    def enviarContador(self):
        contador = self.txt_numero.text()
        if(not(contador.isdigit())):
            self.windowMSG("Dato invalido", "Ingrese un numero")
            self.txt_numero.setText("")
            return
        
        contador = int(contador)
        if(not(0 < contador and contador <= 255)):
            self.windowMSG("Num invalido", "0 < numero <= 255")
            self.txt_numero.setText("")
            return

        self.arduino.write(str(contador))
            

    def closeEvent(self, event):
        self.arduino.disconnect()


    def windowMSG(self, encabezado, texto):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle(encabezado)
        msgbox.setText(texto)        
        msgbox.exec_()  

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
