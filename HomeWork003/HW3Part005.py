# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Вариант с использованием рекурсии

def Fibonacci_positive(number):
    if number == 0:
        return 0
    elif number == 1 or number == 2:
        return 1
    else:
        return Fibonacci_positive(number - 1) + Fibonacci_positive(number - 2)

def Fibonacci_negative(number):
    if number == 0:
        return 0
    elif number == -1:
        return 1
    elif number == -2:
        return -1
    else:
        return Fibonacci_negative(number + 2) - Fibonacci_negative(number + 1)


print('Введите число')
num = abs(int(input()))
fibonacci_list = []
for i in range(-num, 0):
    fibonacci_list.append(Fibonacci_negative(i))
for i in range(num + 1):
    fibonacci_list.append(Fibonacci_positive(i))

print(f'Список чисел фибоначи  для k = {num} с учетом отрицательных индексов \n{fibonacci_list}')


# Вариант с использованием циклов

# print('Введите число')
# num = abs(int(input()))
# fibonacci_list = []
# for i in range(0, -num - 1, -1):
#     if i == 0: 
#         fibonacci_list.append(0)
#     elif i == -1:
#         fibonacci_list.append(1)
#     elif i == -2:
#         fibonacci_list.append(-1)
#     else:
#         fibonacci_list.append(fibonacci_list[-2] - fibonacci_list[-1])

# for i in range(len(fibonacci_list) // 2):
#     temp = fibonacci_list[-(i + 1)]
#     fibonacci_list[-(i + 1)] = fibonacci_list[i]
#     fibonacci_list[i] = temp

# size = len(fibonacci_list) - 1

# for i in range(1, num + 1):
#     if i == 1 or i == 2:
#         fibonacci_list.append(1)
#     else:
#         fibonacci_list.append(fibonacci_list[size + i-1] + fibonacci_list[size + i - 2])

# print(f'Список чисел фибоначи  для k = {num} с учетом отрицательных индексов \n{fibonacci_list}')