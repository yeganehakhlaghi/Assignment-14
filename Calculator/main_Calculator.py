from math import *

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import *


class Calculatore(QMainWindow):
    def __init__(self):
        super().__init__()


        loader = QUiLoader ()
        self.ui=loader.load("des.ui")
        self.ui.show()
        self.ui.btn_sum.clicked.connect(self.add)
        self.ui.btn_equal.clicked.connect(self.equal)
        self.ui.btn_sub.clicked.connect(self.sub)
        self.ui.btn_mul.clicked.connect(self.mul)
        self.ui.btn_sub.clicked.connect(self.div)
        self.ui.btn_mod.clicked.connect(self.mod)
        self.ui.btn_sign.clicked.connect(self.sign)


        self.ui.btn_ac.clicked.connect(self.ac)

        self.ui.btn_dec.clicked.connect(self.dec)

        self.ui.btn_sin.clicked.connect(self.sin)
        self.ui.btn_cos.clicked.connect(self.cos)
        self.ui.btn_tan.clicked.connect(self.tan)
        self.ui.btn_cot.clicked.connect(self.cot)
        self.ui.btn_log.clicked.connect(self.log)
        self.ui.btn_sqrt.clicked.connect(self.sqrt)

        self.ui.btn0.clicked.connect(self.button0)
        self.ui.btn1.clicked.connect(self.button1)
        self.ui.btn2.clicked.connect(self.button2)
        self.ui.btn3.clicked.connect(self.button3)
        self.ui.btn4.clicked.connect(self.button4)
        self.ui.btn5.clicked.connect(self.button5)
        self.ui.btn6.clicked.connect(self.button6)
        self.ui.btn7.clicked.connect(self.button7)
        self.ui.btn8.clicked.connect(self.button8)
        self.ui.btn9.clicked.connect(self.button9)
        

        self.res=0

    def add(self):
        self.mark='add' 
        self.num1 = int(self.ui.TB1.text())
        self.ui.TB1.setText("")
        #self.ui.TB1.setText(self.ui.TB1.text()+"+")
        self.res+= self.num1

    def sub(self):
        self.mark='sub' 
        self.num1 = int(self.ui.TB1.text())
        self.ui.TB1.setText("")
        self.res-= self.num1 

    def mul(self):
        self.mark='mul' 
        self.num1 = int(self.ui.TB1.text())
        self.ui.TB1.setText("")  

    def div(self):
        self.mark='div' 
        self.num1 = int(self.ui.TB1.text())
        self.ui.TB1.setText("") 

    def mod(self):
        self.mark='mod' 
        self.num1 = int(self.ui.TB1.text())
        self.ui.TB1.setText("") 


    def sin(self):
        self.mark='sin' 
        self.num1 = int(self.ui.TB1.text())
        res=sin(radians(self.num1))

    def cos(self):
        self.mark='cos' 
        self.num1 = int(self.ui.TB1.text())
        res=cos(radians(self.num1))
        self.ui.TB1.setText("")

    def tan(self):
        self.mark='tan' 
        res=tan(radians(self.num1))
        self.ui.TB1.setText("")

    def cot(self):
        self.mark='cot' 
        res=tan(radians(self.num1))
        self.ui.TB1.setText("")

    def log(self):
        self.mark='log' 
        res=log(self.num1)
        self.ui.TB1.setText("")

    def sqrt(self):
        self.mark='sqrt' 
        res=sqrt(self.num1)
        self.ui.TB1.setText("")

    
    def dec(self):
        pass

    def sign(self):
        pass


    def ac(self):
        self.ui.TB1.setText("")
        self.res=0
        self.mark = ""
    
    def equal(self):
        
        if self.mark == "add":
            
            self.num2=int(self.ui.TB1.text())
            result=self.res+self.num2
            
            self.ui.TB1.setText(str(result))

        if self.mark == "sub":
            
            self.num2=int(self.ui.TB1.text())
            result=self.res-self.num2
            
            self.ui.TB1.setText(str(result))


    def button0(self):
        self.ui.TB1.setText(self.ui.TB1.text() +"0")

    def button1(self):
        self.ui.TB1.setText(self.ui.TB1.text() +"1")

    def button2(self):
        self.ui.TB1.setText(self.ui.TB1.text() +"2")

    def button3(self):
        self.ui.TB1.setText(self.ui.TB1.text() +"3")

    def button4(self):
        self.ui.TB1.setText(self.ui.TB1.text() +"4")

    def button5(self):
        self.ui.TB1.setText(self.ui.TB1.text() +"5")

    def button6(self):
        self.ui.TB1.setText(self.ui.TB1.text() +"6")

    def button7(self):
        self.ui.TB1.setText(self.ui.TB1.text() +"7")
    
    def button8(self):
        self.ui.TB1.setText(self.ui.TB1.text() +"8")
    
    def button9(self):
        self.ui.TB1.setText(self.ui.TB1.text() +"9")



    

    #def Test(self):
        #print("Hello QT")
        #self.ui.My_txt.setText("Hello Qt:)")



if __name__ == "__main__":

    app = QApplication()
    calculatore_main_window = Calculatore()
    app.exec()
