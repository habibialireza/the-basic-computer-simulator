# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import time
from PyQt5 import QtCore, QtGui, QtWidgets
stopflag = 0
dic = ''
step=0
AC = '0000'
DR = '0000'
AR = '000'
IR = '0000'
TR = '0000'
PC = '000'
INPR = '00'
OUTR = '00'
I = 0
S = 0
sc = 0
E = '0'
R = 0
IEN = 0
FGI = 0
FGO =0
i = 0
M = ''
class Ui_Dialog(object):
    # def s16(self, value):
    #     return -(value & 0x8000) | (value & 0x7fff)

    def is_ready(self):
        global step_flag, run_flag
        if step_flag == True:
            step_flag = False
            return True
        elif run_flag == True:
            return True
        else:
            return False

    def wait_until(self, timeout, period=0.25):
        mustend = time.time() + timeout
        while time.time() < mustend:
            if self.is_ready(): return True
            time.sleep(period)
        return False
    def andd(a, b):
        if a == "0" or b == "0":
            return "0"
        else:
            return "1"

    def go(self, cmd):

        global PC, INPR, OUTR, AC, DR, AR, IR, TR,I, S, sc, E, R, IEN, FGI, FGO,step,M, stopflag
        if len(cmd) == 0:
            return
        spliter = cmd['com'].split(' ')
        spliter = list(filter(None, spliter))
        # for cmd in dic:
        line = int(PC, 16)
        if step == 1 and stopflag == 0:
            print(PC)
            self.textEdit_5.setPlainText('Fetch\n AR <- PC \n PC <- PC+1, IR = M[AR]')
            print('step1')
            # fetch
            AR = PC
            # step
            # self.wait_until(100, 100)
            PC = hex(int(PC, 16) + 1)[2:].zfill(3)
            IR = M[int(AR, 16)]
            self.textBrowser.setText(AR)
            self.textEdit.setText(PC)
            self.textEdit_2.setText(IR)
        # decode

        if step == 2 and stopflag == 0:
            print(PC)
            self.textEdit_5.setPlainText('Decode\n set AR and I and decode ....')
            print('step2')
            IR_temp = bin(int(IR, 16))[2:].zfill(16)
            I = IR_temp[0]
            AR = IR[1:]
            self.textBrowser.setText(AR)
            self.plainTextEdit_2.setPlainText(I)
        # if cmd['com'] == '':
        #     return
        if step == 3 and stopflag == 0:
            print(PC)
            self.textEdit_5.setText(f'EXECUTE :\n {cmd["com"]} ')
            print('step3')
            if spliter[0] == "CLA":
                # CLA
                SC = 0
                AC = "0000"

            if spliter[0] == "CLE":
                # CLE
                SC = 0
                E = '0'

            if spliter[0] == "CMA":
                # CMA
                SC = 0
                x = int(AC, 16)
                AC = hex((2 ** 16) - 1 - x)[2:].zfill(16)

            if spliter[0] == "CME":
                # CME
                SC = 0
                if E == '0':
                    E = '1'
                else:
                    E = '0'

            if spliter[0] == "CIR":
                # CIR
                SC = 0
                x = E
                AC_temp = bin(int(AC, 16))[2:].zfill(16)
                E = AC_temp[15]
                for i in range(15, 0, -1):
                    AC_temp[i] = AC_temp[i - 1]
                AC_temp[0] = x
                AC = hex(int(AC_temp, 2))[2:].zfill(4)

            if spliter[0] == "CIL":
                # CIL
                SC = 0
                x = E
                AC_temp = bin(int(AC, 16))[2:].zfill(16)
                E = AC_temp[0]
                for i in range(0, 15):
                    AC_temp[i] = AC_temp[i + 1]
                AC_temp[15] = x
                AC = hex(int(AC_temp, 2))[2:].zfill(4)

            if spliter[0] == "INC":
                # INC
                SC = 0
                AC = hex(int(AC, 16) + 1)[2:].zfill(16)

            if spliter[0] == "SPA":
                # SPA
                SC = 0
                AC_temp = bin(int(AC, 16))[2:].zfill(16)
                if AC_temp[0] == '0':
                    PC = hex(int(PC, 16) + 1)[2:].zfill(3)

            if spliter[0] == "SNA":
                # SNA
                SC = 0
                AC_temp = bin(int(AC, 16))[2:].zfill(16)
                if AC_temp[0] == '1':
                    PC = hex(int(PC, 16) + 1)[2:].zfill(3)

            if spliter[0] == "SZA":
                # SZA
                SC = 0
                if int(AC, 16) == 0:
                    PC = hex(int(PC, 16) + 1)[2:].zfill(3)

            if spliter[0] == "SZE":
                # SZE
                SC = 0
                if E == '0':
                    PC = hex(int(PC, 16) + 1)[2:].zfill(3)

            if spliter[0] == "HLT":
                # HLT

                SC = 0
                S = 0
                stopflag = 1
            if spliter[0] == "INP":
                # INP
                SC = 0
                FGI = 0
                AC_temp = bin(int(AC, 16))[2:].zfill(16)
                for i in range(0, 8):
                    AC_temp[7 - i] = INPR[i]

            if spliter[0] == "OUT":
                # OUT
                SC = 0
                FGO = 0
                AC_temp = bin(int(AC, 16))[2:].zfill(16)
                for i in range(0, 8):
                    OUTR[i] = AC_temp[7 - i]

            if spliter[0] == "SKI":
                # SKI
                SC = 0
                if FGI == 1:
                    PC = hex(int(PC, 16) + 1)[2:].zfill(3)

            if spliter[0] == "SKO":
                # SKO
                SC = 0
                if FGO == 1:
                    PC = hex(int(PC, 16) + 1)[2:].zfill(3)

            if spliter[0] == "ION":
                # ION
                SC = 0
                IEN = 1

            if spliter[0] == "IOF":
                # IOF
                SC = 0
                IEN = 0

            if spliter[0] == "AND":
                # AND
                DR = M[int(AR, 16)]
                # step
                sc = 0
                AC3 = "0000000000000000"
                AC2 = bin(int(AC, 16))[2:].zfill(16)
                DR2 = bin(int(DR, 16))[2:].zfill(16)
                for i in range(0, 16):
                    AC3[i] = AC2[i] and DR2[i]
                AC = hex(int(AC3, 2))[2:].zfill(4)

            if spliter[0] == "ADD":
                # ADD
                DR = M[int(AR, 16)]
                # step
                sc = 0
                x = int(AC, 16)
                y = int(DR, 16)
                if (x + y >= 2 ** 16):
                    E = "1"
                else:
                    E = "0"

                z = x + y
                z = int(z)
                z2 = bin(z)
                if (z >= 2 ** 16):
                    z2 = z2[3:]
                    AC = hex(int(z2, 2))[2:].zfill(4)
                else:
                    z2 = z2[2:]
                    AC = hex(int(z2, 2))[2:].zfill(4)

            if spliter[0] == "LDA":
                # lda
                DR = M[int(AR, 16)]
                # step
                SC = 0
                AC = DR

            if spliter[0] == "STA":
                # STA
                SC = 0
                M[int(AR, 16)] = AC
                item = QtWidgets.QTableWidgetItem(AC)
                self.tableWidget.setItem(int(AR, 16), 3, item)

            if spliter[0] == "BUN":
                # BUN
                SC = 0
                PC = AR
            if spliter[0] == "BSA":
                # BSA
                AR += 1
                M[int(AR, 16)] = PC
                # step
                SC = 0
                PC = AR

            if spliter[0] == "ISZ":
                # ISZ
                DR = M[int(AR, 16)]
                # step
                DR = hex(int(DR, 16) + 1)[2:].zfill(4)
                # step
                SC = 0
                x = int(DR, 16)
                if x == 0:
                    PC = hex(int(PC, 16) + 1)[2:].zfill(3)
                M[int(AR, 16)] = DR
            print(PC)
            self.textBrowser.setText(AR)
            self.textEdit.setText(PC)
            self.textBrowser_2.setText(DR)
            self.textEdit_2.setText(IR)
            self.textBrowser_4.setText(TR)
            self.textBrowser_3.setText(AC)
            self.textBrowser_6.setText(OUTR)
            self.textBrowser_5.setText(INPR)
            self.plainTextEdit_2.setPlainText(str(I))
            self.textBrowser_10.setText(E)
            self.textBrowser_8.setText(str(FGI))
            self.textBrowser_7.setText(str(FGO))
            self.textBrowser_11.setText(str(IEN))

    def set_Ram(self, coms,m):
        global dic,M,PC

        dic = coms
        PC = dic[0]['address']
        self.textBrowser.setText(AR)
        self.textEdit.setText(PC)
        self.textBrowser_2.setText(DR)
        self.textEdit.setText(IR)
        self.textBrowser_4.setText(TR)
        self.textBrowser_3.setText(AC)
        self.textBrowser_6.setText(OUTR)
        self.textBrowser_5.setText(INPR)
        self.plainTextEdit_2.setPlainText(str(I))
        self.textBrowser_10.setText(E)
        self.textBrowser_8.setText(str(FGI))
        self.textBrowser_7.setText(str(FGO))
        self.textBrowser_11.setText(str(IEN))
        M = m
        for i in range(0,4096):
            item = QtWidgets.QTableWidgetItem(hex(i)[2:])
            self.tableWidget.setItem(i,1,item)
        for i in coms:
            lable = QtWidgets.QTableWidgetItem(i['lable'])
            Hex = QtWidgets.QTableWidgetItem(i['hex'])
            Instruction = QtWidgets.QTableWidgetItem(i['com'])
            row = int(i['address'], 16)
            self.tableWidget.setItem(row, 0, lable)
            self.tableWidget.setItem(row, 2, Instruction)
            self.tableWidget.setItem(row, 3, Hex)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(863, 492)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 50, 361, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 1, 4, 1, 1)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.gridLayout.addWidget(self.textBrowser_5, 3, 4, 1, 1)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout.addWidget(self.textBrowser_3, 2, 4, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.textBrowser_2, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.gridLayout.addWidget(self.textBrowser_4, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.gridLayout.addWidget(self.textBrowser_6, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(50, 210, 171, 111))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 0, 0, 1, 1)
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.textBrowser_11.setEnabled(True)
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.gridLayout_2.addWidget(self.textBrowser_11, 3, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 3, 0, 1, 1)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_2)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout_2.addWidget(self.plainTextEdit_2, 0, 1, 1, 1)
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.gridLayout_2.addWidget(self.textBrowser_7, 1, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 1, 2, 1, 1)
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.gridLayout_2.addWidget(self.textBrowser_8, 1, 1, 1, 1)
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.gridLayout_2.addWidget(self.textBrowser_10, 0, 3, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 0, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 1, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(440, 50, 421, 431))
        self.tableWidget.setRowCount(4096)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.verticalHeader().setVisible(False)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(650, 10, 47, 13))
        self.label_10.setObjectName("label_10")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 440, 61, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.step_clicked)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 440, 61, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.run_clicked)
        self.textEdit_5 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_5.setGeometry(QtCore.QRect(100, 350, 311, 81))
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(10, 380, 81, 16))
        self.label_17.setObjectName("label_17")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_8.setText(_translate("Dialog", "  INPR : "))
        self.label_4.setText(_translate("Dialog", "  IR : "))
        self.label_2.setText(_translate("Dialog", "  PC : "))
        self.label_3.setText(_translate("Dialog", "AR : "))
        self.label_5.setText(_translate("Dialog", "DR : "))
        self.label_6.setText(_translate("Dialog", "  AC : "))
        self.label_7.setText(_translate("Dialog", "TR"))
        self.label_9.setText(_translate("Dialog", "OUTR:"))
        self.label_14.setText(_translate("Dialog", " I : "))
        self.label_18.setText(_translate("Dialog", "  IEN : "))
        self.label_11.setText(_translate("Dialog", "FGO: "))
        self.label_16.setText(_translate("Dialog", "   E : "))
        self.label_15.setText(_translate("Dialog", " FGI:"))
        self.label_10.setText(_translate("Dialog", "RAM:"))
        self.pushButton.setText(_translate("Dialog", "STEP"))
        self.pushButton_2.setText(_translate("Dialog", "RUN"))
        self.label_17.setText(_translate("Dialog", "Microoperation"))
    def step_clicked(self):

        global step, i, dic
        if i <= len(dic) - 1:
            cmd = dic[i]
            step += 1
            self.go(cmd)
            if step==3:
                step = 0
                i += 1



    def run_clicked(self):
        global step, i, dic
        while i <= len(dic) - 1:
            cmd = dic[i]
            step += 1
            self.go(cmd)
            if step == 3:
                step = 0
                i += 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())