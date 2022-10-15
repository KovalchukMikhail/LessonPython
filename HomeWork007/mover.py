result_equation = ''

def Mult_or_div(list):
    i = 0
    num = 0
    while 'x' in list or '/' in list:
        if list[i] == 'x' or list[i] == '/':
            if list[i+1] == '-':
                list[i+1] = str(float(list[i+2])*(-1))
                list.pop(i+2)
            num = (float(list[i-1])/float(list[i+1])) if list[i] == '/' else (float(list[i-1])*float(list[i+1]))
            list[i-1] = num
            list.pop(i)
            list.pop(i)
            i = -1
        i += 1
    return list

def Plus_or_minus(list):
    i = 0
    while '-' in list or '+' in list:
        if list[i] == '-' or list[i] == '+':
            if list[i+1] == '-':
                list[i+1] = str(float(list[i+2])*(-1))
                list.pop(i+2)
            num = (float(list[i-1])-float(list[i+1])) if list[i] == '-' else (float(list[i-1])+float(list[i+1]))
            list[i-1] = num
            list.pop(i)
            list.pop(i)
            i = -1
        i += 1
    return list

def Calc(text):
    list = text.replace('+', ' + ').replace('-', ' - ').replace('x', ' x ').replace('*', ' x ').replace('/', ' / ').replace('(', ' ( ').replace(')', ' ) ').split()

    if list[0] == '-':
        list[1] = float(list[1])*-1
        list.pop(0)
    
    list_temp = []
    start = 0
    end = 0

    while '(' in list or ')' in list:
        for i in range(len(list)):
            if list[i] == '(':
                start = i
            if list[i] == ')':
                end = i
                break
        for i in range(start + 1, end):
            list_temp.append(str(list[i]))
        list_temp = Calc(''.join(list_temp))
        list[start] = list_temp[0]
        for _ in range(1, end - start + 1):
            list.pop(start + 1)
        list_temp = []

    list = Mult_or_div(list)
    list = Plus_or_minus(list) 

    return list   

