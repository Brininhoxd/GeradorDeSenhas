# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tela.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 450)
        MainWindow.setMinimumSize(QtCore.QSize(550, 450))
        MainWindow.setMaximumSize(QtCore.QSize(550, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/windowIcon/icons/cadeado.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(550, 450))
        self.centralwidget.setMaximumSize(QtCore.QSize(550, 450))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frParteSuperior = QtWidgets.QFrame(self.centralwidget)
        self.frParteSuperior.setMaximumSize(QtCore.QSize(16777215, 75))
        self.frParteSuperior.setStyleSheet("background-color: rgb(252, 163, 17);")
        self.frParteSuperior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frParteSuperior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frParteSuperior.setObjectName("frParteSuperior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frParteSuperior)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txtSenha = QtWidgets.QLineEdit(self.frParteSuperior)
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(13)
        self.txtSenha.setFont(font)
        self.txtSenha.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(0, 0, 0);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0)\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(70, 70, 70)\n"
"}")
        self.txtSenha.setInputMask("")
        self.txtSenha.setText("")
        self.txtSenha.setMaxLength(30)
        self.txtSenha.setFrame(True)
        self.txtSenha.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txtSenha.setAlignment(QtCore.Qt.AlignCenter)
        self.txtSenha.setReadOnly(True)
        self.txtSenha.setClearButtonEnabled(False)
        self.txtSenha.setObjectName("txtSenha")
        self.horizontalLayout.addWidget(self.txtSenha)
        self.btnCopy = QtWidgets.QPushButton(self.frParteSuperior)
        self.btnCopy.setMinimumSize(QtCore.QSize(43, 43))
        self.btnCopy.setMaximumSize(QtCore.QSize(34, 43))
        self.btnCopy.setToolTipDuration(0)
        self.btnCopy.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;    \n"
