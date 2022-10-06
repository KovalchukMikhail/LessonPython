# Найти корни квадратного уравнения ax2 + bx + c = 0, двумя способами. 1 способ, матиматическими формулами. 2 способ библиотеками python.
# Уровнение надо считать из файла 2*x**2 + 4*x - 2 = 0

with open('equation.txt') as equation:
    text = equation.read()


text = text.replace(' ', '')

index_for_a = text.find('x**')
a = text[:index_for_a]
if a.find('*') > 0:
    a = a.rstrip('*')
if a == '':
    a = 1
if a == '-':
    a = -1
a = float(a)


if text.find('x', index_for_a + 1) > 0:
    index_for_b = text.find('x', index_for_a + 1)
    if text.find('+',index_for_a, index_for_b) > 0:
        index_sign = text.find('+',index_for_a, index_for_b )
        b = text[index_sign + 1: index_for_b - 1]
        if b == '':
            b = 1
    elif text.find('-', index_for_a, index_for_b) > 0:
            index_sign = text.find('-', index_for_a, index_for_b)
            b = text[index_sign: index_for_b - 1]
            if b == '':
                b = -1
else:
    b = 0
    index_for_b = index_for_a

b = float(b)

index_for_c = text.find('=')
if text[index_for_c - 1].isdigit():
    if text.find('+',index_for_b, index_for_c) > 0:
        index_sign = text.find('+',index_for_b, index_for_c)
        c = text[index_sign + 1: index_for_c]
    elif text.find('-', index_for_b, index_for_c) > 0:
            index_sign = text.find('-', index_for_b, index_for_c)
            c = text[index_sign: index_for_c]
else:
    c = 0

c = float(c)

d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + d ** 0.5)/(2 * a)
    x2 = (-b - d ** 0.5)/(2 * a)
    result = f'Уровнение {text} \nимеет 2 корня Х1 = {x1} и X2 = {x2}'
elif d == 0:
    x1 = -b/(2 * a)
    result = f'Уровнение {text} имеет 1 корень Х1 = {x1}'
else:
    result = f'Уровнение {text} не имеет корней'

with open('result.txt', 'w', encoding='UTF-8') as file:
    file.write(result)



