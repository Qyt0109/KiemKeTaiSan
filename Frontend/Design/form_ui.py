# Form implementation generated from reading ui file '/Applications/CODESTUFF/KiemKeTaiSan/Frontend/Design/form.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(452, 236)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_TenKhu = QtWidgets.QLabel(parent=Form)
        self.label_TenKhu.setObjectName("label_TenKhu")
        self.verticalLayout.addWidget(self.label_TenKhu)
        self.frame_Phongs = QtWidgets.QFrame(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_Phongs.sizePolicy().hasHeightForWidth())
        self.frame_Phongs.setSizePolicy(sizePolicy)
        self.frame_Phongs.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_Phongs.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_Phongs.setObjectName("frame_Phongs")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_Phongs)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_P1 = QtWidgets.QPushButton(parent=self.frame_Phongs)
        self.pushButton_P1.setObjectName("pushButton_P1")
        self.gridLayout_3.addWidget(self.pushButton_P1, 0, 1, 1, 1)
        self.pushButton_P0 = QtWidgets.QPushButton(parent=self.frame_Phongs)
        self.pushButton_P0.setObjectName("pushButton_P0")
        self.gridLayout_3.addWidget(self.pushButton_P0, 0, 0, 1, 1)
        self.pushButton_P2 = QtWidgets.QPushButton(parent=self.frame_Phongs)
        self.pushButton_P2.setObjectName("pushButton_P2")
        self.gridLayout_3.addWidget(self.pushButton_P2, 0, 2, 1, 1)
        self.pushButton_P3 = QtWidgets.QPushButton(parent=self.frame_Phongs)
        self.pushButton_P3.setObjectName("pushButton_P3")
        self.gridLayout_3.addWidget(self.pushButton_P3, 1, 0, 1, 1)
        self.pushButton_P4 = QtWidgets.QPushButton(parent=self.frame_Phongs)
        self.pushButton_P4.setObjectName("pushButton_P4")
        self.gridLayout_3.addWidget(self.pushButton_P4, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_Phongs)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_TenKhu.setText(_translate("Form", "Khu vực nhà D"))
        self.pushButton_P1.setText(_translate("Form", "Pxxx"))
        self.pushButton_P0.setText(_translate("Form", "Pxxx"))
        self.pushButton_P2.setText(_translate("Form", "Pxxx"))
        self.pushButton_P3.setText(_translate("Form", "Pxxx"))
        self.pushButton_P4.setText(_translate("Form", "Pxxx"))
