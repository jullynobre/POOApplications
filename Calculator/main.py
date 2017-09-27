# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Calculator:
    __instance = None

    @staticmethod
    def instance():
        if not Calculator.__instance:
            Calculator.__instance = Calculator()
        return Calculator.__instance

    def __init__(self):
        self.n1 = ""
        self.n2 = ""
        self.operator = ""
        self.sol = ""

    def clicked_button(self, n):
        if self.operator == "":
            self.n1 += n
        else:
            self.n2 += n

    def clicked_operation(self, op):
        self.operator = op

    def clear(self):
        self.n1 = ""
        self.n2 = ""
        self.operator = ""

    def calc(self):
        print("op: ", self.operator)
        print("n1: ", self.n1)
        print("n2: ", self.n2)
        if self.operator == "+":
            self.sol = float(self.n1) + float(self.n2)
        elif self.operator == "-":
            self.sol = float(self.n1) - float(self.n2)
        elif self.operator == "X":
            self.sol = float(self.n1) * float(self.n2)
        elif self.operator == "/":
            self.sol = float(self.n1) / float(self.n2)
        else:
            self.sol = "Invalid Format"

        self.n1 = ""
        self.n2 = ""
        if self.sol != "Invalid Format":
            self.n1 = str(self.sol)


class Ui_Form(object):

    def clicked_button(self, value):
        calculator = Calculator.instance()
        self.textEdit.setPlainText(self.textEdit.toPlainText() + value)
        calculator.clicked_button(value)

    def clicked_operation(self, value):
        calculator = Calculator.instance()
        self.textEdit.setPlainText(self.textEdit.toPlainText() + value)
        calculator.clicked_operation(value)

    def clear(self):
        calculator = Calculator.instance()
        self.textEdit.setPlainText("")
        calculator.clear()

    def delete(self):
        print("delete")

    def calc(self):
        calculator = Calculator.instance()
        calculator.calc()
        self.textEdit.setPlainText(str(calculator.sol))

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(328, 448)
        Form.setStyleSheet("background-color:white;")
        self.btn1 = QtWidgets.QToolButton(Form)
        self.btn1.setGeometry(QtCore.QRect(10, 300, 71, 61))
        self.btn1.setStyleSheet("background-color:black;\n""font-size:40px;\n""border:0;\n""color: white;")
        self.btn1.setObjectName("btn1")
        self.btn1.clicked.connect(lambda: self.clicked_button("1"))
        self.btn7 = QtWidgets.QToolButton(Form)
        self.btn7.setGeometry(QtCore.QRect(10, 160, 71, 61))
        self.btn7.setStyleSheet("background-color:black;\n""font-size:40px;\n""border:0;\n""color: white;")
        self.btn7.setObjectName("btn7")
        self.btn7.clicked.connect(lambda: self.clicked_button("7"))
        self.btn4 = QtWidgets.QToolButton(Form)
        self.btn4.setGeometry(QtCore.QRect(10, 230, 71, 61))
        self.btn4.setStyleSheet("background-color:black;\n""font-size:40px;\n""border:0;\n""color: white;")
        self.btn4.setObjectName("btn4")
        self.btn4.clicked.connect(lambda: self.clicked_button("4"))
        self.btn6 = QtWidgets.QToolButton(Form)
        self.btn6.setGeometry(QtCore.QRect(170, 230, 71, 61))
        self.btn6.setStyleSheet("background-color:black;\n""font-size:40px;\n""border:0;\n""color: white;")
        self.btn6.setObjectName("btn6")
        self.btn6.clicked.connect(lambda: self.clicked_button("6"))
        self.btn8 = QtWidgets.QToolButton(Form)
        self.btn8.setGeometry(QtCore.QRect(90, 160, 71, 61))
        self.btn8.setStyleSheet("background-color:black;\n""font-size:40px;\n""border:0;\n""color: white;")
        self.btn8.setObjectName("btn8")
        self.btn8.clicked.connect(lambda: self.clicked_button("8"))
        self.btn5 = QtWidgets.QToolButton(Form)
        self.btn5.setGeometry(QtCore.QRect(90, 230, 71, 61))
        self.btn5.setStyleSheet("background-color:black;\n""font-size:40px;\n""border:0;\n""color: white;")
        self.btn5.setObjectName("btn5")
        self.btn5.clicked.connect(lambda: self.clicked_button("5"))
        self.btn9 = QtWidgets.QToolButton(Form)
        self.btn9.setGeometry(QtCore.QRect(170, 160, 71, 61))
        self.btn9.setStyleSheet("background-color:black;\n""font-size:40px;\n""border:0;\n""color: white;")
        self.btn9.setObjectName("btn9")
        self.btn9.clicked.connect(lambda: self.clicked_button("9"))
        self.btn2 = QtWidgets.QToolButton(Form)
        self.btn2.setGeometry(QtCore.QRect(90, 300, 71, 61))
        self.btn2.setStyleSheet("background-color:black;\n""font-size:40px;\n""border:0;\n""color: white;")
        self.btn2.setObjectName("btn2")
        self.btn2.clicked.connect(lambda: self.clicked_button("2"))
        self.btn3 = QtWidgets.QToolButton(Form)
        self.btn3.setGeometry(QtCore.QRect(170, 300, 71, 61))
        self.btn3.setStyleSheet("background-color:black;\n""font-size:40px;\n""border:0;\n""color: white;")
        self.btn3.setObjectName("btn3")
        self.btn3.clicked.connect(lambda: self.clicked_button("3"))
        self.btn0 = QtWidgets.QToolButton(Form)
        self.btn0.setGeometry(QtCore.QRect(90, 370, 71, 61))
        self.btn0.setStyleSheet("background-color:black;\n""font-size:40px;\n""border:0;\n""color: white;")
        self.btn0.setObjectName("btn0")
        self.btn0.clicked.connect(lambda: self.clicked_button("0"))
        self.btndiv = QtWidgets.QToolButton(Form)
        self.btndiv.setGeometry(QtCore.QRect(250, 160, 71, 61))
        self.btndiv.setStyleSheet("background-color:rgb(0, 0, 108);\n""font-size:40px;\n""border:0;\n""color: white;")
        self.btndiv.setObjectName("btndiv")
        self.btndiv.clicked.connect(lambda: self.clicked_operation("/"))
        self.btnmult = QtWidgets.QToolButton(Form)
        self.btnmult.setGeometry(QtCore.QRect(250, 230, 71, 61))
        self.btnmult.setStyleSheet("background-color:rgb(0, 0, 108);\n""font-size:40px;\n""border:0;\n""color: white;")
        self.btnmult.setObjectName("btnmult")
        self.btnmult.clicked.connect(lambda: self.clicked_operation("X"))
        self.btnsun = QtWidgets.QToolButton(Form)
        self.btnsun.setGeometry(QtCore.QRect(250, 300, 71, 61))
        self.btnsun.setStyleSheet("background-color:rgb(0, 0, 108);\n""font-size:40px;\n""border:0;\n""color: white;")
        self.btnsun.setObjectName("btnsun")
        self.btnsun.clicked.connect(lambda: self.clicked_operation("+"))
        self.btnsub = QtWidgets.QToolButton(Form)
        self.btnsub.setGeometry(QtCore.QRect(250, 370, 71, 61))
        self.btnsub.setStyleSheet("background-color:rgb(0, 0, 108);\n""font-size:40px;\n""border:0;\n""color: white;")
        self.btnsub.setObjectName("btnsub")
        self.btnsub.clicked.connect(lambda: self.clicked_operation("-"))
        self.btndot = QtWidgets.QToolButton(Form)
        self.btndot.setGeometry(QtCore.QRect(10, 370, 71, 61))
        self.btndot.setStyleSheet("background-color:rgb(0, 0, 108);\n""font-size:35px;\n""border:0;\n""color: white;")
        self.btndot.setObjectName("btndot")
        self.btndot.clicked.connect(lambda: self.clicked_button("."))
        self.btnclr = QtWidgets.QToolButton(Form)
        self.btnclr.setGeometry(QtCore.QRect(10, 90, 151, 61))
        self.btnclr.setStyleSheet("background-color:rgb(0, 0, 108);\n""font-size:35px;\n""border:0;\n""color: white;")
        self.btnclr.setObjectName("btnclr")
        self.btnclr.clicked.connect(lambda: self.clear())
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(3, 20, 321, 61))
        self.textEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.textEdit.setStyleSheet("text-align:right;\n""font-size:38px;\n""padding-left:5px;\n""border:0;")
        self.textEdit.setObjectName("textEdit")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 70, 311, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btncalc = QtWidgets.QToolButton(Form)
        self.btncalc.setGeometry(QtCore.QRect(170, 90, 151, 61))
        self.btncalc.setStyleSheet("background-color:rgb(0, 0, 75);\n""font-size:40px;\n""border:0;\n""color: white;")
        self.btncalc.setObjectName("btncalc")
        self.btncalc.clicked.connect(lambda: self.calc())
        self.btndel = QtWidgets.QToolButton(Form)
        self.btndel.setGeometry(QtCore.QRect(170, 370, 71, 61))
        self.btndel.setStyleSheet("background-color:rgb(0, 0, 108);\n""font-size:35px;\n""border:0;\n""color: white;")
        self.btndel.setObjectName("btndel")
        self.btndel.clicked.connect(lambda: self.delete())
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn1.setText(_translate("Form", "1"))
        self.btn7.setText(_translate("Form", "7"))
        self.btn4.setText(_translate("Form", "4"))
        self.btn6.setText(_translate("Form", "6"))
        self.btn8.setText(_translate("Form", "8"))
        self.btn5.setText(_translate("Form", "5"))
        self.btn9.setText(_translate("Form", "9"))
        self.btn2.setText(_translate("Form", "2"))
        self.btn3.setText(_translate("Form", "3"))
        self.btn0.setText(_translate("Form", "0"))
        self.btndiv.setText(_translate("Form", "/"))
        self.btnmult.setText(_translate("Form", "X"))
        self.btnsun.setText(_translate("Form", "+"))
        self.btnsub.setText(_translate("Form", "-"))
        self.btndot.setText(_translate("Form", "."))
        self.btnclr.setText(_translate("Form", "CLR"))
        self.btncalc.setText(_translate("Form", "="))
        self.btndel.setText(_translate("Form", "DEL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
