from collections import defaultdict
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
    QSizePolicy,
    QTableWidgetItem,
    QHeaderView
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
# from Backend.Models.models import *
# Database
from Backend.Database.db_sessions import *

""" Paths """
icon_search_path = "Frontend/Resources/Bootstrap/search.png"
icon_options_path = "Frontend/Resources/Bootstrap/sliders.png"
icon_home_path = "Frontend/Resources/Bootstrap/house-fill.png"
icon_back_path = "Frontend/Resources/Bootstrap/arrow-left.png"
icon_x_path = "Frontend/Resources/Bootstrap/x-lg.png"

class PageRoomsInfoMode(Enum):
    DANH_SACH = "Danh sach"
    KIEM_KE = "Kiem ke"

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

        # Full screen
        # self.showFullScreen()
        self.toPageMainMenu()

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
        self.don_vis = CRUD_DonVi.read_all()
        self.ui.comboBox_RoomSearchOptions_DonVi.clear()
        self.ui.comboBox_RoomSearchOptions_DonVi.addItem("")  # INDEX 0 OPTION
        for don_vi in self.don_vis:
            self.ui.comboBox_RoomSearchOptions_DonVi.addItem(don_vi.ten)
        # Setup frame for display all Khus
        self.khus = CRUD_Khu.read_all()
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
            self.ui.pushButton_RoomSearchOptions.setStyleSheet("background-color: rgba(255, 255, 255, 128);")
        else:
            self.ui.pushButton_RoomSearchOptions.setStyleSheet("background-color: rgba(102, 153, 255, 128);")
    """ Page Rooms """

    """ Page Room info """
    def toPageRoomInfo(self, phong=None):
        parent = self.ui.frame_RoomInfo
        clearAllWidgets(parent=parent)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_RoomInfo)
        if phong:
            self.renderViewRoomInfo_Info(phong)
            qpushbutton_clicked_disconnect(self.ui.pushButton_RoomInfo_Info)
            self.ui.pushButton_RoomInfo_Info.clicked.connect(lambda: self.renderViewRoomInfo_Info(phong=phong))
            
            if self.page_rooms_info_mode == PageRoomsInfoMode.DANH_SACH:
                self.ui.pushButton_RoomInfo_DanhMuc.setHidden(False)
                self.ui.pushButton_RoomInfo_KiemKe.setHidden(True)
                qpushbutton_clicked_disconnect(self.ui.pushButton_RoomInfo_DanhMuc)
                self.ui.pushButton_RoomInfo_DanhMuc.clicked.connect(lambda: self.renderViewRoomInfo_DanhMuc(phong=phong))
            elif self.page_rooms_info_mode == PageRoomsInfoMode.KIEM_KE:
                self.ui.pushButton_RoomInfo_DanhMuc.setHidden(True)
                self.ui.pushButton_RoomInfo_KiemKe.setHidden(False)
                qpushbutton_clicked_disconnect(self.ui.pushButton_RoomInfo_KiemKe)
                self.ui.pushButton_RoomInfo_KiemKe.clicked.connect(lambda: self.renderViewRoomInfo_KiemKe(phong=phong))
            else:
                pass
    
    def renderViewRoomInfo_Info(self, phong):
        self.ui.label_RoomInfo_TenPhong.setText(f"Phòng {phong.ma} - {phong.khu.ten}\n{phong.ten}")
        # Setup frame for display RoomInfo_Info
        parent = self.ui.frame_RoomInfo
        layout = self.ui.frame_RoomInfo.layout()
        clearAllWidgets(parent=parent)
        # Frame for RoomInfo_Info to be setted in frame_RoomInfo
        frame_RoomInfo_Info = QFrame(parent=parent)
        frame_RoomInfo_Info.setFrameShape(QFrame.Shape.StyledPanel)   # Optional
        frame_RoomInfo_Info.setFrameShadow(QFrame.Shadow.Raised)  # Optional
        # Vertical layout for the frame
        layout_for_frame_RoomInfo_Info = QVBoxLayout(frame_RoomInfo_Info)
        # Displaying Info
        label_ma_phong = QLabel(parent=frame_RoomInfo_Info)
        label_ma_phong.setText(f"Mã phòng: P.{phong.ma}")
        layout_for_frame_RoomInfo_Info.addWidget(label_ma_phong)

        label_ten_phong = QLabel(parent=frame_RoomInfo_Info)
        label_ten_phong.setText(f"Tên phòng: {phong.ten}")
        layout_for_frame_RoomInfo_Info.addWidget(label_ten_phong)

        label_khu_vuc = QLabel(parent=frame_RoomInfo_Info)
        label_khu_vuc.setText(f"Khu vực: {phong.khu.ten if phong.khu else ''}")
        layout_for_frame_RoomInfo_Info.addWidget(label_khu_vuc)

        label_don_vi = QLabel(parent=frame_RoomInfo_Info)
        label_don_vi.setText(f"Đơn vị quản lý: {phong.don_vi.ten if phong.don_vi else ''}")
        layout_for_frame_RoomInfo_Info.addWidget(label_don_vi)

        label_can_bo = QLabel(parent=frame_RoomInfo_Info)
        label_can_bo.setText(f"Cán bộ quản lý: {phong.can_bo.ten if phong.can_bo else ''}")
        layout_for_frame_RoomInfo_Info.addWidget(label_can_bo)

        label_sdt = QLabel(parent=frame_RoomInfo_Info)
        label_sdt.setText(f"SĐT liên hệ: {phong.can_bo.sdt if phong.can_bo.sdt else '' if phong.can_bo else ''}")
        layout_for_frame_RoomInfo_Info.addWidget(label_sdt)

        label_thong_tin = QLabel(parent=frame_RoomInfo_Info)
        label_thong_tin.setText(f"Thông tin phòng: {phong.thong_tin if phong.thong_tin else ''}")
        layout_for_frame_RoomInfo_Info.addWidget(label_thong_tin)

        # . . . add more label for phong's properties here ...
        # Create a vertical spacer as a widget
        spacer_widget = QWidget(parent=frame_RoomInfo_Info)
        spacer_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        layout_for_frame_RoomInfo_Info.addWidget(spacer_widget)
        layout.addWidget(frame_RoomInfo_Info)

    def renderViewRoomInfo_DanhMuc(self, phong):
        self.ui.label_RoomInfo_TenPhong.setText(f"Phòng {phong.ma} - {phong.khu.ten}\n{phong.ten}")
        # Setup frame for display RoomInfo_Info
        parent = self.ui.frame_RoomInfo
        layout = self.ui.frame_RoomInfo.layout()
        clearAllWidgets(parent=parent)
        frame_RoomInfo_DanhMuc = createRoomInfo_DanhMuc_Frame(parent=parent, phong=phong)
        layout.addWidget(frame_RoomInfo_DanhMuc)

    def renderViewRoomInfo_DanhMuc_Detail(self, phong:Phong, loai_tai_san:LoaiTaiSan, tai_san_list:List[TaiSan]):
        self.ui.label_RoomInfo_TenPhong.setText(f"Phòng {phong.ma} - {phong.khu.ten}\n{phong.ten}")
        # Setup frame for display RoomInfo_Info
        parent = self.ui.frame_RoomInfo
        layout = self.ui.frame_RoomInfo.layout()
        clearAllWidgets(parent=parent)
        frame_RoomInfo_DanhMuc_Detail = createRoomInfo_DanhMuc_Detail_Frame(parent=parent, phong=phong, loai_tai_san=loai_tai_san, tai_san_list=tai_san_list)
        layout.addWidget(frame_RoomInfo_DanhMuc_Detail)
    
    """ Page Room info """
    """ Page Check """
    def toPageCheck(self):
        self.page_rooms_info_mode = PageRoomsInfoMode.KIEM_KE
        self.renderRooms()

    def renderViewRoomInfo_KiemKe(self, phong):
        pass
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
        khu = CRUD_Khu.read_all()[0]
        parent = self.ui.frame_ScrollAreaTest
        frame_Khu = createKhuFrame(parent, khu)
        layout = self.ui.frame_ScrollAreaTest.layout()
        layout.addWidget(frame_Khu)

    def myPrint(self, text):
        print(text)


