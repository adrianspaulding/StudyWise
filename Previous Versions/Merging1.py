import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QWidget,
    QMessageBox
)

# Create a class for the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("StudyWise")

        appName = QLabel("StudyWise")
        font = appName.font()
        font.setPointSize(60)
        appName.setFont(font)
        appName.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        pageLayout = QVBoxLayout()
        buttonLayout = QHBoxLayout()

        btn_biology = QPushButton("Biology")
        btn_biology.setFixedSize(200, 200)
        btn_biology.clicked.connect(self.show_biology_sets)
        buttonLayout.addWidget(btn_biology)

        btn_psychology = QPushButton("Psychology")
        btn_psychology.setFixedSize(200, 200)
        btn_psychology.clicked.connect(self.show_psychology_sets)
        buttonLayout.addWidget(btn_psychology)

        pageLayout.addWidget(appName)
        pageLayout.addLayout(buttonLayout)

        container = QWidget()
        container.setLayout(pageLayout)
        self.setCentralWidget(container)

    def show_biology_sets(self):
        # Implement logic to show biology sets window
        # This currently calls it but the window doesn't stay open ~AS
        app = QApplication.instance()
        window = BioSetWindow()
        window.show()

    def show_psychology_sets(self):
        # Implement logic to show psychology sets window
        pass

# Create a class for the Biology Sets window
class BioSetWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Biology Focused Sets")

        screenName = QLabel("Biology Study Sets")
        font = screenName.font()
        font.setPointSize(50)
        screenName.setFont(font)
        screenName.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        titleName = QLabel("Unit Sections")
        font = titleName.font()
        font.setPointSize(38)
        titleName.setFont(font)
        titleName.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        pageLayout = QVBoxLayout()
        buttonLayout = QGridLayout()

        buttonLayout.addWidget(QPushButton("Unit 1: Bio Foundations"), 0, 1)
        buttonLayout.addWidget(QPushButton("Unit 2: Intro to Cells"), 1, 1)
        buttonLayout.addWidget(QPushButton("Unit 3: Cell Reproduction"), 2, 1)
        buttonLayout.addWidget(QPushButton("Unit 4: Basic Genetics"), 3, 1)

        pageLayout.addWidget(screenName)
        pageLayout.addWidget(titleName)
        pageLayout.addLayout(buttonLayout)
        container = QWidget()
        container.setLayout(pageLayout)

        self.setCentralWidget(container)

# Create a class for the Score Screen
class ScoreScreen(QWidget):
    def __init__(self):
        super().__init__()

        scoreLayout = QVBoxLayout()

        scoreLabel = QLabel("Score")
        font = scoreLabel.font()
        font.setPointSize(60)
        scoreLabel.setFont(font)
        scoreLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        yourScoreLabel = QLabel("Your Score: 8/10")  # You can update the score dynamically
        font = yourScoreLabel.font()
        font.setPointSize(36)
        yourScoreLabel.setFont(font)
        yourScoreLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        statsLabel = QLabel("Stats: 8/10")  # You can update the stats dynamically
        font = statsLabel.font()
        font.setPointSize(28)
        statsLabel.setFont(font)
        statsLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        returnButton = QPushButton("Return")
        returnButton.setFixedSize(QSize(200, 60))
        returnButton.clicked.connect(self.return_to_main_screen)

        scoreLayout.addWidget(scoreLabel)
        scoreLayout.addWidget(yourScoreLabel)
        scoreLayout.addWidget(statsLabel)
        scoreLayout.addWidget(returnButton)

        self.setLayout(scoreLayout)

    def return_to_main_screen(self):
        # Implement the logic to return to the main screen here
        pass

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
