#Importing needed components 
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
     QApplication,
     QMainWindow,
     QPushButton,
     QLabel,
     QVBoxLayout,
     QHBoxLayout,
     QStackedLayout,
     QGridLayout,
     QWidget
 )

import sys

# Create the BioSet Window
class BioSetWindow (QMainWindow):
    def __init__(self):
        super().__init__()

        #Setting window title 
        self.setWindowTitle("Biology Focused Sets")

        #Create screen title(display)
        screenName = QLabel("Biology Study Sets")
        font = screenName.font()
        font.setPointSize(50)
        screenName.setFont(font)
        screenName.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        #Create list title
        titleName = QLabel("Unit Sections")
        font = titleName.font()
        font.setPointSize(38)
        titleName.setFont(font)
        titleName.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        #Layouts
        pageLayout = QVBoxLayout()
        buttonLayout = QGridLayout()


        #Create List Button 1
        buttonLayout.addWidget(QPushButton("Unit 1: Bio Foundations"), 0, 1)


        #Create List Button 2
        buttonLayout.addWidget(QPushButton("Unit 2: Intro to Cells"), 1, 1)


        #Create List Button 3
        buttonLayout.addWidget(QPushButton("Unit 3: Cell Reproduction"), 2, 1)


        #Create List Button 4 
        buttonLayout.addWidget(QPushButton("Unit 4: Basic Genetics"), 3, 1)


        #Can add more sets later on if needed

        #Set Widgets
        pageLayout.addWidget(screenName)
        pageLayout.addWidget(titleName)
        pageLayout.addLayout(buttonLayout)
        container = QWidget()
        container.setLayout(pageLayout)

        
        # Set the central widget of the Window.
        self.setCentralWidget(container)

app = QApplication(sys.argv)

window = BioSetWindow()
window.show()

app.exec()
