import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QTabWidget,
    QWidget,
    QLabel,
    QVBoxLayout,
    QGridLayout
)

mport sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow , QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Psych Section")
        self.setGeometry(100,100,600,500)

        widget = QLabel("Psychology")
        widget2 = QLabel("Psych sets")
        widget2.move(250,250)
        font = widget.font()# <1>
        font2 = widget2.font()
        font2.setPointSize(15)
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)# <2>
        
        
        self.setCentralWidget(widget2)
        self.setCentralWidget(widget)
        Button = QPushButton("Cognitive ", self)
        Button2 = QPushButton("Social ", self)
        Button3 = QPushButton("Personality", self)
        Button4 = QPushButton("Humanistic", self)
        Button5 = QPushButton("Behaviorism", self)
        Button6 = QPushButton("Forensic", self)
        
        Button.move(250,300)
        Button2.move(250,330)
        Button3.move(250,360)
        Button4.move(250,390)
        Button5.move(250,420)
        Button6.move(250,450)
     


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
