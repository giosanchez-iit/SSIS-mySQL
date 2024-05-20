import sys
from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QLineEdit, QComboBox, QLabel, QPushButton, QHBoxLayout, QMessageBox, QSizePolicy
from PyQt5.QtCore import pyqtSignal
from utils_crud import CRUDLClass

class StudentDialog(QDialog):
    dialogClosed = pyqtSignal() 
    formSubmit = pyqtSignal()
    
    def __init__(self, student_id=None, student_name=None, course_id=None, year_level=None, gender=None, multiple = False, student_ids=None):
        super().__init__()
        self.setWindowTitle("Student Information")
        self.setGeometry(100, 100, 400, 200)  
        with open('styles.qss', 'r') as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)
        
        self.crudl_class = CRUDLClass(failure_action=self.printError, success_action=self.printError)

        # Initialize fields as null
        self.student_id1 = QLineEdit(self)
        self.student_id2 = QLineEdit(self)
        self.student_name = QLineEdit(self)
        self.course_id = QComboBox(self)
        self.year_level = QComboBox(self)
        self.gender = QComboBox(self)
        self.multiple = multiple
        self.student_id = student_id
        self.student_ids = student_ids
            
            
        # Make the button ahead
        self.button = QPushButton("Submit", self)
        self.button.clicked.connect(self.submit)
        
        # Populate combo boxes
        courses = self.crudl_class.listCourses()
        self.course_id.addItem('None')
        self.year_level.addItem('None')
        self.gender.addItem('None')
        self.course_id.setCurrentIndex(0)
        self.year_level.setCurrentIndex(0)
        self.gender.setCurrentIndex(0)
        courseList = []
        for course in courses[1:]:
            courseList.append(f"{course[0]}")
        self.course_id.addItems(courseList)
        self.year_level.addItems([str(i) for i in range(1, 6)])
        self.gender.addItems(["Man", "Woman", "Non-Binary", "Other"])

        # Set default values and editability based on student ID  
        if multiple: #edit multiple
            self.student_id1.setEnabled(False)
            self.student_id1.setStyleSheet("background-color: lightgray;")
            self.student_id2.setEnabled(False)
            self.student_id2.setStyleSheet("background-color: lightgray;")
            self.student_name.setEnabled(False)
            self.student_name.setText("-- multiple selected --")
            self.student_name.setStyleSheet("background-color: lightgray;")
            self.course_id.setCurrentIndex(-1)
            self.year_level.setEnabled(False)
            self.year_level.setCurrentIndex(-1)
            self.year_level.setStyleSheet("background-color: lightgray;")
            self.gender.setEnabled(False)
            self.gender.setCurrentIndex(-1)
            self.gender.setStyleSheet("background-color: lightgray;") 
            self.button.setText("Edit All")   
        elif student_id: #edit
            self.student_id1.setText(student_id[:4])
            self.student_id2.setText(student_id[5:])
            self.student_id1.setEnabled(False)
            self.student_id2.setEnabled(False)
            self.student_id1.setStyleSheet("background-color: lightgray;")
            self.student_id2.setStyleSheet("background-color: lightgray;") 
            self.button.setText("Edit")    
        else: #create
            self
            self.student_id1.setEnabled(True)
            self.student_id2.setEnabled(True)
            self.student_id1.setStyleSheet("")
            self.student_id2.setStyleSheet("")
            self.button.setText("Create")

        if student_name:
            self.student_name.setText(student_name)

        if course_id:
            self.course_id.setCurrentText(course_id)

        if year_level:
            self.year_level.setCurrentText(str(year_level))

        if gender:
            self.gender.setCurrentText(gender)

        # Create an HBox for student ID
        hbox = QHBoxLayout()
        hbox.addWidget(self.student_id1)
        hbox.addWidget(QLabel("-"))
        hbox.addWidget(self.student_id2)

        # Layout
        layout = QGridLayout()
        layout.addWidget(QLabel("Student ID:"), 0, 0)
        layout.addLayout(hbox, 0, 1) 
        layout.addWidget(QLabel("Student Name:"), 1, 0)
        layout.addWidget(self.student_name, 1, 1)
        layout.addWidget(QLabel("Course ID:"), 2, 0)
        layout.addWidget(self.course_id, 2, 1)
        layout.addWidget(QLabel("Year Level:"), 3, 0)
        layout.addWidget(self.year_level, 3, 1)
        layout.addWidget(QLabel("Gender:"), 4, 0)
        layout.addWidget(self.gender, 4, 1)

        # Button
        layout.addWidget(self.button, 6, 0, 1, 2)
        
        # Error Label
        self.error_label = QLabel(self)
        self.error_label.setText("")
        self.error_label.setWordWrap(True)
        self.error_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout.addWidget(self.error_label, 5, 0, 1, 2)  

        self.setLayout(layout)

    def printError(self, message):
        try:
            self.error_label.setText(message)
        except:
            pass
        
    def submit(self):
        func = self.crudl_class.updateStudent if self.student_id else self.crudl_class.createStudent
        if self.multiple:
            count = 0
            courseID = self.course_id.currentText()
            for student_id in self.student_ids:
                data = self.crudl_class.readStudent(student_id)
                self.crudl_class.updateStudent(data[0], data[1], courseID, data[3], data[4])
                count += 1
            self.error_label.setText(f"{count} Students Edited.")
        else:
            student_id = self.student_id1.text() + '-' + self.student_id2.text()
            student_name = self.student_name.text()
            course_id = self.course_id.currentText()
            year_level = self.year_level.currentText()
            gender = self.gender.currentText()
            func(student_id, student_name, course_id, year_level, gender)
        self.formSubmit.emit()


    def closeEvent(self, event):
        self.dialogClosed.emit() 
        super().closeEvent(event) 


