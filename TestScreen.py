import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QMessageBox
)

#Practice Test Window
class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("StudyWise")
        self.resize(500,400)

        # variable that is set through pop-up window
        self.numberOfQuestions = -1   #-1 allows it to not be 0=0 in if statement
        
        # variable to keep track of number of questions answered
        self.questionsAnswered = 0

        # Create layouts 
        pageLayout = QVBoxLayout()
        topButtonsLayout = QHBoxLayout()
        bottomButtonsLayout = QHBoxLayout()
        
        # Practice test display
        mainText = QLabel("Practice Test")
        font = mainText.font()
        font.setPointSize(12)
        mainText.setFont(font)
        mainText.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        # Display the number of questions chosen
        self.numberDisplay = QLabel("Number of Questions: ")
        font = self.numberDisplay.font()
        font.setPointSize(15)
        self.numberDisplay.setFont(font)
        self.numberDisplay.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        # Question display
        # Need to make a list of questions and answers that this will chose from
        self.question = QLabel("Question Placeholder")
        font = self.question.font()
        font.setPointSize(22)
        self.question.setFont(font)
        self.question.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        #Updates the question to show which button was selected. Progress updates inside question update
        #Will be changed in the future to incorporate the previously mentioned list
        def updateQuestion(selected):
            self.questionsAnswered += 1
            if self.questionsAnswered <= self.numberOfQuestions:
                updateNumber()
                newQuestion = f"Selected: {selected}"
                self.question.setText(newQuestion)
            else:
                self.question.setText("Max reached. Will go to next screen")
            
        def updateNumber():
            newNumber = f"Progress: {self.questionsAnswered}/{self.numberOfQuestions}"
            self.numberDisplay.setText(newNumber)
        
        # Create option A
        btnA = QPushButton("A")
        btnA.setFixedSize(200, 200)
        topButtonsLayout.addWidget(btnA)
        
        # Create option B
        btnB = QPushButton("B")
        btnB.setFixedSize(200, 200)
        topButtonsLayout.addWidget(btnB)
        
        # Create option C
        btnC = QPushButton("C")
        btnC.setFixedSize(200, 200)
        bottomButtonsLayout.addWidget(btnC)
        
        # Create option D
        btnD = QPushButton("D")
        btnD.setFixedSize(200, 200)
        bottomButtonsLayout.addWidget(btnD)

        # Button clicked events
        btnA.clicked.connect(lambda: updateQuestion("A"))
        btnB.clicked.connect(lambda: updateQuestion("B"))
        btnC.clicked.connect(lambda: updateQuestion("C"))
        btnD.clicked.connect(lambda: updateQuestion("D"))  
        
        # Organize elements
        pageLayout.addWidget(mainText)
        pageLayout.addWidget(self.numberDisplay)
        pageLayout.addWidget(self.question)
        pageLayout.addLayout(topButtonsLayout)
        pageLayout.addLayout(bottomButtonsLayout)
        container = QWidget()
        container.setLayout(pageLayout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

        #Shows the pop-up on start
        self.initialPopUp()

    #A pop-up to ask how many questions the user would like
    #This will potentially need to be changed if we entertain the idea of a timer
    def initialPopUp(self):
        msg = QMessageBox()
        msg.setWindowTitle("Practice Test")
        msg.setText("How many questions would you like in your practice test?")
        
        fiveButton = QPushButton("5")
        tenButton = QPushButton("10")
        fifteenButton = QPushButton("15")
        twentyButton = QPushButton("20")

        msg.addButton(fiveButton, QMessageBox.AcceptRole)
        msg.addButton(tenButton, QMessageBox.AcceptRole)
        msg.addButton(fifteenButton, QMessageBox.AcceptRole)
        msg.addButton(twentyButton, QMessageBox.AcceptRole)
        
        result = msg.exec()
        
        if msg.clickedButton() == fiveButton:
            self.numberOfQuestions = 5
        elif msg.clickedButton() == tenButton:
            self.numberOfQuestions = 10
        elif msg.clickedButton() == fifteenButton:
            self.numberOfQuestions = 15
        elif msg.clickedButton() == twentyButton:
            self.numberOfQuestions = 20

        #Changes the numberDisplay in the main TestWindow  (this is only for 0/number selected)
        self.numberDisplay.setText(f"Progress: {self.questionsAnswered}/{self.numberOfQuestions}")

app = QApplication(sys.argv)

window = TestWindow()
window.show()

app.exec()
