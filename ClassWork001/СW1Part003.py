# Напишите программу которая будет на вход принимать число N и выводить числа от -N до N

print('Введите число N: ')
number = int(input())
numbers = []
for i in range(-number, number + 1):
    numbers.append(i)
print(f' Числа от минус {number} до {number}: {numbers}')