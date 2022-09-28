# Для натурального n создать словарь индекс - значение, состоящее из элементов последовательности 3n + 1

# print ('Введите число N')
# number = int(input())
# list = []
# for i in range (1, number + 1):
#     list.append(f'{i}: {3*i + 1}')
# print (list)


print ('Введите число N')
number = int(input())
dict = {}
for i in range (1, number + 1):
    dict[i] = 3*i + 1
print (dict)

print (dict.get(6))

