# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

print('Введите целое число: ')
number = int(input())
list = []
result = 1

for i in range(1, number + 1):
    result *= i
    list.append(result)

print(list)

