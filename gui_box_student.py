import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QLayout

class StudentWidget(QWidget):
    def __init__(self, studentID=None, studentName=None, courseID=None, yearLevel=None, gender=None):
        super().__init__()
        self.initUI(studentID, studentName, courseID, yearLevel, gender)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # Allow horizontal scaling
        
    def initUI(self, studentID="", studentName="", courseID="", yearLevel=0, gender=""):
        # Set Enrollment Status
        enrollmentStatus = "Not Enrolled" if courseID == "" else "Enrolled"

        # Create a QHBoxLayout with spacing
        hbox = QHBoxLayout(spacing=5)
        hbox.setSizeConstraint(QLayout.SetMinAndMaxSize)  # Allow layout to resize

        # Add spacing between widgets
        labelStudentID = QLabel(studentID)
        labelStudentID.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        labelStudentName = QLabel(studentName)
        labelStudentName.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)  # Allow label to scale horizontally
        labelCourseID = QLabel(courseID)
        labelCourseID.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        labelYearLevel = QLabel(str(yearLevel))
        labelYearLevel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        labelGender = QLabel(gender)
        labelGender.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        labelEnrollmentStatus = QLabel(enrollmentStatus)
        labelEnrollmentStatus.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        btnEdit = QPushButton("Edit")
        btnEdit.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        btnDelete = QPushButton("Delete")
        btnDelete.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        hbox.addWidget(labelStudentID, 4)
        hbox.addWidget(labelStudentName, 6)
        hbox.addWidget(labelCourseID, 2)
        hbox.addWidget(labelYearLevel, 2)
        hbox.addWidget(labelGender, 2)
        hbox.addWidget(labelEnrollmentStatus, 3)
        hbox.addWidget(btnEdit, 1)
        hbox.addWidget(btnDelete, 1)

        # Set the layout to the widget
        self.setLayout(hbox)
        

class StudentWidgetHeader(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # Allow horizontal scaling
        
    def initUI(self, studentID="", studentName="", courseID="", yearLevel=0, gender=""):
        
        # Create a QHBoxLayout with spacing
        hbox = QHBoxLayout(spacing=5)
        hbox.setSizeConstraint(QLayout.SetMinAndMaxSize)  # Allow layout to resize

        # Add spacing between widgets
        labelStudentID = QLabel("studentID")
        labelStudentID.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        labelStudentName = QLabel("studentName")
        labelStudentName.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)  # Allow label to scale horizontally
        labelCourseID = QLabel("courseID")
        labelCourseID.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        labelYearLevel = QLabel(str("yearLevel"))
        labelYearLevel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        labelGender = QLabel("gender")
        labelGender.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        labelEnrollmentStatus = QLabel("enrollmentStatus")
        labelEnrollmentStatus.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        btnEdit = QPushButton("    ")
        btnEdit.setStyleSheet("""
                              QPushButton {
                                    color: None;
                                    background-color: None;
                                }

                                QPushButton:hover {
                                    color: None;
                                    background-color: None;
                                }
                              """)
        btnEdit.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        btnDelete = QPushButton("      ")
        btnDelete.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        hbox.addWidget(labelStudentID, 4)
        hbox.addWidget(labelStudentName, 6)
        hbox.addWidget(labelCourseID, 2)
        hbox.addWidget(labelYearLevel, 2)
        hbox.addWidget(labelGender, 2)
        hbox.addWidget(labelEnrollmentStatus, 3)
        hbox.addWidget(btnEdit, 1)
        hbox.addWidget(btnDelete, 1)

        # Set the layout to the widget
        self.setLayout(hbox)