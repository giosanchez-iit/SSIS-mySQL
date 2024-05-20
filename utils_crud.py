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
        courseID = "NULL" if courseID == 'None' else f"'{courseID}'"
        yearLevel = "NULL" if yearLevel == 'None' or yearLevel == '' else f"{yearLevel}"
        gender = "NULL" if gender == 'None' or gender == '' else f"'{gender}'"
        query = f"""INSERT INTO Students (StudentID, StudentName, CourseID, YearLevel, Gender, IsEnrolled)
                    VALUES ('{studentID}', '{studentName}', {courseID}, {yearLevel}, {gender}, 0);"""
        self.executeQuery(query, success_message=f"Student {studentName} ({studentID}) Created!")

    def readStudent(self, studentID):
        query = f"""SELECT * FROM Students WHERE StudentID='{studentID}';"""
        self.cursor.execute(query)
        student = self.cursor.fetchall()
        return student[0] if student else None
    
    def updateStudent(self, studentID, studentName, courseID, yearLevel, gender):
        print("before")
        courseID = "NULL" if courseID == 'None' else f"'{courseID}'"
        yearLevel = "NULL" if yearLevel == 'None' or yearLevel == '' else f"{yearLevel}"
        gender = "NULL" if gender == 'None' or gender == '' else f"'{gender}'"
        query = f"""UPDATE Students SET StudentName = '{studentName}', CourseID = {courseID}, YearLevel = {yearLevel}, Gender = {gender}, IsEnrolled = 0 WHERE StudentID = '{studentID}';"""
        print(query)
        self.executeQuery(query, success_message=f"Student {studentName} ({studentID}) Updated!")
        print("after")

    def deleteStudent(self, studentID):
        student = self.readStudent(studentID)
        studentName = student[0][1]
        query = f"""DELETE FROM Students WHERE StudentID='{studentID}';"""
        self.executeQuery(query, success_message=f"Student {studentName} ({studentID}) Deleted!")
        
    def listStudents(self, **kwargs):
        base_query = "SELECT * FROM Students"
        where_clause = ""

        if kwargs:
            where_clauses = []
            for key, value in kwargs.items():
                if key == 'isEnrolled' and value is not None:
                    where_clauses.append(f"{key} = {value}")
                elif (key == 'gender' or key=='courseID') and value:
                    where_clauses.append(f"{key} = '{value}'")
                elif value:
                    where_clauses.append(f"{key} LIKE '%{value}%'")
            if where_clauses:
                where_clause = " WHERE " + " AND ".join(where_clauses)

        final_query = base_query + where_clause
        self.cursor.execute(final_query)
        students = self.cursor.fetchall()

        # Convert the first row of students to column names
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
        query = "SELECT * FROM Students;"
        self.cursor.execute(query)
        columns = self.cursor.fetchall()
        column_names = [column[0] for column in columns]
        return column_names
    
    
    
    # COURSE CRUDL
    
    def createCourse(self, courseID, courseDesc):
        query = f"""INSERT INTO Courses (CourseID, CourseDesc) VALUES ('{courseID}', '{courseDesc}')"""
        self.executeQuery(query, success_message=f"Course {courseDesc} ({courseID}) Created!")
    
    def readCourse(self, courseID):
        query = f"""SELECT * FROM Courses WHERE CourseID = '{courseID}';"""
        self.cursor.execute(query)
        course = self.cursor.fetchall()
        return course[0] if course else None
            
    def updateCourse(self, courseID, courseDesc):
        query = f"""UPDATE Courses SET CourseDesc = '{courseDesc}' WHERE CourseID = '{courseID}';"""
        self.executeQuery(query, success_message=f"Course {courseDesc} ({courseID}) Updated!")
        
    def deleteCourse(self, courseID):
        update_students_query = f"""UPDATE Students SET CourseID = NULL WHERE CourseID = '{courseID}';"""
        self.executeQuery(update_students_query, success_message=f"All students enrolled in course {courseID} have been updated.")

        delete_course_query = f"DELETE FROM Courses WHERE CourseID = '{courseID}';"
        self.executeQuery(delete_course_query, success_message=f"Course ({courseID}) Deleted!")
            
    def listCourses(self, searchItem=None, searchQuery=None):
        base_query = "SELECT * FROM Courses"
        where_clause = ""

        if searchItem and searchQuery:
            where_clause = f" WHERE {searchItem} LIKE '%{searchQuery}%'"

        final_query = base_query + where_clause
        self.cursor.execute(final_query)
        courses = self.cursor.fetchall()

        # Convert the first row of courses to column names
        column_names = [desc[0] for desc in self.cursor.description]
        courses.insert(0, tuple(column_names))

        return courses
    
    def listCourseKeys(self):
        query = "SELECT * FROM Courses;"
        self.cursor.execute(query)
        columns = self.cursor.fetchall()
        column_names = [column[0] for column in columns]
        return column_names
    
    # COURSE HELPER FUNCTIONS
    
    def doForEachCourse(self, myFunc, searchItem=None, searchQuery=None):
        searchItemWithQuery = f""" WHERE {searchItem} LIKE '%{searchQuery}%' """ if (searchItem and searchQuery) else ""
        
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