def createRoomInfo_DanhMuc_Frame(parent, phong:Phong, callback=None):
    # Frame for RoomInfo_Info to be setted in frame_RoomInfo
    frame_RoomInfo_DanhMuc = QFrame(parent=parent)
    frame_RoomInfo_DanhMuc.setFrameShape(QFrame.Shape.StyledPanel)   # Optional
    frame_RoomInfo_DanhMuc.setFrameShadow(QFrame.Shadow.Raised)  # Optional
    # Vertical layout for the frame
    layout_for_frame_RoomInfo_DanhMuc = QVBoxLayout(frame_RoomInfo_DanhMuc)
    # Display table for all Danh muc
    table_DanhMuc = QtWidgets.QTableWidget(parent=frame_RoomInfo_DanhMuc)
    # Table headers
    table_DanhMuc.setColumnCount(6)
    table_DanhMuc.setHorizontalHeaderLabels(['STT', 'Mã tài sản', 'Loại tài sản', 'SL', 'Trạng thái', 'Chức năng'])
    # Fill NhomTaiSan > LoaiTaiSan
    tai_sans_grouped = defaultdict(lambda: defaultdict(list))   # Dictionary of dictionaries of lists of tai_san
    for tai_san in phong.tai_sans:
        loai_tai_san = tai_san.loai_tai_san if tai_san.loai_tai_san else None
        nhom_tai_san = loai_tai_san.nhom_tai_san if loai_tai_san else None
        if loai_tai_san and nhom_tai_san:
            tai_sans_grouped[nhom_tai_san][loai_tai_san].append(tai_san)
    # Number of row in table = total nhom tai san + total loai tai san
    row_count = len(tai_sans_grouped)
    for nhom_tai_san, loai_tai_san_list in tai_sans_grouped.items():
        row_count += len(loai_tai_san_list)
    table_DanhMuc.setRowCount(row_count)
    # Display
    row = 0
    for nhom_tai_san, loai_tai_san_dict in tai_sans_grouped.items():
        # Nhom tai san
        print(f"Nhom tai san: {nhom_tai_san.ten}")
        # Display ten Nhom Tai San
        table_DanhMuc.setSpan(row, 0, 1, 6)
        qitem_ten_danh_muc = QTableWidgetItem(nhom_tai_san.ten)
        qitem_ten_danh_muc.setFlags(qitem_ten_danh_muc.flags() & ~PyQt6.QtCore.Qt.ItemFlag.ItemIsEditable)
        table_DanhMuc.setItem(row, 0, qitem_ten_danh_muc)
        row += 1
        stt = 1
        for loai_tai_san, tai_san_list in loai_tai_san_dict.items():
            # Loai tai san
            print(f"    Loai tai san: {loai_tai_san.ten}")
            # stt
            qitem_stt = QTableWidgetItem(f"{stt}")
            qitem_stt.setFlags(qitem_stt.flags() & ~PyQt6.QtCore.Qt.ItemFlag.ItemIsEditable)
            table_DanhMuc.setItem(row, 0, qitem_stt)
            table_DanhMuc.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
            # ma
            qitem_ma_loai_tai_san = QTableWidgetItem(f"{phong.don_vi.ma}.{phong.ma}.{loai_tai_san.ma}")
            qitem_ma_loai_tai_san.setFlags(qitem_ma_loai_tai_san.flags() & ~PyQt6.QtCore.Qt.ItemFlag.ItemIsEditable)
            table_DanhMuc.setItem(row, 1, qitem_ma_loai_tai_san)
            table_DanhMuc.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
            # ten
            qitem_ten_loai_tai_san = QTableWidgetItem(loai_tai_san.ten)
            qitem_ten_loai_tai_san.setFlags(qitem_ten_loai_tai_san.flags() & ~PyQt6.QtCore.Qt.ItemFlag.ItemIsEditable)
            table_DanhMuc.setItem(row, 2, qitem_ten_loai_tai_san)
            table_DanhMuc.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
            # sl
            qitem_sl = QTableWidgetItem(f"{len(tai_san_list)}")
            qitem_sl.setFlags(qitem_sl.flags() & ~PyQt6.QtCore.Qt.ItemFlag.ItemIsEditable)
            table_DanhMuc.setItem(row, 3, qitem_sl)
            # trang thai
            qitem_trang_thai = QTableWidgetItem(f"_")
            qitem_trang_thai.setFlags(qitem_trang_thai.flags() & ~PyQt6.QtCore.Qt.ItemFlag.ItemIsEditable)
            table_DanhMuc.setItem(row, 4, qitem_trang_thai)
            # chuc nang
            button = QPushButton('Chi tiết', parent)
            if callback:
                button.clicked.connect(lambda: callback())
            table_DanhMuc.setCellWidget(row, 5, button)
            table_DanhMuc.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)

            row += 1
            stt += 1
    # Custom display for cols and rows of table
    table_DanhMuc.resizeColumnsToContents()
    table_DanhMuc.resizeRowsToContents()
    # Put the table into layout
    layout_for_frame_RoomInfo_DanhMuc.addWidget(table_DanhMuc)
    return frame_RoomInfo_DanhMuc

