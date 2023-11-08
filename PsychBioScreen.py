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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        """
        def initUI(self):
            self.label = Qtwidgets.QLabel(self)
            self.label.setText("Psycology Sections")
            self.label.setPointSize(30)
            self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        """
        
        self.setWindowTitle("Psych Sections ")
        #self.initUI()
        Title = QLabel("Psych Sets")
        font = Title.font()
        font.setPointSize(45)
        Title.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        

        layout = QVBoxLayout()
        Button = QGridLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        layout.addWidget(Title)
        #button.addButton()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
