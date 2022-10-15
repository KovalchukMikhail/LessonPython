# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
from random import randint

# def CreateList (size, min, max):
#     createList = []
#     for i in range(size):
#         createList.append(randint(min, max))
#     return createList

# print('Введите количество элементов списка: ')
# size_list = int(input())
# print ('Введите минимальное возможное значение числа в списке: ')
# min_number = int(input())
# print ('Введите максимальное возможное значение числа в списке: ')
# max_number = int(input())
# new_list = CreateList(size_list, min_number, max_number)
# sum = 0

# if len(new_list) > 1:
#     for i in range(1, len(new_list), 2):
#         sum += new_list[i]
#     print(f'Сумма элементов списка {new_list} стоящих на нечетных позициях равна {sum}')
# else:
#     print(f'В списке отсутсвую элементы с нечетными индексами')

print(f'Сумма чисел стоящих на нечетных позициях списка равна {sum((list_new :=[randint(0, 10) for _ in range(int(input("Введите количество чисел в списке: ")))])[1::2])}')
print(f'Список: {list_new}')