class CourseDialog(QDialog):
    dialogClosed = pyqtSignal()
    formSubmit = pyqtSignal()

    def __init__(self, course_id=None, course_desc=None):
        super().__init__()
        self.setWindowTitle("Course Information")
        self.setGeometry(100, 100, 400, 200)
        with open('styles.qss', 'r') as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)

        self.idIsEnabled = True if course_id else False
        self.crudl_class = CRUDLClass(failure_action=self.printError, success_action=self.printError)

        # Initialize fields as null
        self.course_id = QLineEdit(self)
        self.course_desc = QLineEdit(self)

        # Make the button ahead
        self.button = QPushButton("Submit", self)
        self.button.clicked.connect(self.submit)

        # Set default values and editability based on course ID
        if course_id:
            self.course_id.setText(course_id)
            self.course_id.setEnabled(False)
            self.course_id.setStyleSheet("background-color: lightgray;")
            self.button.setText("Edit")
        else:
            self.course_id.setEnabled(True)
            self.course_id.setStyleSheet("")
            self.button.setText("Create")

        if course_desc:
            self.course_desc.setText(course_desc)

        # Layout
        layout = QGridLayout()
        layout.addWidget(QLabel("Course ID:"), 0, 0)
        layout.addWidget(self.course_id, 0, 1)
        layout.addWidget(QLabel("Course Description:"), 1, 0)
        layout.addWidget(self.course_desc, 1, 1)

        # Button
        layout.addWidget(self.button, 2, 0, 1, 2)

        # Error Label
        self.error_label = QLabel(self)
        self.error_label.setText("")
        self.error_label.setWordWrap(True)
        self.error_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout.addWidget(self.error_label, 3, 0, 1, 2)

        self.setLayout(layout)

    def printError(self, message):
        try:
            self.error_label.setText(message)
        except:
            pass

    def submit(self):
        course_id = self.course_id.text()
        course_desc = self.course_desc.text()

        if not course_id:
            self.error_label.setText("Course code cannot be blank.")
            return
        if not course_desc:
            self.error_label.setText("Course description cannot be blank.")
            return

        func = self.crudl_class.updateCourse if self.idIsEnabled else self.crudl_class.createCourse
        func(course_id, course_desc)
        self.formSubmit.emit()

    def closeEvent(self, event):
        self.dialogClosed.emit()
        super().closeEvent(event)
