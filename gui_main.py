import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QComboBox, QCompleter
from PyQt5.QtWidgets import QHBoxLayout, QSpacerItem,QLineEdit, QSizePolicy, QLabel, QFrame
from PyQt5.QtCore import Qt, QRect
from gui_table import MyTableWidget
from gui_popups import StudentDialog, CourseDialog
from utils_crud import CRUDLClass

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.student_dialog = None

    def init_ui(self):
        self.displayModeIsStudent = True
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
        
        self.btnClearSearch = QPushButton("CLEAR")
        hLayoutHeader.addWidget(self.btnClearSearch)
        
        # SECOND ROW
        
        self.displayLabel = QLabel("\nNOW DISPLAYING TABLE: STUDENTS")  # Create the label
        self.displayLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.displayLabel.setAlignment(Qt.AlignCenter)
        vLayout.addWidget(self.displayLabel)
        
        # THIRD ROW
        
        self.my_table_widget = MyTableWidget()
        vLayout.addWidget(self.my_table_widget)
        
        # FOURTH ROW
        
        hLayoutFooter = QHBoxLayout()
        vLayout.addLayout(hLayoutFooter)
        self.labelStatus = QLabel("Status will be displayed here.")
        self.btnDeselectAll = QPushButton("DESELECT ALL DISPLAYED")
        self.btnSelectAll = QPushButton("SELECT ALL DISPLAYED")
        self.btnAddItem = QPushButton("+ ADD STUDENT")
        self.btnEditItem = QPushButton("- EDIT STUDENT")
        self.btnDeleteItem = QPushButton("x DELETE STUDENT")
        
        hLayoutFooter.addWidget(self.labelStatus)
        hLayoutFooter.addItem(hSpacer)
        hLayoutFooter.addWidget(self.btnDeselectAll)
        self.btnDeselectAll.setVisible(False)
        hLayoutFooter.addWidget(self.btnSelectAll)
        self.btnSelectAll.setVisible(False)
        hLayoutFooter.addWidget(self.btnAddItem)
        hLayoutFooter.addWidget(self.btnEditItem)
        hLayoutFooter.addWidget(self.btnDeleteItem)
        
        # SIGNALS
        self.btnAddItem.clicked.connect(self.open_student_create_dialog)
        self.btnEditItem.clicked.connect(self.open_student_edit_dialog)
        self.btnDeleteItem.clicked.connect(self.open_delete_dialog)
        self.my_table_widget.checkBoxCountChanged.connect(self.updateStatusLabel)
        self.btnDeselectAll.clicked.connect(lambda: self.my_table_widget.checkAllDisplayed(False))
        self.btnSelectAll.clicked.connect(lambda: self.my_table_widget.checkAllDisplayed(True))
        self.btnClearSearch.clicked.connect(self.clearSearchBar)
        # FUNCTIONALITY AND SETUP
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
    
    def clearSearchBar(self):
        self.searchBarName.setText('')
        self.searchBarIDNum.setText('')
        self.searchCourse.setCurrentIndex(0)
        self.searchYearLevel.setCurrentIndex(0)
        self.searchGender.setCurrentIndex(0)
        self.searchStatus.setCurrentIndex(0)
        self.searchCourse.clear()
        self.searchBarHandler()
    
    def open_student_create_dialog(self):
        dialog = StudentDialog()
        dialog.dialogClosed.connect(self.refreshTable)
        dialog.formSubmit.connect(self.refreshTable)
        dialog.exec()

    
    def open_student_edit_dialog(self):
        selected_students = self.my_table_widget.getCheckedKeys()
        if not selected_students:
            self.setStatus("No students selected")
            return

        if len(selected_students) == 1:
            student_id = selected_students[0]
            data = self.cc.readStudent(student_id)
            dialog = StudentDialog(student_id=data[0], student_name=data[1], course_id=data[2], year_level=data[3], gender=data[4])
        else:
            dialog = StudentDialog(multiple=True, student_ids=self.my_table_widget.getCheckedKeys())
        
        dialog.dialogClosed.connect(self.refreshTable)
        dialog.formSubmit.connect(self.refreshTable)
        dialog.exec()
        
    def open_delete_dialog(self):
        self.setStatus(self.my_table_widget.deleteSelectedItems(self.displayModeIsStudent))
        self.refreshTable()

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

        if not self.displayModeIsStudent:
            search_params = {
                'searchItem': 'CourseID',
                'searchQuery': self.searchBarIDNum.text().strip()
            } if self.searchBarIDNum.text().strip() else {
                'searchItem': 'CourseDesc',
                'searchQuery': self.searchBarName.text().strip()
            }

        for key in list(search_params.keys()):
            if not isinstance(search_params[key], int) and (search_params[key] == '' or search_params[key][:3] == 'No '):
                del search_params[key]
            elif isinstance(search_params[key], int) and search_params[key] < 0:
                del search_params[key]

        
        if not search_params or not self.displayModeIsStudent:
            self.btnSelectAll.setVisible(False)
            self.btnDeselectAll.setVisible(False)
        elif search_params:
            self.btnSelectAll.setVisible(True)
            self.btnDeselectAll.setVisible(True)
        self.my_table_widget.setTableContents(self.displayModeIsStudent, **search_params)
        self.updateStatusLabel()
        
    def toggle_display(self):
        incc = CRUDLClass()
        self.displayModeIsStudent = not self.displayModeIsStudent
        self.searchBarName.setText('')
        self.searchBarIDNum.setText('')
        self.searchCourse.setCurrentIndex(0)
        self.searchYearLevel.setCurrentIndex(0)
        self.searchGender.setCurrentIndex(0)
        self.searchStatus.setCurrentIndex(0)
        self.searchCourse.clear()
        courses = incc.listCourseKeys()
        courseList = []
        courseList.append("No Course Specified")
        for course in courses:
            print("Courses fetched:", course)
            courseList.append(f"{course}")
        courseList.pop(1) 
        self.searchCourse.addItems(courseList)
        self.btnEditItem.clicked.disconnect()
        self.btnDeleteItem.clicked.disconnect()
        self.btnAddItem.clicked.disconnect()
        if self.displayModeIsStudent:
            self.btnEditItem.clicked.connect(self.open_student_edit_dialog)
            self.btnDeleteItem.clicked.connect(self.open_delete_dialog)
            self.btnAddItem.clicked.connect(self.open_student_create_dialog)
            self.btnToggleDisplay.setText('Display Courses')
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
            self.btnSelectAll.setVisible(True)
            self.btnDeselectAll.setVisible(True)
        else:
            self.btnEditItem.clicked.connect(self.open_course_edit_dialog)
            self.btnDeleteItem.clicked.connect(self.open_delete_dialog)
            self.btnAddItem.clicked.connect(self.open_course_create_dialog)
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
            self.btnDeleteItem.setText("x DELETE COURSE")
            self.btnSelectAll.setVisible(False)
            self.btnDeselectAll.setVisible(False)
        self.searchBarHandler()
            
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

    def refreshTable(self):
        self.searchBarHandler()
        
    def updateStatusLabel(self):
        count = self.my_table_widget.countCheckedBoxes()
        if count == 0:
            item_type = "student" if self.displayModeIsStudent else "course"
            self.setStatus(f"No {item_type}s selected")
            self.btnEditItem.setText(f"- EDIT {item_type.upper()}")
            self.btnEditItem.setStyleSheet("background-color: lightgray;")
            self.btnEditItem.setEnabled(False)
            self.btnDeleteItem.setText(f"x DELETE {item_type.upper()}")
            self.btnDeleteItem.setStyleSheet("background-color: lightgray;")
            self.btnDeleteItem.setEnabled(False)
        elif count == 1:
            item_type = "student" if self.displayModeIsStudent else "course"
            self.setStatus(f"1 {item_type} selected")
            self.btnEditItem.setText(f"- EDIT {item_type.upper()}")
            self.btnEditItem.setStyleSheet("")
            self.btnEditItem.setEnabled(True)
            self.btnDeleteItem.setText(f"x DELETE {item_type.upper()}")
            self.btnDeleteItem.setStyleSheet("")
            self.btnDeleteItem.setEnabled(True)
        else:
            item_type = "students" if self.displayModeIsStudent else "courses"
            self.setStatus(f"{count} {item_type} selected")
            self.btnEditItem.setText(f"- EDIT {item_type.upper()}")
            self.btnEditItem.setStyleSheet("")
            self.btnEditItem.setEnabled(True)
            self.btnDeleteItem.setText(f"x DELETE {item_type.upper()}")
            self.btnDeleteItem.setStyleSheet("")
            self.btnDeleteItem.setEnabled(True)
            if not self.displayModeIsStudent:
                self.btnEditItem.setText(f"- EDIT COURSE")
                self.btnEditItem.setStyleSheet("background-color: lightgray;")
                self.btnEditItem.setEnabled(False)
            
    def open_course_create_dialog(self):
        dialog = CourseDialog()
        dialog.dialogClosed.connect(self.refreshTable)
        dialog.formSubmit.connect(self.refreshTable)
        dialog.exec()

    def open_course_edit_dialog(self):
        selected_courses = self.my_table_widget.getCheckedKeys()
        if not selected_courses:
            self.setStatus("No courses selected")
            return
        if len(selected_courses) == 1:
            course_id = selected_courses[0]
            data = self.cc.readCourse(course_id)
            if data is not None: 
                dialog = CourseDialog(course_id=data[0], course_desc=data[1])
            else:
                self.setStatus("Failed to load course data")
        else:
            self.setStatus("Cannot edit multiple courses at once")


        dialog.dialogClosed.connect(self.refreshTable)
        dialog.formSubmit.connect(self.refreshTable)
        dialog.exec()
                
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Set Stylesheet
    with open('styles.qss', 'r') as f:
        styleSheet = f.read()

    window = MainWindow()
    window.setStyleSheet(styleSheet)
    
    window.show()
    sys.exit(app.exec_())