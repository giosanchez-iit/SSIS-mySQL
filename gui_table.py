from PyQt5.QtWidgets import QWidget, QTableView, QVBoxLayout, QSizePolicy, QHeaderView
from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex
from utils_crud import CRUDLClass


class StudentTableModel(QAbstractTableModel):
    def __init__(self, data):
        super(StudentTableModel, self).__init__()
        self._data = data

    def rowCount(self, parent=QModelIndex()):
        return len(self._data) - 1

    def columnCount(self, parent=QModelIndex()):
        return len(self._data[0])

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid() and role == Qt.DisplayRole:
            return str(self._data[index.row() + 1][index.column()])
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return str(self._data[0][section])
        return None

class StudentTableWidget(QWidget):
    def __init__(self, parent=None):
        super(StudentTableWidget, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        cc = CRUDLClass()
        students = cc.listStudents()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.table_view = QTableView()
        self.table_view.setSelectionBehavior(QTableView.SelectRows)
        self.table_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        model = StudentTableModel(students)
        self.table_view.setModel(model)
        model = StudentTableModel(students)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table_view)
