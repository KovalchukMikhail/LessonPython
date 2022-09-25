# Напишите программу которая на вход принимает 5 чисел и находит максимальное из них


print('Введите количество цифр')
size = int(input())

numbers = []
for i in range(0, size):
    print('Введите ', i+1, 'число')
    numbers.append(int(input()))

    if i == 0:
         max = numbers[0]
    elif i > 0:
        if max < numbers[i]:
            max = numbers[i]
         


print('Вы ввели: ')
print(numbers)
#for i in numbers:
#    print(i)

print('Наибольшее число: ', max)

