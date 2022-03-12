import sys
import gatoui # NameFile donde esta la ventana
from PyQt5 import uic, QtWidgets
 
class MyApp(QtWidgets.QMainWindow, gatoui.Ui_MainWindow): # NameFile

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        gatoui.Ui_MainWindow.__init__(self) # NameFile
        self.setupUi(self)

        #Area de los signals ... Nombre de variables       
        self.btn_grp.buttonClicked[int].connect(self.click)
        self.btnAction.clicked.connect(self.start)
        self.tab = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
        self.scoreX = 0
        self.scoreO = 0
        self.flagX = True
        

    #Area de Slots ... funciones
    def start(self):
        self.tab = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
        self.eraseContent()
        self.updateTurn()

        if self.btnAction.text() == 'Start':
            self.btnAction.setText('Reset')
            self.setBtnState(True)          

    
    def click(self, ide):
        #self.txt.setText(ide.__str__())
        btn = self.btn_grp.button(ide)        
        if not btn.text():  # SI NO tiene texto...
            if self.flagX:
                self.game(ide, btn, 1, 'X', 'color:#F92672;')

            else:
                self.game(ide, btn, 0, 'O', 'color: #66D9EF;')  
          
    # ide = Id of Button; btn = Objeto seleccionado; valor = 0 or 1; XoO = caracter X or O; color = red o blue
    def game(self, ide, btn, valor, XoO, color):
        btn.setText(XoO)
        btn.setStyleSheet(color)
        self.flagX = not self.flagX
        self.tab[ide] = valor
        self.updateTurn()
        self.checkWinner(XoO)


    def checkWinner(self, XoO):
        if (self.tab[0] > -1 and self.tab[0] == self.tab[4] and self.tab[0] == self.tab[8]) or (self.tab[2] > -1 and self.tab[2] == self.tab[4] and self.tab[2] == self.tab[6]):
            self.gameOver(XoO)
            return
        # Horizontal
        for i in range(0, 7, 3):
            if(self.tab[i] > -1 and self.tab[i] == self.tab[i+1] and self.tab[i] == self.tab[i+2]):
                self.gameOver(XoO)
                return            
        # Vertical
        for i in range(0, 3):
            if(self.tab[i] > -1 and self.tab[i] == self.tab[i+3] and self.tab[i] == self.tab[i+6]):
                self.gameOver(XoO)
                return
        

    def gameOver(self, XoO):
        self.setBtnState(False)
        self.btnAction.setText('Start')
        #txt = 'Las ',XoO, '\'s ganaron!'
        self.lbUp.setText('Las {0}\'s ganaron!!!'.format(XoO))
        #self.lbUp.setText(('Las ', XoO, '\'s ganaron!'))

        if XoO == 'X':
            self.scoreX = self.scoreX + 1
            self.lbXScore.setText(self.scoreX.__str__())
        else:
            self.scoreO = self.scoreO + 1
            self.lbOScore.setText(self.scoreO.__str__())


    def updateTurn(self):
        if self.flagX:
            self.lbUp.setText('Turno de las X\'s')
        else:
            self.lbUp.setText('Turno de las O\'s')


    def setBtnState(self, state):
        self.btn1.setEnabled(state)
        self.btn2.setEnabled(state)
        self.btn3.setEnabled(state)
        self.btn4.setEnabled(state)
        self.btn5.setEnabled(state)
        self.btn6.setEnabled(state)
        self.btn7.setEnabled(state)
        self.btn8.setEnabled(state)
        self.btn9.setEnabled(state)

    
    def eraseContent(self):
        self.btn1.setText('')
        self.btn2.setText('')
        self.btn3.setText('')
        self.btn4.setText('')
        self.btn5.setText('')
        self.btn6.setText('')
        self.btn7.setText('')
        self.btn8.setText('')
        self.btn9.setText('')
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


'''
self.btn_grp = QtWidgets.QButtonGroup()
        self.btn_grp.setExclusive(True)
        self.btn_grp.addButton(self.btn1, 0)
        self.btn_grp.addButton(self.btn2, 1)
        self.btn_grp.addButton(self.btn3, 2)
        self.btn_grp.addButton(self.btn4, 3)
        self.btn_grp.addButton(self.btn5, 4)
        self.btn_grp.addButton(self.btn6, 5)
        self.btn_grp.addButton(self.btn7, 6)
        self.btn_grp.addButton(self.btn8, 7)
        self.btn_grp.addButton(self.btn9, 8)

'''
