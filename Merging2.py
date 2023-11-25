import sys
import os

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QStackedLayout,
    QGridLayout,
    QWidget,
    QMessageBox
)

# Create Main Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Create and get name variable to store user's name
        username = os.getlogin()
        
        # Set min window size (could adjust to set size later)
        self.setMinimumWidth(640)
        self.setMinimumHeight(550)
        
        # Create stacked layout to add all screens into
        self.screenList = QStackedLayout()
        
        
        
        """
         -----------------
        | Greeting Screen |
         -----------------
        """
        
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
        greetingMsg = QLabel("Hello, " + username)
        font = greetingMsg.font()
        font.setPointSize(28)
        greetingMsg.setFont(font)
        greetingMsg.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        # Create layouts to use later
        pageLayout = QVBoxLayout()
        buttonLayout = QHBoxLayout()
        
        # Create Biology button
        bioButton = QPushButton("Biology")
        btnSize = QSize(200, 200)
        bioButton.setFixedSize(btnSize)
        bioButton.pressed.connect(self.showBioScreen)
        buttonLayout.addWidget(bioButton)
        
        # Create Psychology button
        psychButton = QPushButton("Psychology")
        btnSize = QSize(200, 200)
        psychButton.setFixedSize(btnSize)
        psychButton.pressed.connect(self.showBioScreen)
        buttonLayout.addWidget(psychButton)
        
        # Organize elements
        pageLayout.addWidget(appName)
        pageLayout.addWidget(greetingMsg)
        pageLayout.addLayout(buttonLayout)
        greetingScreenContainer = QWidget()
        greetingScreenContainer.setLayout(pageLayout)

        # Set the central widget of the Window
        self.setCentralWidget(greetingScreenContainer)
        
        # Add all to a screen list to allow for switching
        self.screenList.addWidget(greetingScreenContainer)
        
        
        """
         ----------------
        | Biology Screen |
         ----------------
        """
        
        # Set Window title
        self.setWindowTitle("Biology Focused Sets")

        # Create screen header
        screenName = QLabel("Biology Study Sets")
        font = screenName.font()
        font.setPointSize(50)
        screenName.setFont(font)
        screenName.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # Create section header
        titleName = QLabel("Unit Sections")
        font = titleName.font()
        font.setPointSize(38)
        titleName.setFont(font)
        titleName.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)


        # Create layouts
        pageLayout = QVBoxLayout()
        buttonLayout = QGridLayout()

        # Create buttons
        bioUnit1Button = QPushButton("Unit 1: Bio Foundations")
        bioUnit1Button.pressed.connect(self.initialPopUp)
        bioUnit2Button = QPushButton("Unit 2: Intro to Cells")
        bioUnit2Button.pressed.connect(self.initialPopUp)
        bioUnit3Button = QPushButton("Unit 3: Cell Reproduction")
        bioUnit3Button.pressed.connect(self.initialPopUp)
        bioUnit4Button = QPushButton("Unit 4: Basic Genetics")
        bioUnit4Button.pressed.connect(self.initialPopUp)
        
        # Add buttons to layout
        buttonLayout.addWidget(bioUnit1Button, 0, 1)
        buttonLayout.addWidget(bioUnit2Button, 1, 1)
        buttonLayout.addWidget(bioUnit3Button, 2, 1)
        buttonLayout.addWidget(bioUnit4Button, 3, 1)

        # Add elements to page layout
        pageLayout.addWidget(screenName)
        pageLayout.addWidget(titleName)
        pageLayout.addLayout(buttonLayout)
        bioScreencontainer = QWidget()
        bioScreencontainer.setLayout(pageLayout)

        # Set the central widget of the Window
        self.setCentralWidget(bioScreencontainer)
        
        # Add all to a screen list to allow for switching
        self.screenList.addWidget(bioScreencontainer)
        
        
        """
         --------------
        | Score Screen |
         --------------
        """
        # Create page layout
        scoreLayout = QVBoxLayout()

        # Create score label
        scoreLabel = QLabel("Score")
        font = scoreLabel.font()
        font.setPointSize(60)
        scoreLabel.setFont(font)
        scoreLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        # Create user score label
        yourScoreLabel = QLabel("Your Score: 8/10")  # You can update the score dynamically
        font = yourScoreLabel.font()
        font.setPointSize(36)
        yourScoreLabel.setFont(font)
        yourScoreLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # Create stats label
        statsLabel = QLabel("Stats: 8/10")  # You can update the stats dynamically
        font = statsLabel.font()
        font.setPointSize(28)
        statsLabel.setFont(font)
        statsLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # Create return button
        returnButton = QPushButton("Return")
        returnButton.setFixedSize(QSize(200, 60))
        returnButton.clicked.connect(self.showGreetingScreen)

        # Add widgets to layout
        scoreLayout.addWidget(scoreLabel)
        scoreLayout.addWidget(yourScoreLabel)
        scoreLayout.addWidget(statsLabel)
        scoreLayout.addWidget(returnButton)
        scoreScreenContainer = QWidget()
        scoreScreenContainer.setLayout(scoreLayout)
        
        # Add all to a screen list to allow for switching
        self.screenList.addWidget(scoreScreenContainer)
        
        
        """
         --------------
        | Test Screen |
         --------------
        """
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

        # Updates the question to show which button was selected. Progress updates inside question update
        # Will be changed in the future to incorporate the previously mentioned list
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
        testScreenContainer = QWidget()
        testScreenContainer.setLayout(pageLayout)

        # Set the central widget of the Window.
        self.setCentralWidget(testScreenContainer)
        
        # Add all to a screen list to allow for switching
        self.screenList.addWidget(testScreenContainer)

        

    # A pop-up to ask how many questions the user would like
    # This will potentially need to be changed if we entertain the idea of a timer
    def initialPopUp(self):
        # Create message box
        msg = QMessageBox()
        msg.setWindowTitle("Practice Test")
        msg.setText("How many questions would you like in your practice test?")
        
        #Create buttons
        fiveButton = QPushButton("5")
        tenButton = QPushButton("10")
        fifteenButton = QPushButton("15")
        twentyButton = QPushButton("20")

        # Add buttons to message box
        msg.addButton(fiveButton, QMessageBox.AcceptRole)
        msg.addButton(tenButton, QMessageBox.AcceptRole)
        msg.addButton(fifteenButton, QMessageBox.AcceptRole)
        msg.addButton(twentyButton, QMessageBox.AcceptRole)
        
        # Get result
        result = msg.exec()
        
        # Process result
        if msg.clickedButton() == fiveButton:
            self.numberOfQuestions = 5
        elif msg.clickedButton() == tenButton:
            self.numberOfQuestions = 10
        elif msg.clickedButton() == fifteenButton:
            self.numberOfQuestions = 15
        elif msg.clickedButton() == twentyButton:
            self.numberOfQuestions = 20

        # Changes the numberDisplay in the main TestWindow  (this is only for 0/number selected)
        self.numberDisplay.setText(f"Progress: {self.questionsAnswered}/{self.numberOfQuestions}")
        
        # Change to test screen
        self.showTestScreen()
        
        
    # Functions for changing screens
    def showGreetingScreen(self):
        self.screenList.setCurrentIndex(0)
        
    def showBioScreen(self):
        self.screenList.setCurrentIndex(1)
        
    def showPsychScreen(self):
        self.screenList.setCurrentIndex(2)
        
    def showTestScreen(self):
        self.screenList.setCurrentIndex(3)
        
    def showScoreScreen(self):
        self.screenList.setCurrentIndex(4)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()


