import sys
import os
import random

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
        | Psy Screen |
         --------------
        """
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
        Button6.move(250,450
        self.screenList.addWidget(PsyScreencontainer)
        
        
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
        
        # variable to keep track of number of answers answered correctly
        self.numberCorrect = 0

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
        
        #NEEDS ACTUAL QUESTIONS AND ANSWERS
        questions = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25"]
        answers = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25"]
        
        doneQuestions = []  #list to append so questions aren't reused
        
        # Question display
        firstQuestion = random.choice(questions)
        doneQuestions.append(firstQuestion)
        self.question = QLabel(firstQuestion)
        font = self.question.font()
        font.setPointSize(22)
        self.question.setFont(font)
        self.question.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        

        # Updates the question to show which button was selected. Progress updates inside question update
        def updateQuestion(selected,question):
            if self.questionsAnswered < self.numberOfQuestions:
                self.questionsAnswered += 1
                if (answers.index(selected) == questions.index(question)):
                    self.numberCorrect += 1
                updateNumber()
                newQuestion = random.choice(questions)
                while newQuestion in doneQuestions:
                    newQuestion = random.choice(questions)
                doneQuestions.append(newQuestion)
                self.question.setText(newQuestion)
                updateAnswers(newQuestion)
            #NEED TO GO TO SCORE SCREEN
            #numberCorrect kept track of the score 
            else:
                self.question.setText(f"Max reached. Will go to next screen. Correct: {self.numberCorrect}")
            
        def updateNumber():
            newNumber = f"Progress: {self.questionsAnswered}/{self.numberOfQuestions}"
            self.numberDisplay.setText(newNumber)
            
        #Updates the text in the answer buttons
        #Currently does not account for answers being the same
        def updateAnswers(matchingQuestion):
            correctAnswer = random.randint(1,4)
            if correctAnswer == 1:
                self.btnA.setText(answers[questions.index(matchingQuestion)])
                self.btnB.setText(random.choice(answers))
                self.btnC.setText(random.choice(answers))
                self.btnD.setText(random.choice(answers))
            if correctAnswer == 2:
                self.btnA.setText(random.choice(answers))
                self.btnB.setText(answers[questions.index(matchingQuestion)])
                self.btnC.setText(random.choice(answers))
                self.btnD.setText(random.choice(answers))
            if correctAnswer == 3:
                self.btnA.setText(random.choice(answers))
                self.btnB.setText(random.choice(answers))
                self.btnC.setText(answers[questions.index(matchingQuestion)])
                self.btnD.setText(random.choice(answers))
            if correctAnswer == 4:
                self.btnA.setText(random.choice(answers))
                self.btnB.setText(random.choice(answers))
                self.btnC.setText(random.choice(answers))
                self.btnD.setText(answers[questions.index(matchingQuestion)])
            
        # Create option A
        self.btnA = QPushButton()
        self.btnA.setFixedSize(200, 200)
        topButtonsLayout.addWidget(self.btnA)
        
        # Create option B
        self.btnB = QPushButton()
        self.btnB.setFixedSize(200, 200)
        topButtonsLayout.addWidget(self.btnB)
        
        # Create option C
        self.btnC = QPushButton()
        self.btnC.setFixedSize(200, 200)
        bottomButtonsLayout.addWidget(self.btnC)
        
        # Create option D
        self.btnD = QPushButton()
        self.btnD.setFixedSize(200, 200)
        bottomButtonsLayout.addWidget(self.btnD)
        
        updateAnswers(self.question.text())

        # Button clicked events
        self.btnA.clicked.connect(lambda: updateQuestion(self.btnA.text(),self.question.text()))
        self.btnB.clicked.connect(lambda: updateQuestion(self.btnB.text(),self.question.text()))
        self.btnC.clicked.connect(lambda: updateQuestion(self.btnC.text(),self.question.text()))
        self.btnD.clicked.connect(lambda: updateQuestion(self.btnD.text(),self.question.text()))  
        
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
