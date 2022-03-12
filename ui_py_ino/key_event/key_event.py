'''     HELP -------------------
https://www.programcreek.com/python/example/101662/PyQt5.QtCore.Qt.Key_Left
https://doc.qt.io/archives/qtjambi-4.5.2_01/com/trolltech/qt/core/Qt.Key.html


'''

import sys
import serial as connector
from PyQt5 import uic, QtWidgets #, QtCore.Qt  # Use QtCore.Qt.Key_???
from PyQt5.QtCore import Qt     # Use Qt.Key_???m

qtCreatorFile = "ui_py_ino/ej_key_event/prueba_key_event.ui" # Nombre del archivo aquí.
#qtCreatorFile = "prueba_key_event.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals y Configuraciones Iniciales


    # Área de los Slots
    def keyPressEvent(self, event):
        #print(event.key())
        key = event.key()
        ex = "if event.key() == Qt.Key_{}:  self.writeLetter(chr(key))".format(chr(key))
        exec(ex)
        
        #if(event.key() == Qt.Key_Q):
        #    self.writeLetter('Q')
        #elif event.key() == QtCore.Qt.Key_Enter:
        #    pass
    
    def writeLetter(self, letter):
        self.lb_letter.setText(letter)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())