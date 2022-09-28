# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint


print ('Введите число N: ')
number = int(input())
listNumbers = []
listIndex = []

for i in range(number):
    listNumbers.append(randint(-number, number))

file = open('text.txt')
textFromFile = file.read()
listIndex = textFromFile.split('\n')
print(f'Список из {number} случайных чисел от {-number} до {number}: {listNumbers}')
print(f'Список индесов из файла text.txt: {listIndex}')
result = listNumbers[int(listIndex[0])] * listNumbers[int(listIndex[1])]
print(f'Произведение элементов с указанными индексами равно: {result}')





