import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        self.setWindowTitle('Statusbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

# class MyApp(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         QToolTip.setFont(QFont('SansSerif', 10))
#         self.setToolTip('This is a <b>QWidget</b> Widget')

#         btn = QPushButton('Quit', self)
#         btn.setToolTip('Exit')
#         btn.move(300, 150)
#         btn.resize(btn.sizeHint())
#         btn.clicked.connect(QCoreApplication.instance().quit)

#         self.setWindowTitle('Test Application (Non-public)')
#         self.setWindowIcon(QIcon('NAVER.png'))
#         self.move(300, 300)
#         self.resize(400, 200)
#         self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())