"    background-image: url(:/copyIcon/icons/copy-icon.png);\n"
"    background-position: center;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(50, 50, 50);\n"
"    color: rgba(200, 200, 200);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgba(35, 35, 35);\n"
"    color: rgba(200, 200, 200);\n"
"}")
        self.btnCopy.setText("")
        self.btnCopy.setObjectName("btnCopy")
        self.horizontalLayout.addWidget(self.btnCopy)
        self.verticalLayout_2.addWidget(self.frParteSuperior)
        self.frParteInferior = QtWidgets.QFrame(self.centralwidget)
        self.frParteInferior.setEnabled(True)
        self.frParteInferior.setStyleSheet("background-color: rgb(20,33,61);")
        self.frParteInferior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frParteInferior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frParteInferior.setObjectName("frParteInferior")
        self.gridLayout = QtWidgets.QGridLayout(self.frParteInferior)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 4, 1, 1)
        self.lbCaracteres = QtWidgets.QLabel(self.frParteInferior)
        self.lbCaracteres.setMinimumSize(QtCore.QSize(130, 15))
        self.lbCaracteres.setMaximumSize(QtCore.QSize(130, 15))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(12)
        self.lbCaracteres.setFont(font)
        self.lbCaracteres.setStyleSheet("color: rgb(255, 255, 255)")
        self.lbCaracteres.setObjectName("lbCaracteres")
        self.gridLayout.addWidget(self.lbCaracteres, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 4, 1, 1)
        self.btnGerarSenha = QtWidgets.QPushButton(self.frParteInferior)
        self.btnGerarSenha.setMinimumSize(QtCore.QSize(450, 28))
        self.btnGerarSenha.setMaximumSize(QtCore.QSize(450, 28))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(14)
        self.btnGerarSenha.setFont(font)
        self.btnGerarSenha.setStyleSheet("QPushButton {\n"
"    background-color: rgb(100, 100, 100);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid rgb(135,135,135);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(60,60,60);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 3px solid rgb(100, 100, 100);\n"
"    background-color: rgb(252,163,17);\n"
"    color: rgb(335,35,35)\n"
"}")
        self.btnGerarSenha.setFlat(False)
        self.btnGerarSenha.setObjectName("btnGerarSenha")
        self.gridLayout.addWidget(self.btnGerarSenha, 3, 1, 1, 3)
        self.frChk = QtWidgets.QFrame(self.frParteInferior)
        self.frChk.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frChk.setStyleSheet("background-color: rgb(20,33,61);")
        self.frChk.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frChk.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frChk.setObjectName("frChk")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frChk)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 0, 0, 1, 1)
        self.chkLetraMaiuscula = QtWidgets.QCheckBox(self.frChk)
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(14)
        self.chkLetraMaiuscula.setFont(font)
        self.chkLetraMaiuscula.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkLetraMaiuscula.setAutoFillBackground(False)
        self.chkLetraMaiuscula.setStyleSheet("QCheckBox{\n"
"    color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    border: 3px solid rgb(100, 100, 100);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(135, 135, 135);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    border: 3px solid rgb(100, 100, 100);\n"
"    background-color: rgb(252,163,17);\n"
"}")
        self.chkLetraMaiuscula.setTristate(False)
        self.chkLetraMaiuscula.setObjectName("chkLetraMaiuscula")
        self.gridLayout_2.addWidget(self.chkLetraMaiuscula, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 0, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 1, 0, 1, 1)
        self.chkNumero = QtWidgets.QCheckBox(self.frChk)
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(14)
        self.chkNumero.setFont(font)
        self.chkNumero.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkNumero.setAutoFillBackground(False)
        self.chkNumero.setStyleSheet("QCheckBox{\n"
"    color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    border: 3px solid rgb(100, 100, 100);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(135, 135, 135);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    border: 3px solid rgb(100, 100, 100);\n"
"    background-color: rgb(252,163,17);\n"
"}")
        self.chkNumero.setObjectName("chkNumero")
        self.gridLayout_2.addWidget(self.chkNumero, 1, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 1, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(163, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 2, 0, 1, 1)
        self.chkLetraMinuscula = QtWidgets.QCheckBox(self.frChk)
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.chkLetraMinuscula.setFont(font)
        self.chkLetraMinuscula.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkLetraMinuscula.setAutoFillBackground(False)
        self.chkLetraMinuscula.setStyleSheet("QCheckBox{\n"
"    color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    border: 3px solid rgb(100, 100, 100);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(135, 135, 135);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    border: 3px solid rgb(100, 100, 100);\n"
"    background-color: rgb(252,163,17);\n"
"}")
        self.chkLetraMinuscula.setObjectName("chkLetraMinuscula")
        self.gridLayout_2.addWidget(self.chkLetraMinuscula, 2, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(162, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem11, 2, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(163, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem12, 3, 0, 1, 1)
        self.chkSimbolo = QtWidgets.QCheckBox(self.frChk)
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(14)
        self.chkSimbolo.setFont(font)
        self.chkSimbolo.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chkSimbolo.setAutoFillBackground(False)
        self.chkSimbolo.setStyleSheet("QCheckBox{\n"
"    color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    border: 3px solid rgb(100, 100, 100);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(135, 135, 135);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    border: 3px solid rgb(100, 100, 100);\n"
"    background-color: rgb(252,163,17);\n"
"}")
        self.chkSimbolo.setObjectName("chkSimbolo")
        self.gridLayout_2.addWidget(self.chkSimbolo, 3, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(162, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem13, 3, 2, 1, 1)
        self.gridLayout.addWidget(self.frChk, 0, 0, 1, 5)
        self.hslCaracteres = QtWidgets.QSlider(self.frParteInferior)
        self.hslCaracteres.setMinimumSize(QtCore.QSize(450, 22))
        self.hslCaracteres.setMaximumSize(QtCore.QSize(450, 22))
        self.hslCaracteres.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid;\n"
"    height: 10px; \n"
"    background-color: rgb(100, 100, 100);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {   \n"
"    \n"
"    background-color: rgb(252, 163, 17);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 15px;\n"
"     margin: -3px 0;\n"
"       border-radius: 5px;\n"
"}")
        self.hslCaracteres.setMinimum(1)
        self.hslCaracteres.setMaximum(30)
        self.hslCaracteres.setPageStep(1)
        self.hslCaracteres.setProperty("value", 15)
        self.hslCaracteres.setOrientation(QtCore.Qt.Horizontal)
        self.hslCaracteres.setInvertedAppearance(False)
        self.hslCaracteres.setInvertedControls(False)
        self.hslCaracteres.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.hslCaracteres.setObjectName("hslCaracteres")
        self.gridLayout.addWidget(self.hslCaracteres, 1, 1, 1, 3)
        self.verticalLayout_2.addWidget(self.frParteInferior)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gerador de Senhas"))
        self.txtSenha.setPlaceholderText(_translate("MainWindow", "Sua Senha", "Sua Senha"))
        self.btnCopy.setToolTip(_translate("MainWindow", "Copiar"))
        self.lbCaracteres.setText(_translate("MainWindow", "30 Caracteres"))
        self.btnGerarSenha.setText(_translate("MainWindow", "Gerar Senha"))
        self.chkLetraMaiuscula.setText(_translate("MainWindow", "Letra Maiúscula"))
        self.chkNumero.setText(_translate("MainWindow", "Letra Minúscula"))
        self.chkLetraMinuscula.setText(_translate("MainWindow", "Números"))
        self.chkSimbolo.setText(_translate("MainWindow", "Símbolos"))
import file_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())