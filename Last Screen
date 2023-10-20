import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QWidget
)

# Create Score Screen
class ScoreScreen(QWidget):
    def __init__(self):
        super().__init__()

        # Create Score Screen layout
        scoreLayout = QVBoxLayout()

        # Create Score Label
        scoreLabel = QLabel("Score")
        font = scoreLabel.font()
        font.setPointSize(60)
        scoreLabel.setFont(font)
        scoreLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # Create Your Score Label
        yourScoreLabel = QLabel("Your Score: 8/10")  # You can update the score dynamically
        font = yourScoreLabel.font()
        font.setPointSize(36)
        yourScoreLabel.setFont(font)
        yourScoreLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # Create Stats Label
        statsLabel = QLabel("Stats: 8/10")  # You can update the stats dynamically
        font = statsLabel.font()
        font.setPointSize(28)
        statsLabel.setFont(font)
        statsLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # Create Return Button
        returnButton = QPushButton("Return")
        returnButton.setFixedSize(QSize(200, 60))

        # Connect the button click event to a function (e.g., to return to the main screen)
        returnButton.clicked.connect(self.return_to_main_screen)

        # Add elements to the score layout
        scoreLayout.addWidget(scoreLabel)
        scoreLayout.addWidget(yourScoreLabel)
        scoreLayout.addWidget(statsLabel)
        scoreLayout.addWidget(returnButton)

        # Set the layout for the Score Screen
        self.setLayout(scoreLayout)

    def return_to_main_screen(self):
        # Implement the logic to return to the main screen here
        print("Returning to the main screen")  # You can replace this with your actual logic


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

        # Create layouts to use later
        pageLayout = QVBoxLayout()
        buttonLayout = QHBoxLayout()

        # Create Biology button
        btn = QPushButton("Biology")
        btnSize = QSize(200, 200)
        btn.setFixedSize(btnSize)
        buttonLayout.addWidget(btn)

        # Create Psychology button
        btn = QPushButton("Psychology")
        btnSize = QSize(200, 200)
        btn.setFixedSize(btnSize)
        buttonLayout.addWidget(btn)

        # Add buttons layout to the page layout
        pageLayout.addWidget(appName)
        pageLayout.addLayout(buttonLayout)

        # Set the central widget of the Window to the Greeting Screen
        container = QWidget()
        container.setLayout(pageLayout)
        self.setCentralWidget(container)

        # Initialize Score Screen (hidden by default)
        self.score_screen = ScoreScreen()
        self.score_screen.setVisible(False)
        self.setFixedSize(800, 600)  # Adjust the window size as needed

        # Create a button to switch to the Score Screen
        show_score_button = QPushButton("Show Score")
        show_score_button.clicked.connect(self.show_score)
        buttonLayout.addWidget(show_score_button)

    def show_score(self):
        # Show the Score Screen and hide the main screen
        self.score_screen.setVisible(True)
        self.centralWidget().setVisible(False)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
