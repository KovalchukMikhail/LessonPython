# Напишите программу, удаляющую из текста все слова, содержащие "абв"
from encodings import utf_8

print('Введите искомые символы: ')
part_text = input()
with open('text002.txt', 'r', encoding = 'utf_8') as file:
    list = [i for i in file.read().split() if part_text not in i]

print (list)

