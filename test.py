from utils_crud import CRUDLClass as cc

mycc = cc()

print(mycc.listStudents(isEnrolled = 0, gender='Man'))