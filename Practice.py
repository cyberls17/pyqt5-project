import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class Application(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('Empty Space')
        
        self.setWindowTitle('Test Application')
        self.setWindowIcon(QIcon(r'C:\Users\user\Downloads\web.png'))
        self.setGeometry(300, 300, 300, 300)
        # self.move(300, 300)
        # self.resize(400, 200)

        exitbtn = QPushButton('Exit', self)
        exitbtn.move(200, 250)
        exitbtn.resize(exitbtn.sizeHint())
        exitbtn.setToolTip('Escape.')
        exitbtn.clicked.connect(QCoreApplication.instance().quit)
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Application()
    sys.exit(app.exec_())