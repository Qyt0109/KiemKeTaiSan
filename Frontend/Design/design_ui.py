# Form implementation generated from reading ui file '/Applications/CODESTUFF/KKTS/Frontend/Design/design.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(617, 500)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setStyleSheet("background-color: rgb(102, 153, 255);\n"
"color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_ToLeft = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_ToLeft.setObjectName("pushButton_ToLeft")
        self.horizontalLayout_8.addWidget(self.pushButton_ToLeft)
        self.pushButton_ToRight = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_ToRight.setObjectName("pushButton_ToRight")
        self.horizontalLayout_8.addWidget(self.pushButton_ToRight)
        self.label = QtWidgets.QLabel(parent=self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        self.pushButton_Test = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_Test.setObjectName("pushButton_Test")
        self.horizontalLayout_8.addWidget(self.pushButton_Test, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.frame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_Login = QtWidgets.QWidget()
        self.page_Login.setObjectName("page_Login")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_Login)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_4 = QtWidgets.QFrame(parent=self.page_Login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_6 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.frame_3 = QtWidgets.QFrame(parent=self.frame_6)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_Username = QtWidgets.QLineEdit(parent=self.frame_3)
        self.lineEdit_Username.setObjectName("lineEdit_Username")
        self.horizontalLayout_2.addWidget(self.lineEdit_Username)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_6)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit_Password = QtWidgets.QLineEdit(parent=self.frame_5)
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.horizontalLayout.addWidget(self.lineEdit_Password)
        self.verticalLayout_5.addWidget(self.frame_5)
        self.pushButton_Login = QtWidgets.QPushButton(parent=self.frame_6)
        self.pushButton_Login.setMaximumSize(QtCore.QSize(230, 16777215))
        self.pushButton_Login.setObjectName("pushButton_Login")
        self.verticalLayout_5.addWidget(self.pushButton_Login, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.pushButton_ForgotPassword = QtWidgets.QPushButton(parent=self.frame_6)
        self.pushButton_ForgotPassword.setStyleSheet("text-decoration:underline solid;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.pushButton_ForgotPassword.setCheckable(False)
        self.pushButton_ForgotPassword.setObjectName("pushButton_ForgotPassword")
        self.verticalLayout_5.addWidget(self.pushButton_ForgotPassword)
        self.verticalLayout_4.addWidget(self.frame_6)
        self.verticalLayout_6.addWidget(self.frame_4, 0, QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.stackedWidget.addWidget(self.page_Login)
        self.page_MainMenu = QtWidgets.QWidget()
        self.page_MainMenu.setObjectName("page_MainMenu")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_MainMenu)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_7 = QtWidgets.QFrame(parent=self.page_MainMenu)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_8 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_10 = QtWidgets.QFrame(parent=self.frame_7)
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_10)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.pushButton_Rooms = QtWidgets.QPushButton(parent=self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Rooms.sizePolicy().hasHeightForWidth())
        self.pushButton_Rooms.setSizePolicy(sizePolicy)
        self.pushButton_Rooms.setObjectName("pushButton_Rooms")
        self.horizontalLayout_5.addWidget(self.pushButton_Rooms)
        self.verticalLayout_8.addWidget(self.frame_10)
        self.frame_9 = QtWidgets.QFrame(parent=self.frame_7)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_9)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.pushButton_Check = QtWidgets.QPushButton(parent=self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Check.sizePolicy().hasHeightForWidth())
        self.pushButton_Check.setSizePolicy(sizePolicy)
        self.pushButton_Check.setObjectName("pushButton_Check")
        self.horizontalLayout_4.addWidget(self.pushButton_Check)
        self.verticalLayout_8.addWidget(self.frame_9)
        self.frame_8 = QtWidgets.QFrame(parent=self.frame_7)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(parent=self.frame_8)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout_8.addWidget(self.frame_8)
        self.verticalLayout_7.addWidget(self.frame_7, 0, QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.stackedWidget.addWidget(self.page_MainMenu)
        self.page_Rooms = QtWidgets.QWidget()
        self.page_Rooms.setObjectName("page_Rooms")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_Rooms)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_11 = QtWidgets.QFrame(parent=self.page_Rooms)
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_12 = QtWidgets.QFrame(parent=self.frame_11)
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_Rooms_Tittle = QtWidgets.QLabel(parent=self.frame_12)
        self.label_Rooms_Tittle.setObjectName("label_Rooms_Tittle")
        self.verticalLayout_11.addWidget(self.label_Rooms_Tittle, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_14 = QtWidgets.QFrame(parent=self.frame_12)
        self.frame_14.setStyleSheet(".QPushButton {\n"
"    background-color: rgba(255, 255, 255, 128);\n"
"}")
        self.frame_14.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(parent=self.frame_14)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.lineEdit_RoomSearch = QtWidgets.QLineEdit(parent=self.frame_14)
        self.lineEdit_RoomSearch.setObjectName("lineEdit_RoomSearch")
        self.horizontalLayout_6.addWidget(self.lineEdit_RoomSearch)
        self.pushButton_RoomSearch_ClearFilter = QtWidgets.QPushButton(parent=self.frame_14)
        self.pushButton_RoomSearch_ClearFilter.setText("")
        self.pushButton_RoomSearch_ClearFilter.setObjectName("pushButton_RoomSearch_ClearFilter")
        self.horizontalLayout_6.addWidget(self.pushButton_RoomSearch_ClearFilter, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.pushButton_RoomSearch = QtWidgets.QPushButton(parent=self.frame_14)
        self.pushButton_RoomSearch.setStyleSheet("")
        self.pushButton_RoomSearch.setText("")
        self.pushButton_RoomSearch.setObjectName("pushButton_RoomSearch")
        self.horizontalLayout_6.addWidget(self.pushButton_RoomSearch, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.pushButton_RoomSearchOptions = QtWidgets.QPushButton(parent=self.frame_14)
        self.pushButton_RoomSearchOptions.setStyleSheet("")
        self.pushButton_RoomSearchOptions.setText("")
        self.pushButton_RoomSearchOptions.setObjectName("pushButton_RoomSearchOptions")
        self.horizontalLayout_6.addWidget(self.pushButton_RoomSearchOptions, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_11.addWidget(self.frame_14)
        self.frame_RoomSearchOptions = QtWidgets.QFrame(parent=self.frame_12)
        self.frame_RoomSearchOptions.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_RoomSearchOptions.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_RoomSearchOptions.setObjectName("frame_RoomSearchOptions")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_RoomSearchOptions)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_11 = QtWidgets.QLabel(parent=self.frame_RoomSearchOptions)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.comboBox_RoomSearchOptions_DonVi = QtWidgets.QComboBox(parent=self.frame_RoomSearchOptions)
        self.comboBox_RoomSearchOptions_DonVi.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_RoomSearchOptions_DonVi.sizePolicy().hasHeightForWidth())
        self.comboBox_RoomSearchOptions_DonVi.setSizePolicy(sizePolicy)
        self.comboBox_RoomSearchOptions_DonVi.setObjectName("comboBox_RoomSearchOptions_DonVi")
        self.comboBox_RoomSearchOptions_DonVi.addItem("")
        self.comboBox_RoomSearchOptions_DonVi.addItem("")
        self.comboBox_RoomSearchOptions_DonVi.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBox_RoomSearchOptions_DonVi)
        self.verticalLayout_11.addWidget(self.frame_RoomSearchOptions)
        self.verticalLayout_10.addWidget(self.frame_12, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.scrollArea_Rooms = QtWidgets.QScrollArea(parent=self.frame_11)
        self.scrollArea_Rooms.setMouseTracking(False)
        self.scrollArea_Rooms.setWidgetResizable(True)
        self.scrollArea_Rooms.setObjectName("scrollArea_Rooms")
        self.scrollAreaWidgetContents_Rooms = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_Rooms.setGeometry(QtCore.QRect(0, 0, 587, 255))
        self.scrollAreaWidgetContents_Rooms.setObjectName("scrollAreaWidgetContents_Rooms")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_Rooms)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_KhuHolder = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_Rooms)
        self.frame_KhuHolder.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_KhuHolder.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_KhuHolder.setObjectName("frame_KhuHolder")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_KhuHolder)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_12.addWidget(self.frame_KhuHolder)
        self.scrollArea_Rooms.setWidget(self.scrollAreaWidgetContents_Rooms)
        self.verticalLayout_10.addWidget(self.scrollArea_Rooms)
        self.frame_15 = QtWidgets.QFrame(parent=self.frame_11)
        self.frame_15.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_Home = QtWidgets.QPushButton(parent=self.frame_15)
        self.pushButton_Home.setMaximumSize(QtCore.QSize(64, 64))
        self.pushButton_Home.setText("")
        self.pushButton_Home.setObjectName("pushButton_Home")
        self.horizontalLayout_7.addWidget(self.pushButton_Home, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.pushButton_Back = QtWidgets.QPushButton(parent=self.frame_15)
        self.pushButton_Back.setText("")
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.horizontalLayout_7.addWidget(self.pushButton_Back, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_10.addWidget(self.frame_15, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.verticalLayout_9.addWidget(self.frame_11)
        self.stackedWidget.addWidget(self.page_Rooms)
        self.page_RoomInfo = QtWidgets.QWidget()
        self.page_RoomInfo.setObjectName("page_RoomInfo")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.page_RoomInfo)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.frame_13 = QtWidgets.QFrame(parent=self.page_RoomInfo)
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.frame_16 = QtWidgets.QFrame(parent=self.frame_13)
        self.frame_16.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.label_RoomInfo_TenPhong = QtWidgets.QLabel(parent=self.frame_16)
        self.label_RoomInfo_TenPhong.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_RoomInfo_TenPhong.setObjectName("label_RoomInfo_TenPhong")
        self.verticalLayout_27.addWidget(self.label_RoomInfo_TenPhong, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_18 = QtWidgets.QFrame(parent=self.frame_16)
        self.frame_18.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushButton_RoomInfo_Info = QtWidgets.QPushButton(parent=self.frame_18)
        self.pushButton_RoomInfo_Info.setObjectName("pushButton_RoomInfo_Info")
        self.horizontalLayout_14.addWidget(self.pushButton_RoomInfo_Info)
        self.pushButton_RoomInfo_DanhMuc = QtWidgets.QPushButton(parent=self.frame_18)
        self.pushButton_RoomInfo_DanhMuc.setObjectName("pushButton_RoomInfo_DanhMuc")
        self.horizontalLayout_14.addWidget(self.pushButton_RoomInfo_DanhMuc)
        self.pushButton_RoomInfo_KiemKe = QtWidgets.QPushButton(parent=self.frame_18)
        self.pushButton_RoomInfo_KiemKe.setObjectName("pushButton_RoomInfo_KiemKe")
        self.horizontalLayout_14.addWidget(self.pushButton_RoomInfo_KiemKe)
        self.verticalLayout_27.addWidget(self.frame_18, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.verticalLayout_26.addWidget(self.frame_16, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.scrollArea_RoomInfo = QtWidgets.QScrollArea(parent=self.frame_13)
        self.scrollArea_RoomInfo.setWidgetResizable(True)
        self.scrollArea_RoomInfo.setObjectName("scrollArea_RoomInfo")
        self.scrollAreaWidgetContents_RoomInfo = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_RoomInfo.setGeometry(QtCore.QRect(0, 0, 587, 314))
        self.scrollAreaWidgetContents_RoomInfo.setObjectName("scrollAreaWidgetContents_RoomInfo")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_RoomInfo)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_RoomInfo = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_RoomInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_RoomInfo.sizePolicy().hasHeightForWidth())
        self.frame_RoomInfo.setSizePolicy(sizePolicy)
        self.frame_RoomInfo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_RoomInfo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_RoomInfo.setObjectName("frame_RoomInfo")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_RoomInfo)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_15.addWidget(self.frame_RoomInfo)
        self.scrollArea_RoomInfo.setWidget(self.scrollAreaWidgetContents_RoomInfo)
        self.verticalLayout_26.addWidget(self.scrollArea_RoomInfo)
        self.frame_17 = QtWidgets.QFrame(parent=self.frame_13)
        self.frame_17.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_RoomInfo_Home = QtWidgets.QPushButton(parent=self.frame_17)
        self.pushButton_RoomInfo_Home.setText("")
        self.pushButton_RoomInfo_Home.setObjectName("pushButton_RoomInfo_Home")
        self.horizontalLayout_9.addWidget(self.pushButton_RoomInfo_Home, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.pushButton_RoomInfo_Back = QtWidgets.QPushButton(parent=self.frame_17)
        self.pushButton_RoomInfo_Back.setText("")
        self.pushButton_RoomInfo_Back.setObjectName("pushButton_RoomInfo_Back")
        self.horizontalLayout_9.addWidget(self.pushButton_RoomInfo_Back, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_26.addWidget(self.frame_17, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.verticalLayout_25.addWidget(self.frame_13)
        self.stackedWidget.addWidget(self.page_RoomInfo)
        self.page_Test = QtWidgets.QWidget()
        self.page_Test.setObjectName("page_Test")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_Test)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_Test = QtWidgets.QFrame(parent=self.page_Test)
        self.frame_Test.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_Test.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_Test.setObjectName("frame_Test")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_Test)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.frame_29 = QtWidgets.QFrame(parent=self.frame_Test)
        self.frame_29.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_29.setObjectName("frame_29")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_29)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushButton_Test0 = QtWidgets.QPushButton(parent=self.frame_29)
        self.pushButton_Test0.setObjectName("pushButton_Test0")
        self.horizontalLayout_13.addWidget(self.pushButton_Test0)
        self.pushButton_Test1 = QtWidgets.QPushButton(parent=self.frame_29)
        self.pushButton_Test1.setObjectName("pushButton_Test1")
        self.horizontalLayout_13.addWidget(self.pushButton_Test1)
        self.pushButton_Test2 = QtWidgets.QPushButton(parent=self.frame_29)
        self.pushButton_Test2.setObjectName("pushButton_Test2")
        self.horizontalLayout_13.addWidget(self.pushButton_Test2)
        self.verticalLayout_21.addWidget(self.frame_29)
        self.scrollArea_Test = QtWidgets.QScrollArea(parent=self.frame_Test)
        self.scrollArea_Test.setWidgetResizable(True)
        self.scrollArea_Test.setObjectName("scrollArea_Test")
        self.scrollAreaWidgetContents_Test = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_Test.setGeometry(QtCore.QRect(0, 0, 563, 326))
        self.scrollAreaWidgetContents_Test.setObjectName("scrollAreaWidgetContents_Test")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_Test)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.frame_ScrollAreaTest = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents_Test)
        self.frame_ScrollAreaTest.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_ScrollAreaTest.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_ScrollAreaTest.setObjectName("frame_ScrollAreaTest")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frame_ScrollAreaTest)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.frame_27 = QtWidgets.QFrame(parent=self.frame_ScrollAreaTest)
        self.frame_27.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_27.setObjectName("frame_27")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_27)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_17 = QtWidgets.QLabel(parent=self.frame_27)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_11.addWidget(self.label_17)
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_27)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_11.addWidget(self.pushButton)
        self.verticalLayout_23.addWidget(self.frame_27)
        self.frame_28 = QtWidgets.QFrame(parent=self.frame_ScrollAreaTest)
        self.frame_28.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_28.setObjectName("frame_28")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_28)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_18 = QtWidgets.QLabel(parent=self.frame_28)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_12.addWidget(self.label_18)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame_28)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_12.addWidget(self.pushButton_2)
        self.verticalLayout_23.addWidget(self.frame_28)
        self.verticalLayout_22.addWidget(self.frame_ScrollAreaTest)
        self.scrollArea_Test.setWidget(self.scrollAreaWidgetContents_Test)
        self.verticalLayout_21.addWidget(self.scrollArea_Test)
        self.verticalLayout_2.addWidget(self.frame_Test)
        self.stackedWidget.addWidget(self.page_Test)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_ToLeft.setText(_translate("MainWindow", "<"))
        self.pushButton_ToRight.setText(_translate("MainWindow", ">"))
        self.label.setText(_translate("MainWindow", "THIẾT BỊ HỖ TRỢ KIỂM KÊ TÀI SẢN\n"
"T07.NVKH.2023.P7.03"))
        self.pushButton_Test.setText(_translate("MainWindow", "Test"))
        self.label_2.setText(_translate("MainWindow", "Đăng nhập vào thiết bị"))
        self.label_3.setText(_translate("MainWindow", "Tài khoản:"))
        self.label_4.setText(_translate("MainWindow", "Mật khẩu:"))
        self.pushButton_Login.setText(_translate("MainWindow", "Đăng nhập"))
        self.pushButton_ForgotPassword.setText(_translate("MainWindow", "Quên mật khẩu"))
        self.label_8.setText(_translate("MainWindow", "GIAO DIỆN CHÍNH"))
        self.label_5.setText(_translate("MainWindow", "1."))
        self.pushButton_Rooms.setText(_translate("MainWindow", "Danh sách phòng máy"))
        self.label_6.setText(_translate("MainWindow", "2."))
        self.pushButton_Check.setText(_translate("MainWindow", "Kiểm kê tài sản"))
        self.label_7.setText(_translate("MainWindow", "3."))
        self.pushButton_3.setText(_translate("MainWindow", "Kiểm tra thiết bị"))
        self.label_Rooms_Tittle.setText(_translate("MainWindow", "Danh sách phòng máy"))
        self.label_10.setText(_translate("MainWindow", "Tìm kiếm:"))
        self.label_11.setText(_translate("MainWindow", "Đơn vị:"))
        self.comboBox_RoomSearchOptions_DonVi.setItemText(0, _translate("MainWindow", "a"))
        self.comboBox_RoomSearchOptions_DonVi.setItemText(1, _translate("MainWindow", "b"))
        self.comboBox_RoomSearchOptions_DonVi.setItemText(2, _translate("MainWindow", "c"))
        self.label_RoomInfo_TenPhong.setText(_translate("MainWindow", "Ten Phong"))
        self.pushButton_RoomInfo_Info.setText(_translate("MainWindow", "Thông tin"))
        self.pushButton_RoomInfo_DanhMuc.setText(_translate("MainWindow", "Danh mục"))
        self.pushButton_RoomInfo_KiemKe.setText(_translate("MainWindow", "Kiểm kê tài sản"))
        self.pushButton_Test0.setText(_translate("MainWindow", "0"))
        self.pushButton_Test1.setText(_translate("MainWindow", "1"))
        self.pushButton_Test2.setText(_translate("MainWindow", "2"))
        self.label_17.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label_18.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
