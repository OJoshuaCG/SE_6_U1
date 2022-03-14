import sys
from turtle import down
# Modulo/clase arduino
import arduino as ard 
import time
from PyQt5 import uic, QtWidgets, QtCore
from pynput.keyboard import Key, Controller

qtCreatorFile = "line_edit.ui" # Nombre del archivo .ui aqui O ruta.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals y Configuraciones Iniciales
        self.btn_conectar.clicked.connect(self.conectar)
        #self.btn_accion.clicked.connect(self.accion)
	 
        #Instanciamos un objeto de la clase aarduino
        self.arduino = ard.c_arduino()

        self.timer = QtCore.QTimer()
        self.timer2 = QtCore.QTimer()

        self.timer.timeout.connect(self.execTimer)
        self.timer2.timeout.connect(self.execTimer2)

        self.teclado = Controller()
        self.ms = 0
        self.btn = [Key.left,Key.up,Key.down,Key.right,Key.space,Key.enter]
        self.lastBtn = 0


   
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
            self.le_texto.setEnabled(True)
            #self.le_texto.setFocus()    
            
            self.beginRead()


    def beginRead(self):
        if self.arduino == None:
            # Inicializar Conexion con Arduino
            self.conectar()
            print("Arduino Conectado")

        if not self.timer.isActive():
            self.timer.start(10)
        else:
            self.timer.stop()

    # Timer para el Python
    def execTimer(self):
        if self.arduino.inWaiting():
            lectura = self.arduino.read()
            lectura = lectura.replace("\n", "")
            lectura = lectura.replace("\r", "")
            if lectura != "":
                self.keystrokes(int(lectura))
            #print(lectura)
   
    def execTimer2(self):
        self.ms+=1

    def keystrokes(self,data = 0):
        print(data)
        
        if self.timer2.isActive() == False:
            self.timer2.start(1)
            self.lastBtn = data
            self.teclado.press(self.btn[data])
        
        if(self.ms>=5):
            self.teclado.release(self.btn[self.lastBtn])
            self.timer2.stop()
            self.ms = 0
        

    def closeEvent(self, event):
        self.arduino.disconnect()
        if self.timer.isActive():
            self.timer.stop()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
