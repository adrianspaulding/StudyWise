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

        buttons = [
            QPushButton("Unit 1: Basic Anatomy", clicked=self.unit1_clicked),
            QPushButton("Unit 2: Cells", clicked=self.unit2_clicked),
            QPushButton("Unit 3: Botany", clicked=self.unit3_clicked),
            QPushButton("Unit 4: Basic Genetics", clicked=self.unit4_clicked),
        ]

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

    def unit1_clicked(self):
        print("Unit 1 button clicked!")
        self.read_and_display_content("Anatomy.txt")

    def unit2_clicked(self):
        print("Unit 2 button clicked!")
        self.read_and_display_content("Cell Biology.txt")

    def unit3_clicked(self):
        print("Unit 3 button clicked!")
        self.read_and_display_content("Botany.txt")

    def unit4_clicked(self):
        print("Unit 4 button clicked!")
        self.read_and_display_content("Genetics.txt")

    def read_and_display_content(self, file_name):
        try:
            file_path = os.path.join(os.path.dirname(__file__), file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.readlines()

            # Assuming the content is in the format "term:definition"
            for line in content:
                term, definition = line.strip().split(':')
                print(f"Term: {term}, Definition: {definition}")

            # You can modify this logic to display the content in your GUI instead of printing
        except FileNotFoundError:
            print(f"File {file_name} not found.")

app = QApplication(sys.argv)
window = BioSetWindow()
window.show()
app.exec()