def createRoomInfo_DanhMuc_Detail_Frame(parent, phong:Phong, loai_tai_san:LoaiTaiSan, tai_san_list:List[TaiSan]):
    # Frame for RoomInfo_Info to be setted in frame_RoomInfo
    frame_RoomInfo_DanhMuc_Detail = QFrame(parent=parent)
    frame_RoomInfo_DanhMuc_Detail.setFrameShape(QFrame.Shape.StyledPanel)   # Optional
    frame_RoomInfo_DanhMuc_Detail.setFrameShadow(QFrame.Shadow.Raised)  # Optional
    # Vertical layout for the frame
    layout_for_frame_RoomInfo_DanhMuc_Detail = QVBoxLayout(frame_RoomInfo_DanhMuc_Detail)
    # Display table for all Danh muc
    table_DanhMuc_Detail = QtWidgets.QTableWidget(parent=frame_RoomInfo_DanhMuc_Detail)
    # Table headers
    table_DanhMuc_Detail.setColumnCount(5)
    table_DanhMuc_Detail.setHorizontalHeaderLabels(['STT', 'Mã định danh tài sản', 'Mô tả chi tiết tài sản', 'Trạng thái', 'Ghi chú'])
    # Fill LoaiTaiSan > TaiSan
    # Number of row in table = ten loai tai san + total tai san
    row_count = 1 + len(tai_san_list)
    table_DanhMuc_Detail.setRowCount(row_count)
    # Display ten Loai Tai San
    table_DanhMuc_Detail.setSpan(0, 0, 1, 5)  # Merge cells
    qitem_ten_loai_tai_san = QTableWidgetItem(loai_tai_san.ten)
    qitem_ten_loai_tai_san.setFlags(qitem_ten_loai_tai_san.flags() & ~PyQt6.QtCore.Qt.ItemFlag.ItemIsEditable)
    table_DanhMuc_Detail.setItem(0, 0, qitem_ten_loai_tai_san)
    
        
    # Custom display for cols and rows of table
    table_DanhMuc_Detail.resizeColumnsToContents()
    table_DanhMuc_Detail.resizeRowsToContents()
    # Put the table into layout
    layout_for_frame_RoomInfo_DanhMuc_Detail.addWidget(table_DanhMuc_Detail)
    return frame_RoomInfo_DanhMuc_Detail

def createRoomInfo_KiemKe_Frame(parent, phong:Phong):
    pass

def createKhuFrame(parent, khu:Khu, callback = None):
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
                pushButton_Phong.clicked.connect(lambda checked, phong=phong: callback(phong))

            # Calculate the row and column positions based on the index
            row_position = i // columns
            column_position = i % columns

            gridLayout_Phong.addWidget(pushButton_Phong, row_position, column_position, 1, 1)

    else:
        verticalLayout = QVBoxLayout(frame_PhongKhu)
        verticalLayout.addWidget(QLabel("Không có phòng nào thuộc khu này!"))

    return frame_Khu

def qpushbutton_clicked_disconnect(button:QPushButton):
    try:
        button.clicked.disconnect()
    except Exception:
        pass
    

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
