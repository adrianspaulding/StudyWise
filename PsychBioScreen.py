import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QTabWidget,
    QWidget,
)

class psychologySetWin(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Psych Sections ")
        self.initUI()
        Title = Qlabel("Psych Sets")
        font = Title.Font()
        font.setPointSize(45)
        Title.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        def initUI(self):
            self.lable = Qtwidgets.Qlabel(self)
            self.lable.setText("Psycology Sections")
            self.lable.setPointSize(30)
            self.lable.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        layout = QVBoxLayout()
        Button = QGridLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        layout.addWidget(Title)
        button.addButton()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()