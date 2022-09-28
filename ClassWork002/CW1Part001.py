# Напишите программу которая принимает на вход число N и выдает последовательность из N членов
# Пример: для N равно 5: 1, -3, 9, -27, 81

print ('Введите число N')
number = int(input())
current = 1
for i in range (0, number):
    print(current, end = '  ')
    current *= -3