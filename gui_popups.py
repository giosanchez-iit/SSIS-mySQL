import sys
from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QLineEdit, QComboBox, QLabel, QPushButton, QHBoxLayout, QMessageBox, QSizePolicy
from PyQt5.QtCore import pyqtSignal
from utils_crud import CRUDLClass

class StudentDialog(QDialog):
    dialogClosed = pyqtSignal() 

    def __init__(self, student_id=None, student_name=None, course_id=None, year_level=None, gender=None, multiple = False):
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

        # Make the button ahead
        self.button = QPushButton("Submit", self)
        self.button.clicked.connect(self.submit)
        
        # Populate combo boxes
        courseList = []
        courses = self.crudl_class.listCourses()
        self.course_id.addItem('None')
        self.year_level.addItem('None')
        self.gender.addItem('None')
        self.course_id.setCurrentIndex(0)
        self.year_level.setCurrentIndex(0)
        self.gender.setCurrentIndex(0)
        for course in courses:
            courseList.append(f"{course[0]} - {course[1]}")
        self.course_id.addItems([str(course[0]) for course in self.crudl_class.listCourseKeys()])
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
        try:
            student_id = f"{self.student_id1.text()}-{self.student_id2.text()}"
            student_name = self.student_name.text()
            course_id = self.course_id.currentText()
            year_level = self.year_level.currentText()
            gender = self.gender.currentText()

            course_id = None if course_id == 'None' else course_id
            year_level = None if year_level == 'None' else year_level
            gender = None if gender == 'None' else gender

            if self.student_id1.isEnabled():
                success = self.crudl_class.createStudent(student_id, student_name, course_id, year_level, gender)
            else:
                success = self.crudl_class.updateStudent(student_id, student_name, course_id, year_level, gender)

            if success:
                message_box = QMessageBox()
                message_box.setWindowTitle("Success")
                message_box.setText("Student information saved successfully!")
                message_box.setStandardButtons(QMessageBox.Ok)
                message_box.setIcon(QMessageBox.Information)
                message_box.exec_()
            else:
                pass
        except ValueError as ve:
            print(f"ValueError: {ve}")  # Catching ValueError specifically for type conversion errors
        except Exception as e:
            print(f"An unexpected error occurred: {e}")  # Log unexpected errors


    def closeEvent(self, event):
        self.dialogClosed.emit() 
        super().closeEvent(event) 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = StudentDialog(multiple = False)
    dialog.show()
    sys.exit(app.exec_())
