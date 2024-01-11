from Backend.Database.db_sessions import *
from Backend.Services.Scanner.fake_scanner import *
from Frontend.Helper.helper import *
from Frontend.Design.design_ui import Ui_MainWindow
from collections import defaultdict
import signal
import typing
# PyQt6
from functools import partial
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
    QSizePolicy,
    QTableWidgetItem,
    QHeaderView
)
from PyQt6.QtCore import Qt, QTimer, QCoreApplication
from PyQt6.QtGui import (
    QPixmap,
    QIcon,
    QColor
)

""" Modules """
""" Frontend """
# The design
# Dynamic render view and other helper for UI
""" QR Scanner """
# Scanner
# from Backend.Services.Scanner.scanner import *
# Fake scanner for developing UI interface
""" Backend """
# Database

TEST_DEV = True
if TEST_DEV:
    def resetAllTaiSan():
        status, tai_sans = CRUD_TaiSan.read_all()
        for tai_san in tai_sans:
            CRUD_TaiSan.update(id=tai_san.id,
                               ghi_chu=BanGhiKiemKeState.NOT_AVAILABLE.value)

    # resetAllTaiSan()

""" Paths """
icon_search_path = "Frontend/Resources/Bootstrap/search.png"
icon_options_path = "Frontend/Resources/Bootstrap/sliders.png"
icon_home_path = "Frontend/Resources/Bootstrap/house-fill.png"
icon_back_path = "Frontend/Resources/Bootstrap/arrow-left.png"
icon_x_path = "Frontend/Resources/Bootstrap/x-lg.png"
icon_qr_code_path = "Frontend/Resources/Bootstrap/qr-code.png"


