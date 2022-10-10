# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнить условие А[i] - 1 = A[i-1]. Найдите это число

with open('text.txt', 'r') as file:
    text = [int(i) for i in file.read().split()]
    print(text)

list_result = [(text[i] - 1) for i in range(len(text)) if i != 0 and text[i - 1] != text[i] - 1]

print(list_result)


