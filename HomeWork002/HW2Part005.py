# Реализуйте алгоритм перемешивания списка.

from copy import copy
from random import randint


def CreateList (size, min, max):
    createList = []
    for i in range(size):
        createList.append(randint(min, max))
    return createList

def ChangeList (list):
    tempList = list.copy()
    indexList = []

    for i in range(len(list)):
        check = False
        while check == False:
            check = True
            tempIndex = randint(0, len(list) - 1)
            for j in indexList:
                if j == tempIndex:
                    check = False
            if check == True:
                indexList.append(tempIndex)
        list[i] = tempList[indexList[i]]    
    
    return list
                





print ('Введите длину списка: ')
sizeList = int(input())
print ('Введите минимальное возможное значение числа в списке: ')
minNumber = int(input())
print ('Введите максимальное возможное значение числа в списке: ')
maxNumber = int(input())

newList = CreateList (sizeList, minNumber, maxNumber)
print(f'Созданный список: {newList}')

changeList = ChangeList(newList)
print(f'Перемешанный список: {changeList}')


