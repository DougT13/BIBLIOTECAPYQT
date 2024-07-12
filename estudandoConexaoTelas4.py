from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from random import randint

import sys


#
#
# NESTE MODELO, TRABALHAMOS COM A CRIAÇÃO DE MULTIPLAS JANELAS
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

# class window2(QWidget):

#     def __init__(self):
#         super().__init__()

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.window1 = AnotherWindow()
        self.window2 = AnotherWindow()

        button1 = QPushButton("Tela 1")
        button2 = QPushButton("Tela 2")

        button1.clicked.connect(self.toggle_window1)
        button2.clicked.connect(self.toggle_window2)

        l = QVBoxLayout()
        l.addWidget(button1)
        l.addWidget(button2)

        w = QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)

    #feito dessa forma, ele irá verificar se a janela está fechada e, se for verdade, irá abrir de novo. Se clicar no botão novamente, a janela irá fechar.
    def toggle_window1(self, checked):
        if self.window1.isVisible():
            self.window1.hide()
        else:
            self.window1.show()

    def toggle_window2(self, checked):
        if self.window2.isVisible():
            self.window2.hide()
        else:
            self.window2.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()