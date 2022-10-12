# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# def Sum (num):
#     while num != int(num):
#         num *= 10
#     num = int(num)
#     sum = 0
#     while num > 9:
#         sum += num % 10
#         num //= 10
#     sum += num
#     return sum
    


# print('Введите вещественное число')
# number = float(input())
# number = abs(number)

# print(f'Сумма цифр числа {number} равна {Sum(number)}')

print(sum(list(map(lambda x: 0 if x == '.' or x == ',' else int(x), input("Введите вещественное число: ")))))
