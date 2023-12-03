import sys
import os
import random

from PySide6.QtGui import QPixmap
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
        
#Creates application that will hold all the screens       
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #Set fixed window size
        self.setMinimumSize(640, 575)
        self.setMaximumSize(640, 575)
        
        #Set window title to StudyWise
        self.setWindowTitle("StudyWise")
        
        #Initializing variables to be used in the test screen. Need to be in main for multiple function usage
        self.numberOfQuestions = 0  
        #NEEDS ACTUAL QUESTIONS AND ANSWERS
        self.questions = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25"]
        self.answers = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25"]
        
        #Creating a StackedLayout for all the screens to go in
        self.screenList = QStackedLayout()
        
        #Create and add each screen to screenList
        self.screenList.addWidget(self.createGreetingScreen())  #Index 0
        self.screenList.addWidget(self.createBioScreen())       #Index 1
        self.screenList.addWidget(self.createPsychScreen())     #Index 2
        self.screenList.addWidget(self.createTestScreen())      #Index 3
        self.screenList.addWidget(self.createScoreScreen())     #Index 4
        
        central_widget = QWidget()
        central_widget.setLayout(self.screenList)
        self.setCentralWidget(central_widget)
        
        self.showScreen(0)  #Shows the greeting screen on start-up
        
    def showScreen(self, index):  #Function to update which screen is showing
        self.screenList.setCurrentIndex(index)
        
    #Greeting Screen
    def createGreetingScreen(self):
        #Sets username based on name in os
        username = os.getlogin()
        
        # Create app title with image
        appImageLabel = QLabel()
        pixmap = QPixmap("StudyWiseSelectLogo.png")
        pixmap.setDevicePixelRatio(1.2)
        appImageLabel.setPixmap(pixmap)
        appImageLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        # Create greeting message
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
        bioButton.pressed.connect(lambda: self.showScreen(1))
        buttonLayout.addWidget(bioButton)
        
        # Create Psychology button
        psychButton = QPushButton("Psychology")
        btnSize = QSize(200, 200)
        psychButton.setFixedSize(btnSize)
        psychButton.pressed.connect(lambda: self.showScreen(2))
        buttonLayout.addWidget(psychButton)
        
        # Organize elements
        pageLayout.addWidget(appImageLabel)
        pageLayout.addWidget(greetingMsg)
        pageLayout.addLayout(buttonLayout)
        
        greetingScreenContainer = QWidget()
        greetingScreenContainer.setLayout(pageLayout)
            
        return greetingScreenContainer
    
    #Biology Screen
    def createBioScreen(self):
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
        bioUnit1Button = QPushButton("Unit 1: Basic Anatomy")
        bioUnit1Button.pressed.connect(lambda: self.buttonClicked("Anatomy.txt"))
        bioUnit2Button = QPushButton("Unit 2: Cell Biology")
        bioUnit2Button.pressed.connect(lambda: self.buttonClicked("Cell Biology.txt"))
        bioUnit3Button = QPushButton("Unit 3: Botany")
        bioUnit3Button.pressed.connect(lambda: self.buttonClicked("Botany.txt"))
        bioUnit4Button = QPushButton("Unit 4: Basic Genetics")
        bioUnit4Button.pressed.connect(lambda: self.buttonClicked("Genetics.txt"))
        
        # Add buttons to layout
        buttonLayout.addWidget(bioUnit1Button, 0, 1)
        buttonLayout.addWidget(bioUnit2Button, 1, 1)
        buttonLayout.addWidget(bioUnit3Button, 2, 1)
        buttonLayout.addWidget(bioUnit4Button, 3, 1)
        
        # Add elements to page layout
        pageLayout.addWidget(screenName)
        pageLayout.addWidget(titleName)
        pageLayout.addLayout(buttonLayout)
        bioScreenContainer = QWidget()
        bioScreenContainer.setLayout(pageLayout)

        return bioScreenContainer
    
    #Psychology Screen
    def createPsychScreen(self):
        # Create screen header
        screenName = QLabel("Psychology Study Sets")
        font = screenName.font()
        font.setPointSize(40)
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
        psychUnit1Button = QPushButton("Unit 1: Scientific Foundations")
        psychUnit1Button.pressed.connect(lambda: self.buttonClicked("Scientific Foundations.txt"))
        psychUnit2Button = QPushButton("Unit 2: Social/Cognitive Aspects")
        psychUnit2Button.pressed.connect(lambda: self.buttonClicked("SocialAndCognitiveAspects.txt"))
        psychUnit3Button = QPushButton("Unit 3: Biological Bases of Behavior")
        psychUnit3Button.pressed.connect(lambda: self.buttonClicked("BiologicalBasesofBehavior.txt"))
        
        # Add buttons to layout
        buttonLayout.addWidget(psychUnit1Button, 0, 1)
        buttonLayout.addWidget(psychUnit2Button, 1, 1)
        buttonLayout.addWidget(psychUnit3Button, 2, 1)

        # Add elements to page layout
        pageLayout.addWidget(screenName)
        pageLayout.addWidget(titleName)
        pageLayout.addLayout(buttonLayout)
        psychScreenContainer = QWidget()
        psychScreenContainer.setLayout(pageLayout)
          
        return psychScreenContainer
    
    #Pop-up window asking for the amount of questions before the test screen
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
            
        self.resetStats()   #Reset variables to zero or empty to allow for reruns of the test screen
        self.updateNumber() #Display the correct text in the "progress" of the test screen
        
        #Create new test screen to refresh questions
        newTestScreen = self.createTestScreen()
        self.screenList.setCurrentIndex(3)
        self.screenList.removeWidget(self.screenList.currentWidget())
        self.screenList.insertWidget(3, newTestScreen)
        
        #Change to test screen
        self.showScreen(3)
        
    #Resets variables to zero for multiple reruns
    def resetStats(self):
        self.doneQuestions = []  #list to append so questions aren't reused
        self.questionsAnswered = 0
        self.numberCorrect = 0
        
    #Test Screen
    def createTestScreen(self):
        self.resetStats()

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
        self.numberDisplay = QLabel(f"Progress: {self.questionsAnswered}/{self.numberOfQuestions}")
        font = self.numberDisplay.font()
        font.setPointSize(15)
        self.numberDisplay.setFont(font)
        self.numberDisplay.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # Question display
        firstQuestion = random.choice(self.questions)  #The first question will always be an available question
        self.doneQuestions.append(firstQuestion)
        self.question = QLabel(firstQuestion)
        font = self.question.font()
        font.setPointSize(22)
        self.question.setFont(font)
        self.question.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
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

        # Connect button click events
        self.btnA.clicked.connect(lambda: self.handleButtons(self.btnA))
        self.btnB.clicked.connect(lambda: self.handleButtons(self.btnB))
        self.btnC.clicked.connect(lambda: self.handleButtons(self.btnC))
        self.btnD.clicked.connect(lambda: self.handleButtons(self.btnD))

        #Updates the answers displayed in the buttons 
        self.updateAnswers(self.question.text())
        
        # Organize elements
        pageLayout.addWidget(mainText)
        pageLayout.addWidget(self.numberDisplay)
        pageLayout.addWidget(self.question)
        pageLayout.addLayout(topButtonsLayout)
        pageLayout.addLayout(bottomButtonsLayout)
        testScreenContainer = QWidget()
        testScreenContainer.setLayout(pageLayout)
        
        return testScreenContainer
    
    #Score Screen
    def createScoreScreen(self):
        # Create screen header
        scoreLabel = QLabel("Score")
        font = scoreLabel.font()
        font.setPointSize(60)
        scoreLabel.setFont(font)
        scoreLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # Create label to display score
        self.yourScoreLabel = QLabel(f"Score: {self.numberCorrect}/{self.numberOfQuestions}")
        font=self.yourScoreLabel.font()
        font.setPointSize(36)
        self.yourScoreLabel.setFont(font)
        self.yourScoreLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        #Create button to return back to greeting screen
        returnButton = QPushButton("Return")
        returnButton.setFixedSize(QSize(200, 60))
        returnButton.clicked.connect(lambda: self.showScreen(0))

        #layout
        scoreLayout = QVBoxLayout()
        scoreLayout.addWidget(scoreLabel)
        scoreLayout.addWidget(self.yourScoreLabel)
        scoreLayout.addWidget(returnButton)

        #ensures button is centered
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addStretch(1)
        horizontal_layout.addLayout(scoreLayout)
        horizontal_layout.addStretch(1)

        scoreScreenContainer = QWidget()
        scoreScreenContainer.setLayout(horizontal_layout)

        return scoreScreenContainer
        
    #Handles what to call when the answer buttons in test screen are pressed
    def handleButtons(self, button):
        #Sends the index of the selected answer and index of the displayed question into updateQuestion()
        self.updateQuestion(self.answers.index(button.text()), self.questions.index(self.question.text())) 
        if (self.questionsAnswered + 1) > self.numberOfQuestions:
            self.showScreen(4)  #goes to score screen

    #Updates the text of the question displayed
    def updateQuestion(self, answerIndex, questionIndex):
        self.questionsAnswered += 1  #Increments the number of questions the user answered
        if answerIndex == questionIndex:  
            self.numberCorrect += 1  #Increments the number the user got correct
        newQuestion = random.choice(self.questions)  #Selects a new question from the list to display
        while newQuestion in self.doneQuestions:  #If the randomly chosen question has already been selected
            newQuestion = random.choice(self.questions)  #get a new one
        self.doneQuestions.append(newQuestion)  #append the doneQuestions list by that new question
        self.question.setText(newQuestion) #displays the new question
        self.updateAnswers(newQuestion)  #update the displayed answers based on the new question
        self.updateNumber()  #updates the displayed progress
        
        #Updates the score text in the score screen. Ensures the score is always up to date
        self.yourScoreLabel.setText(f"Score: {self.numberCorrect}/{self.numberOfQuestions}") 

    #Updates the progress display in the test screen
    def updateNumber(self):
        newNumber = f"Progress: {self.questionsAnswered}/{self.numberOfQuestions}"
        self.numberDisplay.setText(newNumber)

    #Updates the answers displayed in the buttons in the test screen
    def updateAnswers(self, matchingQuestion):
        self.doneAnswers = []  #creates an empty list to add done answers to, resets each round
        correctAnswer = random.randint(1, 4)  #Chooses which button will be the correct answer
        if correctAnswer == 1:
            self.a = self.answers[self.questions.index(matchingQuestion)]
            self.btnA.setText(self.a)
            self.doneAnswers.append(self.a)
            
            self.b = random.choice(self.answers)
            while self.b in self.doneAnswers:
                self.b = random.choice(self.answers)
            self.btnB.setText(self.b)
            self.doneAnswers.append(self.b)
            
            self.c = random.choice(self.answers)
            while self.c in self.doneAnswers:
                self.c = random.choice(self.answers)
            self.btnC.setText(self.c)
            self.doneAnswers.append(self.c)
            
            self.d = random.choice(self.answers)
            while self.d in self.doneAnswers:
                self.d = random.choice(self.answers)
            self.btnD.setText(self.d)
            self.doneAnswers.append(self.d)
            
        if correctAnswer == 2:
            self.b = self.answers[self.questions.index(matchingQuestion)]
            self.btnB.setText(self.b)
            self.doneAnswers.append(self.b)
            
            self.a = random.choice(self.answers)
            while self.a in self.doneAnswers:
                self.a = random.choice(self.answers)
            self.btnA.setText(self.a)
            self.doneAnswers.append(self.a)
            
            self.c = random.choice(self.answers)
            while self.c in self.doneAnswers:
                self.c = random.choice(self.answers)
            self.btnC.setText(self.c)
            self.doneAnswers.append(self.c)
            
            self.d = random.choice(self.answers)
            while self.d in self.doneAnswers:
                self.d = random.choice(self.answers)
            self.btnD.setText(self.d)
            self.doneAnswers.append(self.d)
            
        if correctAnswer == 3:
            
            self.c = self.answers[self.questions.index(matchingQuestion)]
            self.btnC.setText(self.c)
            self.doneAnswers.append(self.c)
            
            self.b = random.choice(self.answers)
            while self.b in self.doneAnswers:
                self.b = random.choice(self.answers)
            self.btnB.setText(self.b)
            self.doneAnswers.append(self.b)
            
            self.a = random.choice(self.answers)
            while self.a in self.doneAnswers:
                self.a = random.choice(self.answers)
            self.btnA.setText(self.a)
            self.doneAnswers.append(self.a)
            
            self.d = random.choice(self.answers)
            while self.d in self.doneAnswers:
                self.d = random.choice(self.answers)
            self.btnD.setText(self.d)
            self.doneAnswers.append(self.d)
            
        if correctAnswer == 4:
            
            self.d = self.answers[self.questions.index(matchingQuestion)]
            self.btnD.setText(self.d)
            self.doneAnswers.append(self.d)
            
            self.b = random.choice(self.answers)
            while self.b in self.doneAnswers:
                self.b = random.choice(self.answers)
            self.btnB.setText(self.b)
            self.doneAnswers.append(self.b)
            
            self.c = random.choice(self.answers)
            while self.c in self.doneAnswers:
                self.c = random.choice(self.answers)
            self.btnC.setText(self.c)
            self.doneAnswers.append(self.c)
            
            self.a = random.choice(self.answers)
            while self.a in self.doneAnswers:
                self.a = random.choice(self.answers)
            self.btnA.setText(self.a)
            self.doneAnswers.append(self.a)
      
    #Button clicking and question grabbing
    def buttonClicked(self, fileToRead):
        self.questions = []
        self.answers = []
        try:
            #reads the file line by line
            file_path = os.path.join(os.path.dirname(__file__), fileToRead)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.readlines()

            #Puts each line into lists
            for line in content:
                #splits term and definition
                term, definition = line.strip().split(':')
                self.questions.append(term)
                self.answers.append(definition)
        
        #if something goes completely wrong
        except FileNotFoundError:
            print(f"File {fileToRead} not found.")
        
        #Call initialPopUp to get number of questions
        self.initialPopUp()
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

