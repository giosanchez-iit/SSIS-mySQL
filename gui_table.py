import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout, QHeaderView
from PyQt5.QtCore import Qt
from utils_crud import CRUDLClass
from PyQt5.QtGui import QColor

class MyTableWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        
        self.checkBoxCount = 0;
        
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        cc = CRUDLClass()
        
        columns = 6
        rows = cc.countStudents()+1
        tableContents = cc.listStudents()
        
        self.table = QTableWidget(rows, columns)
        self.table.setStyleSheet('font-family: "Atkinson Hyperlegible"; font-size: 12pt; QHeaderView::section { padding: 5px; } QAbstractItemView::indicator{width: 30px; height: 25px;} QTableWidget::item {width:500px; height:40px;} padding: 15px 5px;')
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.layout.addWidget(self.table)
        
        # Set the first row as the header
        header = (tableContents[0][i] for i in range(columns))
        self.table.setHorizontalHeaderLabels(header)
        self.table.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        
        # Disable the vertical header to remove row numbers
        self.table.verticalHeader().setVisible(False)
        
        # Disable manual editing of the table
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        # Call the new method to add students to the table
        self.addStudentsToTable(tableContents)
        
        self.table.setColumnCount(columns)
        self.table.setRowCount(rows)
        
        for i in range(self.table.columnCount()):
            if i!= 1:
                self.table.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)
            else:
                self.table.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)
        
        self.table.itemClicked.connect(self.highlightRow)

    def countCheckedBoxes(self):
        # Reset the counter before counting
        self.checkBoxCount = 0
        
        # Iterate over all rows in the first column
        for row in range(self.table.rowCount()):
            # Check if the item in the first column exists
            item = self.table.item(row, 0)
            if item is not None and item.checkState() == Qt.Checked:
                self.checkBoxCount += 1
        
        return self.checkBoxCount
    
    def highlightRow(self, item):
        if item.column() == 0:
            row = item.row()
            if item.checkState() == Qt.Checked:
                self.checkBoxCount += 1
                for col in range(self.table.columnCount()):
                    self.table.item(row, col).setBackground(QColor("#ffff00"))
            else:
                for col in range(self.table.columnCount()):
                    self.table.item(row, col).setBackground(QColor(Qt.white))
                    
    def setTableContents(self, displayModeIsStudent, **kwargs):
        cc = CRUDLClass()
        
        if displayModeIsStudent:
            new_table_contents = cc.listStudents(**kwargs)
        else:
            new_table_contents = cc.listCourses(**kwargs)
        
        self.table.clearContents()
        self.table.setRowCount(0)

        columns = len(new_table_contents[0]) if new_table_contents else 0
        self.table.setColumnCount(columns)

        self.table.setRowCount(len(new_table_contents) - 1 if new_table_contents else 0)

        header = (item for item in new_table_contents[0]) if new_table_contents else []
        self.table.setHorizontalHeaderLabels(header)

        for row, row_data in enumerate(new_table_contents[1:], start=1):  # Start from 1 to skip the header row
            for col, item in enumerate(row_data):
                if col == 0:
                    table_item = QTableWidgetItem(str(item))
                    table_item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
                    table_item.setCheckState(Qt.CheckState.Unchecked)
                elif col == 5:
                    table_item = QTableWidgetItem('Enrolled') if item == 1 else QTableWidgetItem('Not Enrolled')
                else:
                    table_item = QTableWidgetItem(str(item))
                self.table.setItem(row-1, col, table_item)

        self.checkBoxCount = 0  

        
    def insertAtBottom(self, studentData):
        rowPosition = self.table.rowCount()
        self.table.insertRow(rowPosition)
        
        for col, data in enumerate(studentData):
            if col == 0:
                table_item = QTableWidgetItem()
                table_item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
                table_item.setCheckState(Qt.CheckState.Unchecked)
            elif col == 5:
                table_item = QTableWidgetItem('Not Enrolled') if data == 0 else QTableWidgetItem('Enrolled')
            else:
                table_item = QTableWidgetItem(str(data))
                
            self.table.setItem(rowPosition, col, table_item)
        
    def addStudentsToTable(self, tableContents):
        for row in range(1, len(tableContents)):  # Start from 1 since the first row is now the header
            self.insertAtBottom(tableContents[row])
            