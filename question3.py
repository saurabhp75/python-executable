from PyQt5.QtWidgets import (QWidget, QLabel, QScrollArea, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.scroll = QScrollArea()             
        self.widget = QWidget()               
        self.vbox = QVBoxLayout()               

        object = QLabel("Click <a href='https://github.com/saurabhp75/python-executable'>here</a> for code")
        object.setOpenExternalLinks(True)
        self.vbox.addWidget(object)

        object = QLabel("==========================================")
        self.vbox.addWidget(object)

        for x in range(1,101):
            # Multiple of 3 and 5
            if(x%3==0 and x%5==0):
               object = QLabel("FizzBuzz")
            # Multiple of 5
            elif(x%5==0):
                object = QLabel("Buzz")
            # Multiple of 3
            elif(x%3==0):
               object = QLabel("Fizz")
            else:
               object = QLabel(f"{x}")

            self.vbox.addWidget(object)

        self.widget.setLayout(self.vbox)

        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Solution to Question3')
        self.show()

        return

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()