# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части
# элементов. минимальное значение дробной части отличное от нуля, у целых чисел дробной части нет их в расчет не берем



import random

def CreateList (size, min, max):
    createList = []
    for i in range(size):
        createList.append(random.uniform(min, max))
    return createList

print('Введите количество элементов списка: ')
size_list = int(input())
print ('Введите минимальное возможное значение числа в списке: ')
min_number = int(input())
print ('Введите максимальное возможное значение числа в списке: ')
max_number = int(input())
new_list = CreateList(size_list, min_number, max_number)
result_list = [(abs(i-int(i))) for i in new_list if i - int(i) != 0]
print(result_list)
list_b = []
for i in new_list:
    if i - int(i) != 0:
        list_b.append(abs(i - int(i)))
print(list_b)

min_number = min(result_list)
max_number = max(result_list)

print(f'Для списка {new_list} разница между максимальным и минимальным значение дробной части равна {max_number - min_number}')
