import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Tela import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.hslCaracteres.valueChanged.connect(self.number_changed)

    def show(self):
        self.main_win.show()

    def number_changed(self):
        new_value = str(self.ui.hslCaracteres.value())
        self.ui.lbCaracteres.setText(f"{new_value} Caracteres" if int(new_value) > 1 else f"{new_value} Caractere")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
