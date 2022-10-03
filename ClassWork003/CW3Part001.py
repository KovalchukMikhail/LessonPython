# Задайте список напишите программу которая определит присутствует ли в задоном списке строк
# некоторое число, Вывести есть ли вообще и в каком элементе(вывести элемент)
list = ['hdsjjda', 'ksdhh65', 'hjhsd78', 'jhjhdsa96', 'ua67', 'faf9753', '56']
num = input('Введите искомое число: ')
new_list = []
count = 0
index_list = []
for i in list:
    if i.find(num) != -1:
        new_list.append(i)
        index_list.append(count)
    count += 1

if len(index_list) > 0:
    print (f'Число {num} содержится в следующих элементах списка:')

    for i in range(len(index_list)):
        print (f'В элементе с индексом {index_list[i]}: {new_list[i]}')

