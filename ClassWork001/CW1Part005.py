# Напишите программу которая которая принимает на вход число и проверяет кратно ли оно 5 и 10 или 15, но не 30

print('Введите число: ')
number = int(input())
result = (number % 5 == 0 and number % 10 == 0 and number % 30 != 0) or (number % 15 == 0 and number % 30 != 0)
print(result)
