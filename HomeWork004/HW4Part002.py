# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def Prime_num_generator(number): #генератор простых чисел от 2 до N
    list = []
    for i in range(2, number + 1):
        count = 0
        for j in range(2, i + 1):
            if i % j == 0:
                count += 1
        if count == 1:
            list.append(i)
    return(list)

def Prime_num_list(number):
    new_list = Prime_num_generator(number)
    result_list = []
    while number != 1:
        for i in new_list:
            if number % i == 0:
                result_list.append(i)
                number //= i
                break
    return result_list

print ('Введите натуральное число N: ')
num = int(input())
num_list = Prime_num_list(num)
if len(num_list) == 1:
    print(f'{num} является простым числом')
else:
    print(f'Список простых множителей числа {num}:\n{num_list}')


