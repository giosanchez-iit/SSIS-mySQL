from utils_crud import CRUDLClass as cc
mycc = cc()

func = mycc.readStudent

mine = func('2022-0025')[1]
print(mine)