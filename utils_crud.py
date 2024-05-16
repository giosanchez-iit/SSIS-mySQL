import mysql.connector
from mysql.connector import errorcode
    
class CRUDLClass:
    
    def __init__(self, success_action = None, failure_action = None):
        self.success_action = success_action
        self.failure_action = failure_action
        self.cnx = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(host="127.0.0.1", user="root", password="123", database="ssisdb")
            self.cursor = self.cnx.cursor()
            print("Connected to MySQL database successfully!")
        except mysql.connector.Error as err:
            print("Error connecting to database:", err)

    def executeQuery(self, query, success_message=None):
        try:
            self.cursor.execute(query)
            self.cnx.commit()
            if self.success_action:
                self.success_action(success_message)
            return True
        except mysql.connector.Error as err:
            err_str = str(err)
            if err_str != "Unread result found":
                # Extract the error prompt after the colon
                error_parts = err_str.split(":", 1)
                error_prompt = error_parts[1].strip() if len(error_parts) > 1 else err_str
                
                self.promptTaskError(error_prompt)
                if self.failure_action:
                    self.failure_action(error_prompt)
            return False
            
    def promptTaskSuccess(self, message):
        print(message)
        
    def promptTaskError(self, error):
        print(error)
      
    # STUDENTS CRUDL
      
    def createStudent(self, studentID, studentName, courseID, yearLevel, gender):
        query = f"""INSERT INTO Students VALUES ('{studentID}', '{studentName}', '{courseID}', '{yearLevel}', '{gender}', 0)"""
        self.executeQuery(query, success_message=f"Student {studentName} ({studentID}) Added!")
    
    def readStudent(self, studentID):
        query = f"""SELECT * FROM Students WHERE StudentID='{studentID}';"""
        self.cursor.execute(query)
        student = self.cursor.fetchall()
        return student[0] if student else None
    
    def updateStudent(self, studentID, studentName, courseID, yearLevel, gender):
        query = f"""UPDATE Students
                    SET StudentName = '{studentName}', CourseID = '{courseID}', YearLevel = {yearLevel}, Gender = '{gender}', IsEnrolled = 0
                    WHERE StudentID = '{studentID}';"""
        self.executeQuery(query, success_message=f"Student {studentName} ({studentID}) Updated!")

    def deleteStudent(self, studentID):
        student = self.readStudent(studentID)
        studentName = student[0][1]
        query = f"""DELETE FROM Students WHERE StudentID='{studentID}';"""
        self.executeQuery(query, success_message=f"Student {studentName} ({studentID}) Deleted!")
        
    def listStudents(self, searchItem=None, searchQuery=None):
        query = f"""SELECT * FROM Students WHERE {searchItem} LIKE '%{searchQuery}%' """ if (searchItem and searchQuery) else """SELECT * FROM Students;"""
        self.cursor.execute(query)
        students = self.cursor.fetchall()
        column_names = [desc[0] for desc in self.cursor.description]
        students.insert(0, tuple(column_names))
        return students
    
    # STUDENTS HELPER FUNCTIONS
    
    def doForEachStudent(self, myFunc, searchItem=None, searchQuery=None):
        
        searchItemWithQuery = f""" WHERE {searchItem} LIKE '%{searchQuery}%' """ if (searchItem and searchQuery) else None
        
        query = f"""SELECT * FROM Students {searchItemWithQuery} ORDER BY StudentID"""
        self.cursor.execute(query)
        students = self.cursor.fetchall()
        if not students:
            return
        for student in students:  # Iterating over 'students' list
            myFunc(student)

    def countStudents(self):
        query = "SELECT COUNT(*) FROM Students;"
        self.cursor.execute(query)
        count = self.cursor.fetchall()
        return int(count[0][0])
    
    def listStudentKeys(self):
        query = "SHOW COLUMNS FROM Students;"
        self.cursor.execute(query)
        columns = self.cursor.fetchall()
        column_names = [column[0] for column in columns]
        return column_names
    
    
    
    # COURSE CRUDL
    
    def createCourse(self, courseID, courseDesc):
        query = f"""INSERT INTO Courses VALUES ('{courseID}', '{courseDesc}')"""
        self.executeQuery(query)
    
    def readCourse(self, courseID):
        query = f"""SELECT * FROM Courses WHERE CourseID = '{courseID}';"""
        self.executeQuery(query)
        course = self.cursor.fetchall()
        return course
            
    def updateCourse(self, courseID, courseDesc):
        query = f"""UPDATE Courses SET CourseDesc = '{courseDesc}' WHERE CourseID = '{courseID}';"""
        self.executeQuery(query)
        
    def deleteCourse(self, courseID):
        query = f"""UPDATE Students SET CourseID = NULL WHERE CourseID = {courseID};
                    DELETE FROM Courses WHERE CourseID = {courseID}"""
        self.executeQuery(query)
        
    def listCourses(self, searchItem=None, searchQuery=None):
        query = f"""SELECT * FROM COURSES WHERE {searchItem} LIKE '%{searchQuery}%' """ if (searchItem and searchQuery) else """SELECT * FROM Courses;"""
        
        self.executeQuery(query)
        courses = self.cursor.fetchall()
        
        column_names = [desc[0] for desc in self.cursor.description]
        courses.insert(0, tuple(column_names))
        
        return courses
    
    def listCourseKeys(self):
        query = "SELECT CourseID FROM Courses"
        self.cursor.execute(query)
        courseIDs = self.cursor.fetchall()
        return courseIDs
    
    # COURSE HELPER FUNCTIONS
    
    def doForEachCourse(self, myFunc, searchItem=None, searchQuery=None):
        searchItemWithQuery = f""" WHERE {searchItem} LIKE '%{searchQuery}%' """ if (searchItem and searchQuery) else None
        
        query = f"""SELECT * FROM Courses {searchItemWithQuery} ORDER BY CourseID"""
        self.cursor.execute(query)
        courses = self.cursor.fetchall()
        if not courses:
            return
        for course in courses:
            myFunc(course)

    def countCourses(self):
        query = "SELECT COUNT(*) FROM Courses;"
        self.cursor.execute(query)
        count = self.cursor.fetchall()
        return int(count[0][0])
    
    def listCourseDescriptions(self):
        query = "SELECT CourseDesc FROM Courses;"
        self.cursor.execute(query)
        descriptions = self.cursor.fetchall()
        return descriptions