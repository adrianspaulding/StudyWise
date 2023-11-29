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
from PySide6.QtGui import QFont

import sys
import os

#Class for the screen
class BioSetWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Biology Focused Sets")
        self.init_ui()

    def init_ui(self):
        self.create_labels()
        self.create_buttons()
        self.create_layout()

    def create_labels(self):
        screen_name = QLabel("Biology Study Sets")
        screen_name.setFont(QFont("Arial", 50))
        screen_name.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        title_name = QLabel("Unit Sections")
        title_name.setFont(QFont("Arial", 38))
        title_name.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.screen_name = screen_name
        self.title_name = title_name

    def create_buttons(self):
        button_layout = QGridLayout()
        #creates each button
        buttons = [
            QPushButton("Unit 1: Basic Anatomy", clicked=self.unit1_clicked),
            QPushButton("Unit 2: Cell Biology", clicked=self.unit2_clicked),
            QPushButton("Unit 3: Botany", clicked=self.unit3_clicked),
            QPushButton("Unit 4: Basic Genetics", clicked=self.unit4_clicked),
        ]
        #adds a consistent button layout
        for row, button in enumerate(buttons):
            button_layout.addWidget(button, row, 1)

        self.buttons = button_layout

    def create_layout(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.screen_name)
        main_layout.addWidget(self.title_name)
        main_layout.addLayout(self.buttons)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    #calls read_and_display for each button 
    def unit1_clicked(self):
        #print("Unit 1 button clicked!")
        self.read_and_display_content("Anatomy.txt")

    def unit2_clicked(self):
        #print("Unit 2 button clicked!")
        self.read_and_display_content("Cell Biology.txt")

    def unit3_clicked(self):
        #print("Unit 3 button clicked!")
        self.read_and_display_content("Botany.txt")

    def unit4_clicked(self):
        #print("Unit 4 button clicked!")
        self.read_and_display_content("Genetics.txt")

    def read_and_display_content(self, file_name):
        term_list = []
        definition_list = []
        try:
            #reads the file line by line
            file_path = os.path.join(os.path.dirname(__file__), file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.readlines()

            #Puts each line into lists
            for line in content:
                #splits term and definition
                term, definition = line.strip().split(':')
                term_list.append(term)
                definition_list.append(definition)

            print(term_list)
            print(definition_list)
            return term_list, definition_list
        
        #if something goes completely wrong
        except FileNotFoundError:
            print(f"File {file_name} not found.")

app = QApplication(sys.argv)
window = BioSetWindow()
window.show()
app.exec()
