# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +, -, /, *, приоритет операций стандартный

text = input('Введите уравнение: ')

list = text.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').split()

# start = 0
# end = 0

# for i in range(len(text)):
#     if text[i].isdigit() and i+1 < len(text):
#         end += 1
#     elif i + 1 == len(text):
#         end += 1
#         list.append(text[start: end])
#     else:
#         list.append(text[start: end])
#         list.append(text[i])
#         start = i + 1
#         end = i + 1

i = 0
num = 0      
while '*' in list or '/' in list:
    if list[i] == '*' or list[i] == '/':
        num = (int(list[i-1])/int(list[i+1])) if list[i] == '/' else (int(list[i-1])*int(list[i+1]))
        list[i-1] = num
        list.pop(i)
        list.pop(i)
        i = -1
    i += 1


print(list)
i = 0 
while '-' in list or '+' in list:
    if list[i] == '-' or list[i] == '+':
        num = (int(list[i-1])-int(list[i+1])) if list[i] == '-' else (int(list[i-1])+int(list[i+1]))
        list[i-1] = num
        list.pop(i)
        list.pop(i)
        i = -1
    i += 1


print(list)
