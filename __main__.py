import signal
import typing
# PyQt6
import PyQt6
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
    QLabel,
    QSpacerItem,
    QSizePolicy
)
from PyQt6.QtGui import (
    QPixmap,
    QIcon,
    QColor
)

""" Modules """
# UI
from Frontend.Design.design_ui import Ui_MainWindow
# Scanner
# from Backend.Services.Scanner.scanner import Scanner
from Backend.Services.Scanner.fake_scanner import Scanner # fake scanner for developing UI interface
# Models
from Backend.Models.models import *
# Database
from Backend.Database.db_sessions import *

""" Paths """
icon_search_path = "Frontend/Resources/Bootstrap/search.png"
icon_options_path = "Frontend/Resources/Bootstrap/sliders.png"
icon_home_path = "Frontend/Resources/Bootstrap/house-fill.png"
icon_back_path = "Frontend/Resources/Bootstrap/arrow-left.png"
icon_x_path = "Frontend/Resources/Bootstrap/x-lg.png"

class MyApplication(QMainWindow):
    """ Main App class """
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
        """
        button_increase.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(
            (self.stackedWidget.currentIndex() + 1) % self.stackedWidget.count()))

        button_decrease.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(
            (self.stackedWidget.currentIndex() - 1) % self.stackedWidget.count()))
        """
        self.ui.pushButton_ToLeft.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(
            (self.ui.stackedWidget.currentIndex() - 1) % self.ui.stackedWidget.count()
        ))
        self.ui.pushButton_ToRight.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(
            (self.ui.stackedWidget.currentIndex() + 1) % self.ui.stackedWidget.count()
        ))
        """ Page Rooms """
        self.ui.pushButton_Rooms.clicked.connect(self.toPageRooms)
        self.ui.pushButton_RoomSearch.clicked.connect(self.onClicked_pushButton_RoomSearch)
        self.ui.pushButton_RoomSearch_ClearFilter.clicked.connect(self.onClicked_pushButton_RoomSearch_ClearFilter)
        self.ui.pushButton_RoomSearchOptions.clicked.connect(self.onClicked_pushButton_RoomSearchOptions)
        self.ui.pushButton_Home.clicked.connect(self.toPageMainMenu)
        self.ui.pushButton_Back.clicked.connect(self.toPageMainMenu)
        self.ui.pushButton_RoomSearchOptions.setStyleSheet("background-color: rgba(255, 255, 255, 128);")
        self.ui.frame_RoomSearchOptions.setVisible(False)
        """ Page Rooms """
        """ Pagge Room Info """
        self.ui.pushButton_RoomInfo_Home.clicked.connect(self.toPageMainMenu)
        self.ui.pushButton_RoomInfo_Back.clicked.connect(self.toPageRooms)
        """ Pagge Room Info """
        self.ui.pushButton_Check.clicked.connect(self.toPageCheck)

        # Test
        self.ui.pushButton_Test.clicked.connect(self.toPageTest)
        self.ui.pushButton_Test0.clicked.connect(self.test0)
        self.ui.pushButton_Test1.clicked.connect(self.test1)
        self.ui.pushButton_Test2.clicked.connect(self.test2)

    # Icons
    def init_icons(self):
        """ Page Rooms """
        self.ui.pushButton_RoomSearch.setIcon(QIcon(QPixmap(icon_search_path)))
        self.ui.pushButton_RoomSearch_ClearFilter.setIcon(QIcon(QPixmap(icon_x_path)))
        self.ui.pushButton_RoomSearchOptions.setIcon(QIcon(QPixmap(icon_options_path)))
        self.ui.pushButton_Home.setIcon(QIcon(QPixmap(icon_home_path)))
        self.ui.pushButton_Back.setIcon(QIcon(QPixmap(icon_back_path)))
        """ Page Rooms """
        """ Page RoomInfo """
        self.ui.pushButton_RoomInfo_Home.setIcon(QIcon(QPixmap(icon_home_path)))
        self.ui.pushButton_RoomInfo_Back.setIcon(QIcon(QPixmap(icon_back_path)))
        """ Page RoomInfo """

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
    
    def renderRooms(self):
        """ render rooms for displaying in Page Rooms or Page Check """
        # Setup combobox to select don vi
        self.don_vis = read_all_don_vis()
        self.ui.comboBox_RoomSearchOptions_DonVi.clear()
        self.ui.comboBox_RoomSearchOptions_DonVi.addItem("")  # INDEX 0 OPTION
        for don_vi in self.don_vis:
            self.ui.comboBox_RoomSearchOptions_DonVi.addItem(don_vi.ten)
        # Setup frame for display all Khus
        self.khus = read_all_khus()
        parent = self.ui.frame_KhuHolder
        layout = self.ui.frame_KhuHolder.layout()
        clearAllWidgets(parent)

        for khu in self.khus:
            print(khu.ten)
            if khu.phongs:
                for phong in khu.phongs:
                    print(phong.ten)
            frame_Khu = createKhuFrame(parent=parent, khu=khu, callback=self.toPageRoomInfo)
            layout.addWidget(frame_Khu)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_Rooms)

    """ Page Rooms """
    def toPageRooms(self):
        self.is_view_mode = True
        self.renderRooms()

    def onClicked_pushButton_RoomSearch_ClearFilter(self):
        self.ui.lineEdit_RoomSearch.setText(None)
        self.ui.comboBox_RoomSearchOptions_DonVi.setCurrentIndex(0)

    def onClicked_pushButton_RoomSearch(self):
        selected_don_vi_id = None
        if self.ui.comboBox_RoomSearchOptions_DonVi.isVisible():
            selected_don_vi_index = self.ui.comboBox_RoomSearchOptions_DonVi.currentIndex()
            # NOT INDEX 0 OPTION
            if selected_don_vi_index != 0:
                selected_don_vi = self.don_vis[selected_don_vi_index - 1]
                selected_don_vi_id = selected_don_vi.id
        phongs = search_phong_by_filter(substring=self.ui.lineEdit_RoomSearch.text(),
                                        don_vi_id=selected_don_vi_id)
        for phong in phongs:
            print(phong.ten)
    
    def onClicked_pushButton_RoomSearchOptions(self):
        is_visible = self.ui.frame_RoomSearchOptions.isVisible()
        self.ui.frame_RoomSearchOptions.setVisible(not is_visible)

        # Set color based on visibility
        if is_visible:
            self.ui.pushButton_RoomSearchOptions.setStyleSheet("background-color: rgba(255, 255, 255, 128);")
        else:
            self.ui.pushButton_RoomSearchOptions.setStyleSheet("background-color: rgba(102, 153, 255, 128);")
    """ Page Rooms """

    """ Page Room info """
    def toPageRoomInfo(self, phong=None):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_RoomInfo)
        if self.is_view_mode == True:
            if phong:
                self.renderViewRoomInfo_Info(phong)
        elif self.is_view_mode == False:
            pass
        else:
            pass
    
    def renderViewRoomInfo_Info(self, phong):
        # Setup frame for display RoomInfo_Info
        parent = self.ui.frame_RoomInfo
        layout = self.ui.frame_RoomInfo.layout()
        clearAllWidgets(parent=parent)
        frame_RoomInfo_Info = createRoomInfo_Info_Frame(parent=parent, phong=phong)
        layout.addWidget(frame_RoomInfo_Info)

    
    """ Page Room info """
    """ Page Check """
    def toPageCheck(self):
        self.is_view_mode = False
        self.renderRooms()
    """ Page Check """

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
        khu = read_all_khus()[0]
        parent = self.ui.frame_ScrollAreaTest
        frame_Khu = createKhuFrame(parent, khu)
        layout = self.ui.frame_ScrollAreaTest.layout()
        layout.addWidget(frame_Khu)

    def myPrint(self, text):
        print(text)

