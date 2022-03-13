
# ------------ LIBRERÍAS ------------
import serial as connector
import sys
from PyQt5 import uic, QtWidgets

# ------------ CÓDIGO ------------
qtCreatorFile = "PrefUsuarioInterfaz.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de las variables
        self.arduino = None
        archivo = open('PrefUsuarioDatos.txt')
        contenidoArchivo = archivo.readlines()
        archivoProcesado = [i.split(',') for i in contenidoArchivo]
        instancia = [list(map(int, i)) for i in archivoProcesado]

        # Área de los Signals
        self.btn_conectar.clicked.connect(self.conectar)
        self.btn_limpiar.clicked.connect(self.limpiar)
        self.btn_pref01.clicked.connect(lambda: self.enviar(0, instancia))
        self.btn_pref02.clicked.connect(lambda: self.enviar(1, instancia))
        self.btn_pref03.clicked.connect(lambda: self.enviar(2, instancia))
        self.btn_pref04.clicked.connect(lambda: self.enviar(3, instancia))
        self.btn_pref05.clicked.connect(lambda: self.enviar(4, instancia))
        self.btn_pref06.clicked.connect(lambda: self.enviar(5, instancia))
        self.btn_pref07.clicked.connect(lambda: self.enviar(6, instancia))
        self.btn_pref08.clicked.connect(lambda: self.enviar(7, instancia))
        self.btn_pref09.clicked.connect(lambda: self.enviar(8, instancia))
        self.btn_pref10.clicked.connect(lambda: self.enviar(9, instancia))

    # Área de los Slots
    def conectar(self):
        if self.arduino == None:
            com = 'COM' + self.le_com.text()
            self.le_com.setDisabled(True)
            self.arduino = connector.Serial(com, baudrate=9600, timeout=1)
            print('Conexión Inicializada')
            self.btn_conectar.setText('DESCONECTAR')
        elif self.arduino.isOpen():
            print('Conexión Terminada')
            self.btn_conectar.setText('RECONECTAR')
            self.arduino.write('2'.encode())
            self.arduino.close()
        else:
            print('Conexión Restablecida')
            self.btn_conectar.setText('DESCONECTAR')
            self.arduino.open()

    def enviar(self, idbutton, vectores):
        if self.arduino is not None:
            if self.arduino.isOpen():
                self.arduino.write('2'.encode())
                for i in range(8):
                    self.arduino.write(str(vectores[i][idbutton]).encode())
                print('El dato ha sido enviado correctamente')
            else:
                print('La conexión está cerrada actualmente')
        else:
            print('Aún no se ha realizado la conexión con Arduino')

    def limpiar(self):
        if self.arduino != None:
            if self.arduino.isOpen():
                self.arduino.write('2'.encode())
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

