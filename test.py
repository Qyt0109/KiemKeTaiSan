from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class AssetTable(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Asset Table")
        self.setGeometry(100, 100, 800, 600)  # Set the window size

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.setup_ui()

    def setup_ui(self):
        # Create a table widget
        table = QTableWidget(self)
        table.setRowCount(4)  # Set the number of rows
        table.setColumnCount(6)  # Set the number of columns

        # Set table headers
        table.setHorizontalHeaderLabels(["STT", "Mã tài sản", "Tên tài sản", "Số lượng", "Trạng thái", "Chức năng"])

        # Fill in the table data
        data = [
            ["I. Nhóm thiết bị máy tính", "", "", "", "", ""],
            ["1", "A", "B", "C", "D", "E"],
            ["2", "A", "B", "C", "D", "E"],
            ["II. Nhóm thiết bị mạng", "", "", "", "", ""]
        ]

        for row, row_data in enumerate(data):
            for col, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                table.setItem(row, col, item)

        # Resize columns to contents
        table.resizeColumnsToContents()

        # Merge cells in the first row
        table.setSpan(0, 0, 1, 6)

        # Set fixed sizes for rows and columns
        for i in range(table.rowCount()):
            table.setRowHeight(i, 25)  # Set a fixed row height

        for i in range(table.columnCount()):
            table.setColumnWidth(i, table.columnWidth(i))  # Set a fixed column width

        # Set up a layout
        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(table)

if __name__ == "__main__":
    app = QApplication([])
    window = AssetTable()
    window.show()
    app.exec()
