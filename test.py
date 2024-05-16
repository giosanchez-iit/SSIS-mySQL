import random
from utils_crud import CRUDLClass

cc = CRUDLClass()

arrayOfFirstNames = ["Alex", "Jamie", "Riley", "Sam", "Cameron", "Jordan", "Taylor", "Blake", "Avery", "Rowan",
                        "Parker", "Harper", "Finley", "Peyton", "Emerson", "Quinn", "Dakota", "Skylar", "Kendall", "Sawyer",
                        "Riley", "Rowan", "Blair", "Kendall", "Reese", "Peyton", "Kendall", "Jamie", "Avery", "Parker",
                        "Hayden", "Briar", "Kendall", "Rowan", "Jamie", "Reese", "Riley", "Jordan", "Parker", "Sawyer",
                        "Jamie", "Riley", "Rowan", "Kendall", "Sawyer", "Reese", "Parker", "Jordan", "Jamie", "Avery",
                        "Addison", "Aiden", "Amelia", "Andrew", "Anna", "Asher", "Ava", "Benjamin", "Charlotte", "Chase",
                        "Chloe", "Cole", "Daisy", "Daniel", "Ella", "Ethan", "Evelyn", "Felix", "Grace", "Grayson",
                        "Hannah", "Henry", "Isabella", "Jack", "Jasmine", "Jaxon", "Julia", "Kai", "Kayla", "Keaton",
                        "Liam", "Lily", "Logan", "Madison", "Mason", "Mia", "Nathan", "Nora", "Oscar", "Olivia",
                        "Phoenix", "Quinn", "Remy", "Ruby", "Soren", "Sophia", "Tate", "Tatum", "Theo", "Violet",
                        "Walter", "Willow", "Xavier", "Yara", "Zoe"]

arrayOfLastNames = last_names = ["Sanchez", "Lee", "Quirino", "Abara", "Mullner","Schmidt", "Nguyen", "Garcia",
                                    "Volkov", "Wang", "Kowalski", "Levine", "Cohen", "Murphy", "O'Brien",
                                    "Diallo", "Mohammed", "Johnson", "Zulu", "Mendoza", "Akintola", "Adebayo", "Sissoko", "Keita",
                                    "Silva", "Pereira", "Schmidt", "Nguyen", "Garcia", "Volkov", "Wang", "Kowalski", "Levine", "Cohen", "Murphy", "O'Brien",
                                    "Diallo", "Mohammed", "Johnson", "Zulu", "Mendoza", "Akintola", "Adebayo", "Sissoko", "Keita",
                                    "Silva", "Pereira", "Santos", "Moreno", "Fernandez", "Lopez", "Torres", "Diaz", "Castro", "Gutierrez",
                                    "Kim", "Park", "Choi", "Lee", "Jung", "Han", "Kang", "Won", "Yoo", "Im",
                                    "Campbell", "Scott", "Robinson", "Wilson", "Brown", "Walker", "Allen", "Clark", "Wright", "Moore"]

# Get course keys
arrayOfCourseKeys = cc.listCourseKeys()


# Loop through student IDs
for studentID in range(0, 4000):  # Assuming student IDs start from 2022-0001
    studentStringID = f"2023-{studentID:04d}"
    # Generate random name
    firstName = random.choice(arrayOfFirstNames)
    lastName = random.choice(arrayOfLastNames)
    
    # Decide whether to add a second name
    addSecondName = random.choice([True, False])
    if addSecondName:
        secondName = random.choice(arrayOfFirstNames)
        fullName = f"{firstName} {secondName} {lastName}" if firstName and secondName and lastName else firstName or secondName or lastName
    else:
        fullName = f"{firstName} {lastName}" if firstName and lastName else firstName or lastName

    # Select random course ID, year level, and gender
    courseID = random.choice(arrayOfCourseKeys)[0] if arrayOfCourseKeys else None
    if courseID == "None":
        courseID = None
    yearLevel = 1
    gender = random.choice(["Man", "Woman"]) if arrayOfCourseKeys else None

    # Create new student
    cc.createStudent(studentStringID, fullName, courseID, yearLevel, gender)