class PageRoomsInfoMode(Enum):
    DANH_SACH = "Danh sách"
    KIEM_KE = "Kiểm kê"


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
        self.ui.pushButton_ToLeft.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(
            (self.ui.stackedWidget.currentIndex() -
             1) % self.ui.stackedWidget.count()
        ))
        self.ui.pushButton_ToRight.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(
            (self.ui.stackedWidget.currentIndex() +
             1) % self.ui.stackedWidget.count()
        ))
        """ Page Rooms """
        self.ui.pushButton_Rooms.clicked.connect(self.toPageRooms)
        self.ui.pushButton_RoomSearch.clicked.connect(
            self.onClicked_pushButton_RoomSearch)
        self.ui.pushButton_RoomSearch_ClearFilter.clicked.connect(
            self.onClicked_pushButton_RoomSearch_ClearFilter)
        self.ui.pushButton_RoomSearchOptions.clicked.connect(
            self.onClicked_pushButton_RoomSearchOptions)
        self.ui.pushButton_Home.clicked.connect(self.toPageMainMenu)
        self.ui.pushButton_Back.clicked.connect(self.toPageMainMenu)
        self.ui.pushButton_RoomSearchOptions.setStyleSheet(
            "background-color: rgba(255, 255, 255, 128);")
        self.ui.frame_RoomSearchOptions.setVisible(False)
        """ Page Rooms """
        """ Pagge Room Info """
        self.ui.pushButton_RoomInfo_Home.clicked.connect(self.toPageMainMenu)
        self.ui.pushButton_RoomInfo_Back.clicked.connect(
            self.backToPageRoomsOrChecks)
        """ Pagge Room Info """
        """ Page QR """
        self.ui.pushButton_KiemTraThietBi.clicked.connect(self.toPageQR)
        """ Page QR """
        """ Page CreateQR """
        self.ui.pushButton_ToPageCreateQR.clicked.connect(self.toPageCreateQR)
        """ Page CreateQR """
        """ Page Check """
        self.handler_kiem_kes = defaultdict(Handler_KiemKe)
        self.ui.pushButton_Check.clicked.connect(self.toPageCheck)
        """ Page Check """

        # Test
        self.ui.pushButton_Test.clicked.connect(self.toPageTest)
        self.ui.pushButton_Test0.clicked.connect(self.test0)
        self.ui.pushButton_Test1.clicked.connect(self.test1)
        self.ui.pushButton_Test2.clicked.connect(self.test2)

        # Full screen
        # self.showFullScreen()
        self.toPageMainMenu()

        # Scanner
        self.scanning_phong = None
        self.scanning_loai_tai_san = None
        self.scanning_tai_san_list = None
        self.thread_scanner = Thread_Scanner(vendor_id=0x1a86,
                                             product_id=0xe026)
        self.thread_scanner.is_done.connect(self.scanned_update)
        self.thread_scanner.start()

    # Icons
    def init_icons(self):
        """ Page Rooms """
        self.ui.pushButton_RoomSearch.setIcon(QIcon(QPixmap(icon_search_path)))
        self.ui.pushButton_RoomSearch_ClearFilter.setIcon(
            QIcon(QPixmap(icon_x_path)))
        self.ui.pushButton_RoomSearchOptions.setIcon(
            QIcon(QPixmap(icon_options_path)))
        self.ui.pushButton_Home.setIcon(QIcon(QPixmap(icon_home_path)))
        self.ui.pushButton_Back.setIcon(QIcon(QPixmap(icon_back_path)))
        """ Page Rooms """
        """ Page RoomInfo """
        self.ui.pushButton_RoomInfo_Home.setIcon(
            QIcon(QPixmap(icon_home_path)))
        self.ui.pushButton_RoomInfo_Back.setIcon(
            QIcon(QPixmap(icon_back_path)))
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
        qpushbutton_clicked_disconnect(self.ui.pushButton_RoomInfo_Back)
        self.ui.pushButton_RoomInfo_Back.clicked.connect(
            self.backToPageRoomsOrChecks)
        status, result = CRUD_DonVi.read_all()
        don_vis = []
        if status == CRUD_Status.FOUND:
            don_vis = result
        else:
            print(status, result)
        self.ui.comboBox_RoomSearchOptions_DonVi.clear()
        self.ui.comboBox_RoomSearchOptions_DonVi.addItem("")  # INDEX 0 OPTION
        for don_vi in don_vis:
            self.ui.comboBox_RoomSearchOptions_DonVi.addItem(don_vi.ten)
        parent = self.ui.frame_KhuHolder
        layout = parent.layout()
        clearAllWidgets(parent)
        status, result = CRUD_Khu.read_all()
        khus = []
        if status == CRUD_Status.FOUND:
            khus = result
        else:
            print(status, result)
        for khu in khus:
            frame_Khu = Frame_Khu(parent=parent,
                                  khu=khu,
                                  callback_pushButton_Phong=self.toPageRoomInfo)
            layout.addWidget(frame_Khu)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_Rooms)

    """ Page Rooms """

    def backToPageRoomsOrChecks(self):
        if self.page_rooms_info_mode == PageRoomsInfoMode.DANH_SACH:
            self.toPageRooms()
        elif self.page_rooms_info_mode == PageRoomsInfoMode.KIEM_KE:
            self.toPageCheck()

    def toPageRooms(self):
        self.page_rooms_info_mode = PageRoomsInfoMode.DANH_SACH
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
        """ Filtered search
        phongs = search_phong_by_filter(substring=self.ui.lineEdit_RoomSearch.text(),
                                        don_vi_id=selected_don_vi_id)
        for phong in phongs:
            print(phong.ten)
        """

    def onClicked_pushButton_RoomSearchOptions(self):
        is_visible = self.ui.frame_RoomSearchOptions.isVisible()
        self.ui.frame_RoomSearchOptions.setVisible(not is_visible)

        # Set color based on visibility
        if is_visible:
            self.ui.pushButton_RoomSearchOptions.setStyleSheet(
                "background-color: rgba(255, 255, 255, 128);")
        else:
            self.ui.pushButton_RoomSearchOptions.setStyleSheet(
                "background-color: rgba(102, 153, 255, 128);")
    """ Page Rooms """

    """ Page CreateQR """

    def toPageCreateQR(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_CreateQR)
    """ Page CreateQR """

    """ Page QR """

    def toPageQR(self, callback=None):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_QR)
        self.ui.label_QRCode.setText("Đang chờ đọc QR...")

        # Process pending events to update the UI
        QCoreApplication.processEvents()
        self.scanner.read_barcode(callback=self.displayScannedString)

    def displayScannedString(self, scanned_string=None):
        if scanned_string == ScannerStatus.NO_DEVICE:
            msg = "Không kết nối được tới thiết bị đọc QR"
        elif scanned_string == ScannerStatus.READ_ERROR:
            msg = "Có lỗi xảy ra khi đọc QR"
        else:
            msg = scanned_string

        self.ui.label_QRCode.setText(msg)
        # Process pending events to update the UI
        QCoreApplication.processEvents()
        
        



    """ Page QR """

    """ Page Room info """

    def toPageRoomInfo(self, phong):
        parent = self.ui.frame_RoomInfo
        clearAllWidgets(parent_widget=parent)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_RoomInfo)
        self.renderViewRoomInfo_Info(phong)
        qpushbutton_clicked_disconnect(self.ui.pushButton_RoomInfo_Info)
        self.ui.pushButton_RoomInfo_Info.clicked.connect(
            lambda: self.renderViewRoomInfo_Info(phong=phong))

        if self.page_rooms_info_mode == PageRoomsInfoMode.DANH_SACH:
            self.ui.pushButton_RoomInfo_DanhMuc.setHidden(False)
            self.ui.pushButton_RoomInfo_KiemKe.setHidden(True)
            qpushbutton_clicked_disconnect(
                self.ui.pushButton_RoomInfo_DanhMuc)
            self.ui.pushButton_RoomInfo_DanhMuc.clicked.connect(
                lambda: self.renderViewRoomInfo_DanhMuc(phong=phong))
        elif self.page_rooms_info_mode == PageRoomsInfoMode.KIEM_KE:
            self.ui.pushButton_RoomInfo_DanhMuc.setHidden(True)
            self.ui.pushButton_RoomInfo_KiemKe.setHidden(False)
            qpushbutton_clicked_disconnect(
                self.ui.pushButton_RoomInfo_KiemKe)
            self.ui.pushButton_RoomInfo_KiemKe.clicked.connect(
                lambda: self.renderViewRoomInfo_KiemKe(phong=phong))
        else:
            pass

    def renderViewRoomInfo_Info(self, phong):
        qpushbutton_clicked_disconnect(self.ui.pushButton_RoomInfo_Back)
        self.ui.pushButton_RoomInfo_Back.clicked.connect(
            self.backToPageRoomsOrChecks)
        self.ui.label_RoomInfo_TenPhong.setText(
            f"Phòng {phong.ma} - {phong.khu.ten}\n{phong.ten}")
        # Setup frame for display RoomInfo_Info
        parent = self.ui.frame_RoomInfo
        parent_layout = parent.layout()
        clearAllWidgets(parent_widget=parent)
        # Frame for RoomInfo_Info to be setted in frame_RoomInfo
        frame_RoomInfo_Info = Frame_RoomInfo_Info(parent=parent,
                                                  phong=phong)
        parent_layout.addWidget(frame_RoomInfo_Info)

    def renderViewRoomInfo_DanhMuc(self, phong):
        qpushbutton_clicked_disconnect(self.ui.pushButton_RoomInfo_Back)
        self.ui.pushButton_RoomInfo_Back.clicked.connect(
            self.backToPageRoomsOrChecks)
        """ Tạo view danh mục """
        self.ui.label_RoomInfo_TenPhong.setText(
            f"Phòng {phong.ma} - {phong.khu.ten}\n{phong.ten}")
        # Setup frame for display RoomInfo_Info
        parent = self.ui.frame_RoomInfo
        parent_layout = parent.layout()
        clearAllWidgets(parent_widget=parent)
        table_DanhMuc = Table_DanhMuc(parent=parent,
                                      phong=phong,
                                      callback_DetailButton=self.renderViewRoomInfo_DanhMuc_Detail)
        parent_layout.addWidget(table_DanhMuc)

    def renderViewRoomInfo_KiemKe(self, phong):
        """ Tạo view kiểm kê """
        self.ui.label_RoomInfo_TenPhong.setText(
            f"Phòng {phong.ma} - {phong.khu.ten}\n{phong.ten}")
        # Setup frame for display RoomInfo_Info
        parent = self.ui.frame_RoomInfo
        parent_layout = parent.layout()
        clearAllWidgets(parent_widget=parent)
        table_DanhMuc_KiemKe = Table_DanhMuc_KiemKe(parent=parent,
                                                    phong=phong,
                                                    callback_EditButton=self.renderViewRoomInfo_KiemKe_Detail)
        parent_layout.addWidget(table_DanhMuc_KiemKe)

    def renderViewRoomInfo_KiemKe_Detail(self, phong: Phong, loai_tai_san: LoaiTaiSan, tai_san_list: List[TaiSan]):
        self.ui.label_RoomInfo_TenPhong.setText(
            f"Phòng {phong.ma} - {phong.khu.ten}\n{phong.ten}")
        # Setup frame for display RoomInfo_Info
        parent = self.ui.frame_RoomInfo
        layout = self.ui.frame_RoomInfo.layout()
        clearAllWidgets(parent_widget=parent)
        table_DanhMuc_KiemKe_Detail = Table_DanhMuc_KiemKe_Detail(parent=parent,
                                                                  phong=phong,
                                                                  loai_tai_san=loai_tai_san,
                                                                  tai_san_list=tai_san_list)
        layout.addWidget(table_DanhMuc_KiemKe_Detail)
        # Process pending events to update the UI
        QCoreApplication.processEvents()
        self.scanning_phong = phong
        self.scanning_loai_tai_san = loai_tai_san
        self.scanning_tai_san_list = tai_san_list
    
    def scanned_update(self, scanned_string:str):
        print(scanned_string)
        phong = self.scanning_phong
        loai_tai_san = self.scanning_loai_tai_san
        tai_san_list = self.scanning_tai_san_list
        if not phong or not loai_tai_san or not tai_san_list:
            return
        for tai_san in tai_san_list:
            ma_tai_san = f"{phong.don_vi.ma}.{phong.ma}.{loai_tai_san.ma}.{tai_san.ma}"
            print(f"{ma_tai_san =}")
            if ma_tai_san == scanned_string:
                CRUD_TaiSan.update(id=tai_san.id, ghi_chu=BanGhiKiemKeState.IS_AVAILABLE.value)
                self.renderViewRoomInfo_KiemKe_Detail(phong=phong, loai_tai_san=loai_tai_san, tai_san_list=tai_san_list)
                return
        

    def renderViewRoomInfo_DanhMuc_Detail(self, phong: Phong, loai_tai_san: LoaiTaiSan, tai_san_list: List[TaiSan]):
        qpushbutton_clicked_disconnect(self.ui.pushButton_RoomInfo_Back)
        self.ui.pushButton_RoomInfo_Back.clicked.connect(
            partial(self.renderViewRoomInfo_DanhMuc, phong=phong))
        self.ui.label_RoomInfo_TenPhong.setText(
            f"Phòng {phong.ma} - {phong.khu.ten}\n{phong.ten}")
        # Setup frame for display RoomInfo_Info
        parent = self.ui.frame_RoomInfo
        parent_layout = parent.layout()
        clearAllWidgets(parent_widget=parent)

        table_DanhMuc_Detail = Table_DanhMuc_Detail(parent=parent,
                                                    phong=phong,
                                                    loai_tai_san=loai_tai_san,
                                                    tai_san_list=tai_san_list)
        parent_layout.addWidget(table_DanhMuc_Detail)

    """ Page Room info """
    """ Page Check """

    def toPageCheck(self):
        self.page_rooms_info_mode = PageRoomsInfoMode.KIEM_KE
        self.renderRooms()

    """ Page Check """

    # Test
    def toPageTest(self):
        resetAllTaiSan()
        self.toPageMainMenu()
        return
        dialog = Dialog_QRScanner(title='Test title',
                                  msg='Hello msg')
        result = dialog.exec()
        if result:
            print("Success!")
        else:
            print("Cancel!")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_Test)

    def test0(self):
        clearAllWidgets(self.ui.frame_ScrollAreaTest)

    def test1(self):
        layout = self.ui.frame_ScrollAreaTest.layout()
        button = QPushButton(text=f"{layout.count()}")
        button.clicked.connect(lambda: self.myPrint(
            text=f"Button {button.objectName()} clicked!"))
        layout.addWidget(button)

    def test2(self):
        status, khu = CRUD_Khu.read_all()[0]
        parent = self.ui.frame_ScrollAreaTest
        frame_Khu = createKhuFrame(parent, khu)
        layout = self.ui.frame_ScrollAreaTest.layout()
        layout.addWidget(frame_Khu)

    def myPrint(self, text):
        print(text)


def createRoomInfo_KiemKe_Frame(parent, phong: Phong):
    pass


def createKhuFrame(parent, khu: Khu, callback=None):
    # Frame for Khu
    frame_Khu = QFrame(parent=parent)
    frame_Khu.setFrameShape(QFrame.Shape.StyledPanel)   # Optional
    frame_Khu.setFrameShadow(QFrame.Shadow.Raised)      # Optional

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
            pushButton_Phong.setText(f"P.{phong.ma}")

            if callback:
                pushButton_Phong.clicked.connect(
                    lambda checked, phong=phong: callback(phong))

            # Calculate the row and column positions based on the index
            row_position = i // columns
            column_position = i % columns

            gridLayout_Phong.addWidget(
                pushButton_Phong, row_position, column_position, 1, 1)

    else:
        verticalLayout = QVBoxLayout(frame_PhongKhu)
        verticalLayout.addWidget(QLabel("Không có phòng nào thuộc khu này!"))

    return frame_Khu


def qpushbutton_clicked_disconnect(button: QPushButton):
    try:
        button.clicked.disconnect()
    except Exception:
        pass


if __name__ == "__main__":
    app = QApplication([])
    window = MyApplication()
    window.show()
    app.exec()
