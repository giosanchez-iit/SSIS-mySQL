import mysql.connector

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
            return False
            
    def promptTaskSuccess(self, message):
        print(message)
        
    def createStudent(self, studentID, studentName, courseID, yearLevel, gender):
        query = f"""INSERT INTO Students VALUES ('{studentID}', '{studentName}', '{courseID}', '{yearLevel}', '{gender}', 0)"""
        self.executeQuery(query)
        self.promptTaskSuccess(f"Student {studentID} Created.")
    
    def readStudent(self, studentID):
        query = f"""SELECT * FROM Students WHERE StudentID='{studentID}';"""
        self.executeQuery(query)
        student = self.cursor.fetchall()
        return student
    
    def updateStudent(self, studentID, studentName, courseID, yearLevel, gender):
        query = f"""UPDATE Students
                    SET StudentName = '{studentName}', CourseID = '{courseID}', YearLevel = {yearLevel}, Gender = '{gender}', IsEnrolled = 0
                    WHERE StudentID = '{studentID}';"""
        self.executeQuery(query)
        self.promptTaskSuccess(f"Student {studentID} Updated.")

    def deleteStudent(self, studentID):
        query = f"""DELETE FROM Students WHERE StudentID='{studentID}';"""
        self.executeQuery(query)
        self.promptTaskSuccess(f"Student {studentID} Deleted.")
        
    def listStudents(self):
        query = """SELECT * FROM Students;"""
        self.executeQuery(query)
        students = self.cursor.fetchall()
        
        # Get the column names from the cursor description
        column_names = [desc[0] for desc in self.cursor.description]
        
        # Add the column names as the first tuple in the list
        students.insert(0, tuple(column_names))
        
        self.promptTaskSuccess(f"All Students Listed.")
        return students
    
    def createCourse(self, courseID, courseDesc):
        query = f"""INSERT INTO Courses VALUES ('{courseID}', '{courseDesc}')"""
        self.executeQuery(query)
        self.promptTaskSuccess(f"Course {courseID} Created.")
    
    def readCourse(self, courseID):
        query = f"""SELECT * FROM Courses WHERE CourseID = '{courseID}';"""
        self.executeQuery(query)
        course = self.cursor.fetchall()
        return course
            
    def updateCourse(self, courseID, courseDesc):
        query = f"""UPDATE Courses SET CourseDesc = '{courseDesc}' WHERE CourseID = '{courseID}';"""
        self.executeQuery(query)
        self.promptTaskSuccess(f"shit")
        
    def deleteCourse(self, courseID):
        query = f"""DELETE FROM Courses WHERE CourseID='{courseID}';"""
        self.executeQuery(query)
        self.promptTaskSuccess(f"Course {courseID} Deleted.")
        
    def listCourses(self):
        query = """SELECT * FROM COURSES"""
        self.executeQuery(query)
        courses = self.cursor.fetchall()
        
        column_names = [desc[0] for desc in self.cursor.description]
        courses.insert(0, tuple(column_names))
        
        self.promptTaskSuccess(f"All Students Listed.")
        return courses














'''

    def executeQuery(self, query, params=None):
        try:
            if self.cnx is None or self.cursor is None:
                self.connect()
            
            if params is None:
                self.cursor.execute(query)
            else:
                self.cursor.execute(query, params)
            
            # Fetch all results if the query is expected to return data
            if query.lower().strip().startswith('select'):
                results = self.cursor.fetchall()
                # Return results instead of printing them
                return results
            
            self.cnx.commit()  # Commit the transaction if changes were made
        except mysql.connector.Error as err:
            return f"Error executing query: {err}"
        finally:
            if self.cursor:
                self.cursor.close()
            if self.cnx:
                self.cnx.close()
                self.connect()  # Re-establish connection for future operations

        return "Success"

    def createStudent(self, student_id, student_name, course_id, year_level, gender):
        query = """
            INSERT INTO Students (StudentID, StudentName, CourseID, YearLevel, Gender, isEnrolled)
            VALUES (%s, %s, %s, %s, %s, 0);
        """
        try:
            cnx = mysql.connector.connect(host="127.0.0.1", user="root", password="123", database="ssisdb")
            cursor = cnx.cursor()
            values = (student_id, student_name, course_id, year_level, gender)
            cursor.execute(query, values)
            cnx.commit()
            print("Student created successfully!")
        except mysql.connector.Error as err:
            print(f"Error creating student: {err}")
        finally:
            if cursor:
                cursor.close()
            if cnx:
                cnx.close()
                
    def updateStudent(self, student_id, student_name=None, course_id=None, year_level=None, gender=None):
        query = """
            UPDATE Students
            SET StudentName = %s, CourseID = %s, YearLevel = %s, Gender = %s
            WHERE StudentID = %s;
        """
        values = (student_name, course_id, year_level, gender, student_id)
        result = self.executeQuery(query, values)
        if isinstance(result, str):  # Check if an error occurred
            return result
        else:
            return "Student updated successfully!"
    
    def deleteStudent(self, student_id):
        query = f"DELETE FROM Students WHERE StudentID = '{student_id}';"
        result = self.executeQuery(query)
        if isinstance(result, str): 
            return result
        else:
            return "Student deleted successfully!"
    
    def listStudents(self):
        query = "SELECT * FROM Students;"
        result = self.executeQuery(query)
        if isinstance(result, str): 
            return result
        else:
            return result.fetchall() 
    
    def createCourse(self, course_id, course_desc):
        query = """
            INSERT INTO Courses (CourseID, CourseDesc)
            VALUES (%s, %s);
        """
        try:
            cnx = mysql.connector.connect(host="127.0.0.1", user="root", password="123", database="ssisdb")
            cursor = cnx.cursor()
            values = (course_id, course_desc)
            cursor.execute(query, values)
            cnx.commit()
            print("Course created successfully!")
        except mysql.connector.Error as err:
            print(f"Error creating course: {err}")
        finally:
            if cursor:
                cursor.close()
            if cnx:
                cnx.close()
                
    def updateCourse(self, course_id, course_desc=None):
        query = """
            UPDATE Courses
            SET CourseDesc = %s
            WHERE CourseID = %s;
        """
        values = (course_desc, course_id)
        result = self.executeQuery(query, values)
        if isinstance(result, str): 
            return result
        else:
            return "Course updated successfully!"
    
    def deleteCourse(self, course_id):
        query = f"DELETE FROM Courses WHERE CourseID = '{course_id}';"
        result = self.executeQuery(query)
        if isinstance(result, str): 
            return result
        else:
            return "Course deleted successfully!"
    
    def listCourses(self):
        query = "SELECT * FROM Courses;"
        result = self.executeQuery(query)
        if isinstance(result, str): 
            return result
        else:
            return result.fetchall() 


crud = CRUDClass()
students = crud.listStudents()
for student in students:
    print(student)

'''