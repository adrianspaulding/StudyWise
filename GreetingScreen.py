import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QStackedLayout,
    QWidget
)

# Create Main Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("StudyWise")
        
        # Create app title to display
        appName = QLabel("StudyWise")
        font = appName.font()
        font.setPointSize(60)
        appName.setFont(font)
        appName.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        # Create greeting message
        user = "Person" # This should be changed to allow the user to enter their name
        greetingMsg = QLabel("Hello, " + user)
        font = greetingMsg.font()
        font.setPointSize(28)
        greetingMsg.setFont(font)
        greetingMsg.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        # Create layouts to use later
        pageLayout = QVBoxLayout()
        buttonLayout = QHBoxLayout()
        
        # Create Biology button
        btn = QPushButton("Biology")
        btnSize = QSize(200,200)
        btn.setFixedSize(btnSize)
        buttonLayout.addWidget(btn)
        
        # Create Psychology button
        btn = QPushButton("Psychology")
        btnSize = QSize(200,200)
        btn.setFixedSize(btnSize)
        buttonLayout.addWidget(btn)
        
        #Organize elements
        pageLayout.addWidget(appName)
        pageLayout.addWidget(greetingMsg)
        pageLayout.addLayout(buttonLayout)
        container = QWidget()
        container.setLayout(pageLayout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

