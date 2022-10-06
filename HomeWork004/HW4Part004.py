# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

from datetime import datetime
import time

def Random_number (min, max):
    if abs(max) > abs (min):
        check = min - 1
        max_abs = max + 1
    else:
        check = max + 1
        max_abs = min - 1
    random_number = check
    while random_number < min or random_number > max:
        temp_number = (float(time.time()) * float(datetime.now().time().microsecond)) / 1000000
        sign = -1
        if int(temp_number) % 2 != 0:
            sign = 1
        temp_number = temp_number - int(temp_number)
        random_number = abs(max_abs) * temp_number * sign
        random_number = int(random_number)
        time.sleep(0.000001)
    return random_number

print('Введите натуральную степень k:')
k = int(input())

with open('text.txt', 'w') as file:
    for i in range(k, -1, -1):
        temp = Random_number (-100, 100)
        if i == k:
            if temp < 0:
                file.write(f'{temp}x**{i} ')
            if temp > 0:
                file.write(f'{temp}x**{i} ')
        elif i == 0:
            if temp < 0:
                file.write(f'- {-temp} ')
            if temp > 0:
                file.write(f'+ {temp} ')
        elif temp != 0:
            if temp < 0:
                file.write(f'- {-temp}x**{i} ')
            if temp > 0:
                file.write(f'+ {temp}x**{i} ')
    file.write('= 0')