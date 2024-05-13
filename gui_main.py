import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QScrollArea
from PyQt5.QtWidgets import QHBoxLayout, QSpacerItem,QLineEdit, QSizePolicy, QLabel, QLayout
from gui_box_student import StudentWidget
from gui_table import MyTableWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        
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
        
        btnDisplayStudents = QPushButton("Display Students")
        btnDisplayCourses = QPushButton("Display Courses")
        searchBar = QLineEdit()
        searchBar.setPlaceholderText("Search...")
        
        hLayoutHeader.addWidget(btnDisplayStudents)
        hLayoutHeader.addWidget(btnDisplayCourses)
        hLayoutHeader.addItem(hSpacer)
        hLayoutHeader.addWidget(searchBar)
        
        # SECOND ROW
        
        # THIRD ROW
        my_table_widget = MyTableWidget()
        vLayout.addWidget(my_table_widget)
        
        # FOURTH ROW
        
        hLayoutFooter = QHBoxLayout()
        vLayout.addLayout(hLayoutFooter)
        labelStatus = QLabel("Status will be displayed here.")
        btnAddItem = QPushButton("+ Add New Student")
        
        hLayoutFooter.addWidget(labelStatus)
        hLayoutFooter.addItem(hSpacer)
        hLayoutFooter.addWidget(btnAddItem)
        
    def add100randomstudents(self):
        for i in range(1, 101):  # Range starts from 1 because we already have student1 and student2
            studentID = f"0000-{i:04}"  # Format studentID as a 4-digit number
            studentName = f"Student 00{i}"
            courseID = f"CSE{i%100}"  # Cycle through courses CSE101, CSE102,..., CSE100
            yearLevel = i % 10  # Cycle through year levels 1 to 10
            gender = "Male" if i % 2 == 0 else "Female"  # Alternate between Male and Female

            # Create a new StudentWidget instance
            student = StudentWidget(studentID, studentName, courseID, yearLevel, gender)
            
            # Add the StudentWidget instance to the QVBoxLayout
            self.vLayoutScrollArea.addWidget(student)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Set Stylesheet
    with open('styles.qss', 'r') as f:
        styleSheet = f.read()

    window = MainWindow()
    window.setStyleSheet(styleSheet)
    
    window.show()
    sys.exit(app.exec_())