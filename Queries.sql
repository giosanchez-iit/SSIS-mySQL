-- ADD CONSTRAINT check_student_id CHECK (StudentID REGEXP '^\\d{4}-\\d{4}$');
INSERT INTO Students (studentID, StudentName, CourseID, YearLevel, Gender, isEnrolled) VALUES ('2101-1088', 'John Doe', NULL, 1, 'Male', 0);
SELECT * FROM STUDENTS WHERE studentID LIKE '21%';
/*
UPDATE Students
SET StudentID='2022-0026'
WHERE StudentID = '10';

SELECT * FROM Students;


/*
DELIMITER $$
CREATE TRIGGER after_student_update BEFORE UPDATE
ON Students FOR EACH ROW
BEGIN
  IF NEW.CourseID IS NOT NULL
  THEN SET NEW.isEnrolled := TRUE;
  ELSE SET NEW.isEnrolled := FALSE;
  END IF;
END;
$$
DELIMITER ;
SELECT * FROM students;
*/

-- trigger for created student
/*
DELIMITER $$
CREATE TRIGGER after_student_create BEFORE INSERT
ON Students FOR EACH ROW
BEGIN
  IF NEW.CourseID IS NOT NULL
  THEN SET NEW.isEnrolled := TRUE;
  END IF;
END;
$$
DELIMITER ;
*/

-- CREATE DATABASE --
-- CREATE DATABASE ssisdb;

-- SET UP TABLES --
/*
USE ssisdb;

CREATE TABLE Courses (
	CourseID VARCHAR(15) PRIMARY KEY,
    CourseDesc VARCHAR(50) NOT NULL
);
CREATE TABLE Students (
  StudentID VARCHAR(9) PRIMARY KEY,
  StudentName VARCHAR(50) NOT NULL,
  CourseID VARCHAR(15),
  YearLevel TINYINT,
  Gender VARCHAR(15),
  isEnrolled BOOLEAN DEFAULT FALSE,
  FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);
*/