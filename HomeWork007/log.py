import datetime
path = 'log.txt'
def Log(text):
    global path
    with open(path, 'a', encoding='utf_8') as file:
        file.write(f'{datetime.datetime.now()}: \t{text}\n')