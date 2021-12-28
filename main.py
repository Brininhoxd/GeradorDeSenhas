import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Tela import Ui_MainWindow
from Senha import Senha
# from pyperclip import copy


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.senha = Senha()
        self.ui.hslCaracteres.valueChanged.connect(self.mudou_numero)
        self.ui.chkLetraMaiuscula.stateChanged.connect(self.mudou_chk_maiuscula)
        self.ui.chkLetraMinuscula.stateChanged.connect(self.mudou_chk_minuscula)
        self.ui.chkNumero.stateChanged.connect(self.mudou_chk_numero)
        self.ui.chkSimbolo.stateChanged.connect(self.mudou_chk_simbolo)
        self.ui.txtSenha.isReadOnly = True
        self.ui.btnCopy.clicked.connect(self.clicou_copiar)
        self.ui.btnGerarSenha.clicked.connect(self.clicou_gerar)

    def show(self):
        self.main_win.show()

    def mudou_numero(self):
        novo_valor = str(self.ui.hslCaracteres.value())
        self.ui.lbCaracteres.setText(f"{novo_valor} Caracteres" if int(novo_valor) > 1 else f"{novo_valor} Caractere")
    
    def mudou_chk_maiuscula(self):
        novo_valor = bool(self.ui.chkLetraMaiuscula.checkState())
        self.senha.verifica_maiuscula(novo_valor)
    
    def mudou_chk_minuscula(self):
        novo_valor = bool(self.ui.chkLetraMinuscula.checkState())
        self.senha.verifica_minuscula(novo_valor)

    def mudou_chk_numero(self):
        novo_valor = bool(self.ui.chkNumero.checkState())
        self.senha.verifica_numero(novo_valor)
    
    def mudou_chk_simbolo(self):
        novo_valor = bool(self.ui.chkSimbolo.checkState())
        self.senha.verifica_simbolo(novo_valor)

    def clicou_copiar(self):
        valor = str(self.ui.txtSenha.text())
        # if valor != "Sua Senha":
        #     copy(valor)

    def clicou_gerar(self):
        tamanho = int(self.ui.hslCaracteres.value())
        senha = self.senha._gerar_senha(tamanho)
        self.ui.txtSenha.setText(senha)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
