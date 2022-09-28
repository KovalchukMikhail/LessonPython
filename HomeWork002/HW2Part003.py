# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

print('Введите целое число: ')
number = int(input())
list = []
sum = 0

for i in range(1, number + 1):
    list.append((1+1/i)**i)
    sum += (1+1/i)**i

print (list)
print (f'Сумма чисел списка последовательностей (1+1/n)^n равна {sum}')

