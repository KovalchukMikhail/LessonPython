#4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и
# восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.


from encodings import utf_8


print('Введите данные которые необходимо сжать')
with open('Исходный.txt', 'w', encoding='utf_8') as file:
    file.write(input())

with open('Исходный.txt', 'r', encoding='utf_8') as file:
    text = file.read()

new_text = ''
count = 0
start = 0
end = 1
for i in range(len(text)):
    if i + 1 < len(text):
        if text[i] == text[i+1]:
            end = end + 1
        else:
            new_text = f'{new_text}{end - start}{text[i]}'
            start = i + 1
            end = end + 1
    else:
        new_text = f'{new_text}{end - start}{text[i]}'

print(f'текст преобразован в последовательность:\n{new_text}')

with open('Сжатый_текст.txt', 'w', encoding='utf_8') as file:
    file.write(new_text)

input('для востонавления текста нажмите любую клавишу')

with open('Сжатый_текст.txt', 'r', encoding='utf_8') as file:
    text = file.read()

number = ''
text_return = ''
for i in text:
    if i.isdigit():
        number = number + i
    else:
        text_return += int(number)*i
        number = ''

print(f'Востановленный текст представляет последовательность:\n{text_return}')

with open('Востановленный_текст.txt', 'w', encoding='utf_8') as file:
    file.write(text_return)