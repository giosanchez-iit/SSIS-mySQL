import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QComboBox, QCompleter
from PyQt5.QtWidgets import QHBoxLayout, QSpacerItem,QLineEdit, QSizePolicy, QLabel, QLayout
from PyQt5.QtCore import Qt
from gui_table import MyTableWidget
from gui_popups import StudentDialog
from utils_crud import CRUDLClass

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.displayModeIsStudent = True

    def init_ui(self):
        self.cc = CRUDLClass()
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
        
        self.searchBarIDNum = QLineEdit()
        self.searchBarIDNum.setPlaceholderText("Search ID Number...")
        self.searchBarName = QLineEdit()
        self.searchBarName.setPlaceholderText("Search Student Name...")
        
        self.searchCourse = QComboBox(self) 
        courses = self.cc.listCourses()
        courseList = []
        courseList.append("No Course Specified")
        for course in courses:
            courseList.append(f"{course[0]}")
        courseList.pop(1) 
        self.searchCourse.addItems(courseList)
        self.searchCourse.setEditable(True)
        completer = QCompleter(self.searchCourse)
        self.searchCourse.setCompleter(completer)
        
        self.searchYearLevel = QComboBox(self)
        self.searchYearLevel.addItems(['No Year Level Specified', '1', '2', '3', '4', '5'])
        self.searchGender = QComboBox(self)
        self.searchGender.addItems(['No Gender Specified','Man', 'Woman', 'Non-Binary', 'Other'])   
        self.searchStatus = QComboBox(self)
        self.searchStatus.addItems(['No Status Specified', 'Not Enrolled', 'Enrolled'])  
        
        self.searchCourse.setMaximumWidth(100)
        self.searchYearLevel.setMaximumWidth(50)
        self.searchGender.setMaximumWidth(50)
        self.searchStatus.setMaximumWidth(50)
        
        hLayoutHeader.addWidget(self.btnToggleDisplay)
        hLayoutHeader.addItem(hSpacer)
        hLayoutHeader.addWidget(QLabel("Search:"))
        hLayoutHeader.addWidget(self.searchBarIDNum)
        hLayoutHeader.addWidget(self.searchBarName)
        hLayoutHeader.addWidget(self.searchCourse)
        hLayoutHeader.addWidget(self.searchYearLevel)
        hLayoutHeader.addWidget(self.searchGender)
        hLayoutHeader.addWidget(self.searchStatus)
        
        # SECOND ROW

        self.displayLabel = QLabel("\nNOW DISPLAYING TABLE: STUDENTS")  # Create the label
        self.displayLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.displayLabel.setAlignment(Qt.AlignCenter)
        vLayout.addWidget(self.displayLabel)  # Add the label to the layout
        
        # THIRD ROW
        
        self.my_table_widget = MyTableWidget()
        vLayout.addWidget(self.my_table_widget)
        
        # FOURTH ROW
        
        hLayoutFooter = QHBoxLayout()
        vLayout.addLayout(hLayoutFooter)
        self.labelStatus = QLabel("Status will be displayed here.")
        self.btnAddItem = QPushButton("+ ADD STUDENT")
        self.btnEditItem = QPushButton("- EDIT STUDENT")
        self.btnDeleteItem = QPushButton("x DELETE STUDENT")
        
        hLayoutFooter.addWidget(self.labelStatus)
        hLayoutFooter.addItem(hSpacer)
        hLayoutFooter.addWidget(self.btnAddItem)
        hLayoutFooter.addWidget(self.btnEditItem)
        hLayoutFooter.addWidget(self.btnDeleteItem)
        
        # FUNCTIONALITY AND SETUP
        self.btnAddItem.clicked.connect(self.open_student_dialog)
        self.btnToggleDisplay.clicked.connect(self.toggle_display)
        self.my_table_widget.setTableContents(True)
        self.searchBarName.textChanged.connect(self.searchBarHandler)
        self.searchBarIDNum.textChanged.connect(self.searchBarHandler)
        self.searchCourse.currentIndexChanged.connect(self.searchBarHandler)
        self.searchGender.currentIndexChanged.connect(self.searchBarHandler)
        self.searchYearLevel.currentIndexChanged.connect(self.searchBarHandler)
        self.searchStatus.currentIndexChanged.connect(self.searchBarHandler)
        self.searchCourse.currentIndexChanged.connect(self.comboboxCourseDisabler)
        self.searchStatus.currentIndexChanged.connect(self.comboBoxStatusDisabler)
        self.disablecombobox(self.searchCourse) if self.searchCourse.currentIndex() == 0 else self.enablecombobox(self.searchCourse) 
        self.disablecombobox(self.searchYearLevel) if self.searchYearLevel.currentIndex() == 0 else self.enablecombobox(self.searchYearLevel) 
        self.disablecombobox(self.searchGender) if self.searchGender.currentIndex() == 0 else self.enablecombobox(self.searchGender) 
        self.disablecombobox(self.searchStatus) if self.searchStatus.currentIndex() == 0 else self.enablecombobox(self.searchStatus) 
        
    def setStatus(self, message):
        self.labelStatus.setText(message)
        
    def open_student_dialog(self):
        dialog = StudentDialog()
        dialog.exec()
         
    def displayOnlySearched(self):
        self.my_table_widget.table.clearContents()
        self.my_table_widget.table.setRowCount(0)
        if(self.displayModeIsStudent):
            self.cc.doForEachStudent(self.my_table_widget.insertAtBottom, searchQuery=self.searchBar.text().strip(), searchItem=self.searchCategory.currentText().strip())
        else:
            self.cc.doForEachCourse(self.my_table_widget.insertAtBottom, searchQuery=self.searchBar.text().strip(), searchItem=self.searchCategory.currentText().strip())
            
    def searchBarHandler(self):
        
        self.disablecombobox(self.searchCourse) if self.searchCourse.currentIndex() == 0 else self.enablecombobox(self.searchCourse) 
        self.disablecombobox(self.searchYearLevel) if self.searchYearLevel.currentIndex() == 0 else self.enablecombobox(self.searchYearLevel) 
        self.disablecombobox(self.searchGender) if self.searchGender.currentIndex() == 0 else self.enablecombobox(self.searchGender) 
        self.disablecombobox(self.searchStatus) if self.searchStatus.currentIndex() == 0 else self.enablecombobox(self.searchStatus) 
            
        search_params = {
            'studentID': self.searchBarIDNum.text().strip(),
            'studentName': self.searchBarName.text().strip(),
            'courseID': self.searchCourse.currentText().strip(),
            'yearLevel': self.searchYearLevel.currentText().strip(),
            'gender': self.searchGender.currentText().strip(),
            'isEnrolled': (self.searchStatus.currentIndex() - 1)
        }
        for key in list(search_params.keys()):  # Convert keys to list to avoid RuntimeError
            if not isinstance(search_params[key], int) and (search_params[key] == '' or search_params[key][:3] == 'No '):
                del search_params[key]
            elif isinstance(search_params[key], int) and search_params[key]<0:
                del search_params[key]

        self.my_table_widget.setTableContents(self.displayModeIsStudent, **search_params)
        
        
    def toggle_display(self):
        self.displayModeIsStudent = not self.displayModeIsStudent
        self.my_table_widget.setTableContents(self.displayModeIsStudent)
        self.searchBarName.setText('')
        self.searchBarIDNum.setText('')
        self.searchCourse.setCurrentIndex(0)
        self.searchYearLevel.setCurrentIndex(0)
        self.searchGender.setCurrentIndex(0)
        self.searchStatus.setCurrentIndex(0)
        self.searchCourse.clear()
        if self.displayModeIsStudent:
            self.btnToggleDisplay.setText('Display Courses')
            self.searchCourse.addItems(["No Course Specified", "StudentID", "StudentName", "CourseID", "YearLevel", "Gender", "isEnrolled"])
            self.setStatus('Now Displaying Students')
            self.displayLabel.setText("\nNOW DISPLAYING TABLE: STUDENTS")
            self.btnAddItem.setText("+ ADD STUDENT")
            self.searchBarName.setPlaceholderText("Search Student Name...")
            self.searchBarIDNum.setPlaceholderText("Search ID Number...")
            self.searchCourse.setVisible(True)
            self.searchYearLevel.setVisible(True)
            self.searchGender.setVisible(True)
            self.searchStatus.setVisible(True)
            self.btnAddItem.setText("+ ADD STUDENT")
            self.btnEditItem.setText("- EDIT STUDENT")
            self.btnDeleteItem.setText("x DELETE STUDENT")
        else:
            self.btnToggleDisplay.setText('Display Students')
            self.setStatus('Now Displaying Courses')
            self.displayLabel.setText("\nNOW DISPLAYING TABLE: COURSES")
            self.btnAddItem.setText("+ ADD COURSE")
            self.searchBarName.setPlaceholderText("Search Course Description...")
            self.searchBarIDNum.setPlaceholderText("Search Course Code...")
            self.searchCourse.setVisible(False)
            self.searchYearLevel.setVisible(False)
            self.searchGender.setVisible(False)
            self.searchStatus.setVisible(False)
            self.btnAddItem.setText("+ ADD COURSE")
            self.btnEditItem.setText("- EDIT COURSE")
            
    def comboboxCourseDisabler(self):
        if self.searchCourse.currentIndex()!= 0 and self.searchStatus.currentIndex() == 1 :
            self.searchStatus.setCurrentIndex(0)

    def comboBoxStatusDisabler(self):
        if self.searchCourse.currentIndex() != 0 and self.searchStatus.currentIndex() == 1:
                self.searchCourse.setCurrentIndex(0)
                
    def disablecombobox(self, combobox):
        combobox.setStyleSheet("""
            QComboBox{
                color: #d0d0d0; /* Text color for disabled state */
            }
            QComboBox::drop-down {
                color: black; /* Dropdown arrow color for disabled state */
            }
        """)

    def enablecombobox(self, combobox):
        combobox.setStyleSheet("""
            QComboBox{
                color: #000000; /* Text color for disabled state */
            }
            QComboBox::drop-down {
                color: black; /* Dropdown arrow color for disabled state */
            }
        """)

            
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Set Stylesheet
    with open('styles.qss', 'r') as f:
        styleSheet = f.read()

    window = MainWindow()
    window.setStyleSheet(styleSheet)
    
    window.show()
    sys.exit(app.exec_())