def createRoomInfo_Info_Frame(parent, phong:Phong):
    # Frame for RoomInfo_Info to be setted in frame_RoomInfo
    frame_RoomInfo_Info = QFrame(parent=parent)
    frame_RoomInfo_Info.setFrameShape(QFrame.Shape.StyledPanel)   # Optional
    frame_RoomInfo_Info.setFrameShadow(QFrame.Shadow.Raised)  # Optional
    # Vertical layout for the frame
    layout_for_frame_RoomInfo_Info = QVBoxLayout(frame_RoomInfo_Info)
    label_Ten = QLabel(parent=frame_RoomInfo_Info)
    label_Ten.setText(f"Tên phòng: {phong.ten}")
    layout_for_frame_RoomInfo_Info.addWidget(label_Ten)
    label_Khu = QLabel(parent=frame_RoomInfo_Info)
    label_Khu.setText(f"Khu vực: {phong.khu.ten if phong.khu else ''}")
    layout_for_frame_RoomInfo_Info.addWidget(label_Khu)
    label_DonVi = QLabel(parent=frame_RoomInfo_Info)
    label_DonVi.setText(f"Đơn vị quản lý: {phong.don_vi.ten if phong.don_vi else ''}")
    layout_for_frame_RoomInfo_Info.addWidget(label_DonVi)
    # . . . add more label for phong's properties here ...
    # Create a vertical spacer as a widget
    spacer_widget = QWidget(parent=frame_RoomInfo_Info)
    spacer_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

    layout_for_frame_RoomInfo_Info.addWidget(spacer_widget)
    return frame_RoomInfo_Info

def createKhuFrame(parent, khu:Khu, callback = None):
    # Frame for Khu
    frame_Khu = QFrame(parent=parent)
    frame_Khu.setFrameShape(QFrame.Shape.StyledPanel)   # Optional
    frame_Khu.setFrameShadow(QFrame.Shadow.Raised)  # Optional

    # Vertical layout for Khu
    layout_Khu = QVBoxLayout(frame_Khu)

    # Label for Khu
    label_TenKhu = QLabel(parent=frame_Khu)
    label_TenKhu.setText(khu.ten)
    layout_Khu.addWidget(label_TenKhu)

    # Frame for Phongs in Khu
    frame_PhongKhu = QFrame(parent=frame_Khu)
    layout_Khu.addWidget(frame_PhongKhu)

    if khu.phongs:
        # Grid layout for Phongs
        gridLayout_Phong = QGridLayout(frame_PhongKhu)

        # Calculate rows and columns based on the number of Phongs
        num_phongs = len(khu.phongs)
        rows = (num_phongs - 1) // 5 + 1
        columns = min(num_phongs, 5)

        for i, phong in enumerate(khu.phongs):
            pushButton_Phong = QPushButton(parent=frame_PhongKhu)
            pushButton_Phong.setText(phong.ten)

            if callback:
                pushButton_Phong.clicked.connect(lambda checked, phong=phong: callback(phong))

            # Calculate the row and column positions based on the index
            row_position = i // columns
            column_position = i % columns

            gridLayout_Phong.addWidget(pushButton_Phong, row_position, column_position, 1, 1)

    else:
        verticalLayout = QVBoxLayout(frame_PhongKhu)
        verticalLayout.addWidget(QLabel("Không có phòng nào thuộc khu này!"))

    return frame_Khu

    

def clearAllWidgets(parent):
    layout = parent.layout()
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
