import mysql.connector
from mysql.connector import errorcode

class CRUDLClass:
    
    def __init__(self):
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

    def executeQuery(self, query):
        try:
            self.cursor.execute(query)
            self.cnx.commit()
            return True
        except mysql.connector.Error as err:
            if err != "Unread result found":
                self.promptTaskError(f"ERROR:{err}")
            return False
            
    def promptTaskSuccess(self, message):
        print(message)
        
    def promptTaskError(self, error):
        print(error)
        
    def createStudent(self, studentID, studentName, courseID, yearLevel, gender):
        query = f"""INSERT INTO Students VALUES ('{studentID}', '{studentName}', '{courseID}', '{yearLevel}', '{gender}', 0)"""
        self.executeQuery(query)
    
    def readStudent(self, studentID):
        query = f"""SELECT * FROM Students WHERE StudentID='{studentID}';"""
        self.cursor.execute(query)
        student = self.cursor.fetchall()
        return student
    
    def updateStudent(self, studentID, studentName, courseID, yearLevel, gender):
        query = f"""UPDATE Students
                    SET StudentName = '{studentName}', CourseID = '{courseID}', YearLevel = {yearLevel}, Gender = '{gender}', IsEnrolled = 0
                    WHERE StudentID = '{studentID}';"""
        self.executeQuery(query)

    def deleteStudent(self, studentID):
        query = f"""DELETE FROM Students WHERE StudentID='{studentID}';"""
        self.executeQuery(query)
        
    def listStudents(self):
        query = """SELECT * FROM Students;"""
        self.cursor.execute(query)
        students = self.cursor.fetchall()
        
        column_names = [desc[0] for desc in self.cursor.description]

        students.insert(0, tuple(column_names))

        return students
    
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
        query = f"""DELETE FROM Courses WHERE CourseID='{courseID}';"""
        self.executeQuery(query)
        
    def listCourses(self):
        query = """SELECT * FROM COURSES"""
        self.executeQuery(query)
        courses = self.cursor.fetchall()
        
        column_names = [desc[0] for desc in self.cursor.description]
        courses.insert(0, tuple(column_names))
        
        return courses


cc = CRUDLClass()
students = cc.listStudents()
for student in students:
    print(student)
    
print(cc.readStudent("2022-0000"))