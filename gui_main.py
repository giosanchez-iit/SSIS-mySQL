import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QScrollArea
from PyQt5.QtWidgets import QHBoxLayout, QSpacerItem,QLineEdit, QSizePolicy, QLabel, QLayout
from PyQt5.QtCore import Qt
from gui_table import MyTableWidget
from gui_popups import StudentDialog

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.displayModeIsStudent = True

    def init_ui(self):
        
        self.setMouseTracking(True)
        
        # WINDOW
        
        self.setWindowTitle("Simple Student Information System")
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # Allow vertical resizing

        # SET VBOX AS MAIN LAYOUT
        
        vLayout = QVBoxLayout()
        self.setLayout(vLayout)
        
        # DEFINE H-SPACER TO RECYCLE
        hSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
       
        # FIRST ROW
        
        hLayoutHeader = QHBoxLayout()
        vLayout.addLayout(hLayoutHeader)
        
        self.btnToggleDisplay = QPushButton("Display Courses")
        self.searchBar = QLineEdit()
        self.searchBar.setPlaceholderText("Search...")
        
        hLayoutHeader.addWidget(self.btnToggleDisplay)
        hLayoutHeader.addItem(hSpacer)
        hLayoutHeader.addWidget(self.searchBar)
        
        # SECOND ROW
        
        # THIRD ROW
        self.my_table_widget = MyTableWidget()
        vLayout.addWidget(self.my_table_widget)
        
        # FOURTH ROW
        
        hLayoutFooter = QHBoxLayout()
        vLayout.addLayout(hLayoutFooter)
        self.labelStatus = QLabel("Status will be displayed here.")
        self.btnAddItem = QPushButton("+ ADD STUDENT")
        
        hLayoutFooter.addWidget(self.labelStatus)
        hLayoutFooter.addItem(hSpacer)
        hLayoutFooter.addWidget(self.btnAddItem)
        
        # FUNCTIONALITY
        self.btnAddItem.clicked.connect(self.open_student_dialog)
        self.btnToggleDisplay.clicked.connect(self.toggle_display)
        
        
    def setStatus(self, message):
        self.labelStatus.setText(message)
        
    def mousePressEvent(self, event):
        print (self.my_table_widget.countCheckedBoxes())
        
    def open_student_dialog(self):
        dialog = StudentDialog()
        dialog.exec()
        
        
    def toggle_display(self):
        self.displayModeIsStudent = not self.displayModeIsStudent
        self.my_table_widget.setTableContents(self.displayModeIsStudent)
        if self.displayModeIsStudent:
            self.searchBar.setText('')
        

            
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Set Stylesheet
    with open('styles.qss', 'r') as f:
        styleSheet = f.read()

    window = MainWindow()
    window.setStyleSheet(styleSheet)
    
    window.show()
    sys.exit(app.exec_())