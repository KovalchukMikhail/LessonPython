# Напишите программу которая будет на вход принимать дробь и показывать первую цифру дробной части числа
# Например 6,78 > 7     5,0 > 0     0,34 > 3

print('Введите число: ')
number = input()
number = number.replace('.', ',')
index = number.find(',')
if index == -1:
    print(0)
else: 
    print(number[index + 1])

