import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout, QHeaderView
from PyQt5.QtCore import Qt
from utils_crud import CRUDLClass
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QColor

class MyTableWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
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
        
        # Disable the vertical header to remove row numbers
        self.table.verticalHeader().setVisible(False)
        
        for row in range(1, rows):  # Start from 1 since the first row is now the header
            for col in range(columns):
                if col == 0:
                    item = QTableWidgetItem(str(tableContents[row][col]))
                    item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
                    item.setCheckState(Qt.CheckState.Unchecked)
                    self.table.setItem(row-1, col, item)
                elif col == 5:
                    item = QTableWidgetItem('Enrolled') if tableContents[row][col] == 1 else QTableWidgetItem('Not Enrolled')
                    self.table.setItem(row-1, col, item)
                else:
                    self.table.setItem(row-1, col, QTableWidgetItem(str(tableContents[row][col])))
        
        self.table.setColumnCount(columns)
        self.table.setRowCount(rows)
        
        for i in range(self.table.columnCount()):
            if i != 1:
                self.table.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)
            else:
                self.table.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)
        
        self.table.itemClicked.connect(self.highlightRow)
    
    def highlightRow(self, item):
        if item.column() == 0:
            row = item.row()
            if item.checkState() == Qt.Checked:
                for col in range(self.table.columnCount()):
                    self.table.item(row, col).setBackground(QColor("#ffff00"))
            else:
                for col in range(self.table.columnCount()):
                    self.table.item(row, col).setBackground(QColor(Qt.white))
