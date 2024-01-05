import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap, QPainter, QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class ImageButton(QPushButton):
    def __init__(self, image_path):
        super().__init__()
        self.image_path = image_path
        # self.setFixedSize(100, 100)  # Set an initial size, adjust as needed
        # self.setStyleSheet("background-color: transparent; border: none;")
        self.update_background()

    def update_background(self):
        pixmap = QPixmap(self.image_path)
        pixmap = pixmap.scaled(self.size() - QSize(20, 20), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        qicon = QIcon(pixmap)
        self.setIcon(qicon)
        self.setIconSize(self.size() - QSize(20, 20))

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_background()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        image_button = ImageButton("qrcode.png")
        layout.addWidget(image_button)
        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setGeometry(100, 100, 300, 200)
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
