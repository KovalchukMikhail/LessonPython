# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит что ее нет

def Creat_List ():
    print ('Введите количество элементов списка: ')
    size = int(input())
    new_list = []
    for i in range(size):
        print(f'Введите {i + 1} элемент списка')
        new_list.append(input())
    return new_list


list = Creat_List()
search_text = input('Введите искомое вхождение: ')
count = 0
index_list = []
for i in range(len(list)):
    if list[i] == search_text:
        index_list.append(i)


if len(index_list) > 1:
    print (f'Второе вхождение {search_text} имеет индекс {index_list[1]}')
else: print('Второго вхождения нет')