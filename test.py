import sys
import PyQt6
from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView, QPushButton
from PyQt6.QtCore import Qt

class ResponsiveTableExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Responsive Table Example')

        # Create a QTableWidget
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3'])

        # Populate the table with dummy data and buttons
        self.populateTable()

        # Create a layout and set it for the main window
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        # Set up responsive resizing
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)
        """
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        """

    def populateTable(self):
        data = [
            ['Row 1', 'Data 1', 'Description 1', 'A', 'B', 'C'],
            ['Row 2', 'Data 2', 'Description 2', 'D', 'E', 'F'],
            ['Row 3', 'Data 3', 'Description 3', 'G', 'H', 'I'],
            ['Row 4', 'Data 4', 'Description 4', 'J', 'K', 'L'],
        ]

        self.tableWidget.setRowCount(len(data))

        for row, rowData in enumerate(data):
            for col, item in enumerate(rowData):
                if col == self.tableWidget.columnCount() - 1:
                    # Add a button to the last cell of each row
                    button = QPushButton('Click me', self)
                    self.tableWidget.setCellWidget(row, col, button)
                else:
                    qitem = QTableWidgetItem(item)
                    qitem.setFlags(qitem.flags() & ~Qt.ItemFlag.ItemIsEditable)
                    self.tableWidget.setItem(row, col, qitem)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ResponsiveTableExample()
    window.show()
    sys.exit(app.exec())
