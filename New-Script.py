import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
# 필요한 모듈 불러오기

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Test Application") # 창 이름 설정
        self.setWindowIcon(QIcon('web.png')) # 창 아이콘 설정
        self.setGeometry(300, 300, 300, 200) # 창의 위치와 크기 설정 (move(), resize() 두 기능을 합쳐 놓은 것과 같음)
        self.show() # 위젯을 스크린에 표시


if __name__ == '__main__':
    app = QApplication(sys.argv) # PyQt5 어플리케이션 객체 생성
    ex = App()
    sys.exit(app.exec_())
# 테스트 코드