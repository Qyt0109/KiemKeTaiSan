import typing
# PyQt6
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QFrame,
    QWidget,
    QLabel
)
from PyQt6.QtGui import QPixmap, QIcon

# Modules
from Frontend.Design.design_ui import Ui_MainWindow

# Paths
icon_search_path = "Frontend/Resources/Bootstrap/search.png"
icon_options_path = "Frontend/Resources/Bootstrap/sliders.png"
icon_home_path = "Frontend/Resources/Bootstrap/house-fill.png"
icon_back_path = "Frontend/Resources/Bootstrap/arrow-left.png"

# Main App class
class MyApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set up the user interface from Designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_icons()

        # Extended design and setup for ui
        self.toPageLogin()  # Started at login page

        # Connect signals and slots
        self.ui.pushButton_Login.clicked.connect(self.login)
        self.ui.pushButton_Rooms.clicked.connect(self.toPageRooms)
        self.ui.pushButton_Check.clicked.connect(self.toPageCheck)
        self.ui.pushButton_Home.clicked.connect(self.toPageMainMenu)

        # Test
        self.ui.pushButton_Test.clicked.connect(self.toPageTest)
        self.ui.pushButton_Test0.clicked.connect(self.test0)
        self.ui.pushButton_Test1.clicked.connect(self.test1)
        self.ui.pushButton_Test2.clicked.connect(self.test2)

    # Icons
    def init_icons(self):
        self.ui.pushButton_RoomSearch.setIcon(QIcon(QPixmap(icon_search_path)))
        self.ui.pushButton_RoomSearchOptions.setIcon(QIcon(QPixmap(icon_options_path)))
        self.ui.pushButton_Home.setIcon(QIcon(QPixmap(icon_home_path)))
        self.ui.pushButton_Back.setIcon(QIcon(QPixmap(icon_back_path)))

    # Define functions
    def login(self):
        if self.ui.lineEdit_Username.text() == "admin" and self.ui.lineEdit_Password.text() == "admin":
            print("Logged in!")
            self.toPageMainMenu()
        # Bypass login for developing
        else:
            self.toPageMainMenu()

    def toPageLogin(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_Login)

    def toPageMainMenu(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_MainMenu)
    
    def toPageRooms(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_Rooms)

    def toPageCheck(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_Rooms)

    # Test
    def toPageTest(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_Test)

    def test0(self):
        clearAllWidgets(self.ui.frame_ScrollAreaTest)

    def test1(self):
        layout = self.ui.frame_ScrollAreaTest.layout()
        button = QPushButton(text=f"{layout.count()}")
        button.clicked.connect(lambda: self.myPrint(text=f"Button {button.objectName()} clicked!"))
        layout.addWidget(button)

    def test2(self):
        parent = self.ui.frame_ScrollAreaTest
        frame_Khu = makeKhuFrame(parent)
        layout = self.ui.frame_ScrollAreaTest.layout()
        layout.addWidget(frame_Khu)

    def myPrint(self, text):
        print(text)


def makeKhuFrame(parent):
    # frame_Khu
    frame_Khu = QFrame(parent=parent)
    frame_Khu.setFrameShape(QFrame.Shape.StyledPanel)   # Optional
    frame_Khu.setFrameShadow(QFrame.Shadow.Raised) # Optional
    # Layout for frame_Khu
    verticalLayout_Khu = QVBoxLayout(frame_Khu)
    # label for frame_Khu
    label_TenKhu = QLabel(parent=frame_Khu)
    label_TenKhu.setText("Tên khu")
    verticalLayout_Khu.addWidget(label_TenKhu)
    # frame_PhongKhu
    frame_PhongKhu = QFrame(parent=frame_Khu)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(frame_PhongKhu.sizePolicy().hasHeightForWidth())
    frame_PhongKhu.setSizePolicy(sizePolicy)
    frame_PhongKhu.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    frame_PhongKhu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    verticalLayout_Khu.addWidget(frame_PhongKhu)
    # gridLayout for Phongs in Khu
    gridLayout_Phong = QGridLayout(frame_PhongKhu)
    # Define the number of rows and columns
    rows = 2
    columns = 5
    for i in range(6):
        pushButton_Phong = QPushButton(parent=frame_PhongKhu)
        pushButton_Phong.setText(f"Phòng {i}")
        # Calculate the row and column positions based on the index
        row_position = i // columns
        column_position = i % columns
        gridLayout_Phong.addWidget(pushButton_Phong, row_position, column_position, 1, 1)
    
    return frame_Khu

    

def clearAllWidgets(widget):
    layout = widget.layout()
    if layout:
        while layout.count():
            w = layout.takeAt(0).widget()
            if w:
                w.deleteLater()

if __name__ == "__main__":
    app = QApplication([])
    window = MyApplication()
    window.show()
    app.exec()
