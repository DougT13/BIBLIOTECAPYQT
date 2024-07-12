from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from random import randint

import sys


#
#
# NESTE MODELO, TRABALHAMOS COM AS JANELAS JÁ PRONTAS E, IREMOS MOSTRÁ-LAS QUANDO SOLICITADO
#
#

class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0,100))
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.w = AnotherWindow()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.toggle_window)
        self.setCentralWidget(self.button)

    #feito dessa forma, ele irá verificar se a janela está fechada e, se for verdade, irá abrir de novo. Se clicar no botão novamente, a janela irá fechar.
    def toggle_window(self, checked):
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()
        


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()