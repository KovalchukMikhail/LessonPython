# Задайте строку из набора чисел напишите программу которая покажит большее и меньшее число, в качестве символа разделителя используйте пробел и записать в другой файл отдельно файл с максимальным и файл с минимальным

from datetime import datetime
import time

def Random_number (min, max):
    if abs(max) > abs (min):
        check = min - 1
        max_abs = max + 1
    else:
        check = max + 1
        max_abs = min - 1
    random_number = check
    while random_number < min or random_number > max:
        temp_number = (float(time.time()) * float(datetime.now().time().microsecond)) / 1000000
        sign = -1
        if int(temp_number) % 2 != 0:
            sign = 1
        temp_number = temp_number - int(temp_number)
        random_number = abs(max_abs) * temp_number * sign
        random_number = int(random_number)
        time.sleep(0.000001)
    return random_number


def CreateList (size, min, max):
    createList = []
    for i in range(size):
        createList.append(Random_number(min, max))
    return createList

print('Введите количество элементов списка: ')
size_list = int(input())
print ('Введите минимальное возможное значение числа в списке: ')
min_number = int(input())
print ('Введите максимальное возможное значение числа в списке: ')
max_number = int(input())
new_list = CreateList(size_list, min_number, max_number)

file = open('numbers.txt', 'w')
# for i in new_list:
#     file.write(f'{str(i)} ')
file.write(new_list)
file.close()

file = open('numbers.txt', 'r')
text_file = file.read()
list_numbers = text_file.split(' ')
list_numbers.pop()
max = int(list_numbers[0])
min = int(list_numbers[0])
for i in list_numbers:
    if max < int(i):
        max = int(i)
    elif min > int(i):
        min = int(i)
file_max = open('max.txt', 'w')
file_min = open('min.txt', 'w')

file_max.write(str(max))
file_min.write(str(min))

file_max.close()
file_min.close()


