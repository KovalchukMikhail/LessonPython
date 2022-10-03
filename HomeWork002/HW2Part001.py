# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Вариант 1
# print('Введите вещественное число')
# number = input()
# sum = 0
# for i in number:
#     if i != ',' and i != '.':  # Лучше if i.isdigit():
#         sum += int(i)

# print(f'Сумма цифр заданного числа равна {sum}')


# Вариант 2 

# def Sum (num):
#     num *= 10 ** 15
#     num = int(num)
#     sum = 0
#     while num > 9:
#         sum += num % 10
#         num //= 10
#     sum += num
#     return sum

def Sum (num):
    while num != int(num):
        num *= 10
    num = int(num)
    sum = 0
    while num > 9:
        sum += num % 10
        num //= 10
    sum += num
    return sum
    


print('Введите вещественное число')
number = float(input())
number = abs(number)

print(f'Сумма цифр числа {number} равна {Sum(number)}')

