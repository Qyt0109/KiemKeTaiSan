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

from Backend.Database.db_sessions import *

"""
                           ┌────────────────────────┐                           
                           │┌──────────────────────┐│                           
┌───────────────────────┐  ││     label_TenKhu     ││                           
│┌─────────────────────┐│  │└──────────────────────┘│                           
││                     ││  │┌──────────────────────┐│  ┌───────────────────────┐
││    frame_Phongs     ├┼─▶││                      ││  │ ┌─────┐┌─────┐┌─────┐ │
││                     ││  ││                      ││  │ └─────┘└─────┘└─────┘ │
│└─────────────────────┘│  ││     Frame_Phongs     ├┼─▶│ ┌─────┐┌─────┐        │
│         . . .         │  ││                      ││  │ └─────┘└─────┘        │
│                       │  ││                      ││  └───────────────────────┘
│                       │  │└──────────────────────┘│        Frame_Phongs       
└───────────────────────┘  └────────────────────────┘                           
       Frame_Khus                  Frame_Khu                                    
"""
class Frame_Phongs(QFrame):
    def __init__(self, parent: QWidget, phongs:List[Phong], callback_pushButton_Phong=None) -> None:
        super().__init__(parent)
        # Empty Khu with no phong
        if not phongs:
            self.layout = QVBoxLayout(self)
            self.layout.addWidget(QLabel("Không có phòng nào thuộc khu này!"))
            return
        # Grid layout for Phongs
        self.layout = QGridLayout(self)
        # Calculate rows and columns based on the number of Phongs
        phongs = len(phongs)
        rows = (phongs - 1) // 5 + 1
        columns = min(phongs, 5)
        
        for i, phong in enumerate(phongs):
            pushButton_Phong = QPushButton(parent=self,
                                           text=f'P.{phong.ma}')
            if callback_pushButton_Phong:
                pushButton_Phong.clicked.connect(partial(callback_pushButton_Phong, phong=phong))
            # Calculate the row and column positions based on the index
            row_position = i // columns
            column_position = i % columns
            self.layout.addWidget(pushButton_Phong,
                                  row_position,
                                  column_position,
                                  1,
                                  1)

class Frame_Khu(QFrame):
    def __init__(self, parent: QWidget, khu:Khu, callback_pushButton_Phong=None) -> None:
        super().__init__(parent)
        self.layout = QVBoxLayout(parent=self)
        # Label for Khu
        label_TenKhu = QLabel(parent=self,
                              text=khu.ten)
        self.addWidget(label_TenKhu)
        # Frame for Phongs in Khu
        frame_Phongs = Frame_Phongs(parent=self,
                                    phongs=khu.phongs,
                                    callback_pushButton_Phong=callback_pushButton_Phong)
        self.layout.addWidget(frame_Phongs)

class Frame_Khus(QFrame):
    def __init__(self, parent: QWidget, khus:List[Khu], callback_pushButton_Phong=None) -> None:
        super().__init__(parent)
        self.layout = QVBoxLayout(parent=self)
        for khu in self.khus:
            if not khu.phongs:
                continue
            frame_Khu = Frame_Khu(parent=self,
                                  khu=khu,
                                  callback_pushButton_Phong=callback_pushButton_Phong)
            self.layout.addWidget(frame_Khu)
            