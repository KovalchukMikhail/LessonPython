# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import randint

def CreateList (size, min, max):
    createList = []
    for i in range(size):
        createList.append(randint(min, max))
    return createList

print('Введите количество элементов списка: ')
size_list = int(input())
print ('Введите минимальное возможное значение числа в списке: ')
min_number = int(input())
print ('Введите максимальное возможное значение числа в списке: ')
max_number = int(input())
new_list = CreateList(size_list, min_number, max_number)
result_list = []

if len(new_list) % 2 == 0:
    for i in range(len(new_list) // 2):
        result_list.append(new_list[i] * new_list[-(i + 1)])
else:
    for i in range((len(new_list) // 2) + 1):
        result_list.append(new_list[i] * new_list[-(i + 1)])

print(f'Произведение пар чисел списка {new_list} равно {result_list}')


