import sys
import random
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QThread, pyqtSignal

class RandomThread(QThread):
    valueChanged = pyqtSignal(int)

    def run(self):
        while True:
            value = random.randint(0, 6)
            self.valueChanged.emit(value)
            # Sleep for 2 seconds
            self.msleep(2000)

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel('Random Value: -')
        layout.addWidget(self.label)

        self.startButton = QPushButton('Start Thread')
        self.startButton.clicked.connect(self.startThread)
        layout.addWidget(self.startButton)

        self.stopButton = QPushButton('Stop Thread')
        self.stopButton.clicked.connect(self.stopThread)
        layout.addWidget(self.stopButton)

        self.setLayout(layout)

        self.random_thread = RandomThread()
        self.random_thread.valueChanged.connect(self.updateLabel)

    def startThread(self):
        self.random_thread.start()

    def stopThread(self):
        self.random_thread.terminate()

    def updateLabel(self, value):
        self.label.setText(f'Random Value: {value}')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Main Window')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.popupButton = QPushButton('Popup Dialog')
        self.popupButton.clicked.connect(self.showDialog)
        layout.addWidget(self.popupButton)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def showDialog(self):
        dialog = MyDialog()
        dialog.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
