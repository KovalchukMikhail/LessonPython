# 2. Создайте программу для игры с конфетами человек против человека.

# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'


from asyncio import events
from encodings import utf_8
import tkinter as tk
from functools import partial

class Game:
    name = ''
    number = ''
    part = ''

def Name_player(num):
    window_first = tk.Tk()
    window_first.geometry('400x150+600+300')
    window_first.title(f'Окно ввода имени {num} игрока')
    lable_name = tk.Label(text = f'Введити имя {num} игрока \nи нажмити Enter', height=5, width= 20)
    lable_name.pack()
    entry_name = tk.Entry()
    entry_name.pack()
    def Get(event):
        Game.name = entry_name.get()
        window_first.destroy()
    entry_name.bind('<Return>', Get)
    tk.mainloop()

def Game(rules, count, name_player):
    if name_player == 'Компьютер':
        if count < 29:
            number = count
        elif count - count % 29 != 0:
            number = count % 29
        else:
            number = 1
        window_second = tk.Tk()
        window_second.geometry('600x200+500+300')
        window_second.title('Игра в конфеты')
        def Button_one():
            window_second.destroy()
        lable_rules = tk.Label(text = rules)
        lable_rules.pack()
        lable_comp = tk.Label(text = f'Осталось {count} конфет. Ход игрока {name_player}\n {number} конфет', height='5')
        lable_comp.pack()
        button_one = tk.Button(text='Ок', width=2, height=1, command=partial(Button_one))
        button_one.pack()
        Game.number = str(number)
        tk.mainloop()
    else:
        window_second = tk.Tk()
        window_second.geometry('600x200+500+300')
        window_second.title('Игра в конфеты')
        lable_rules = tk.Label(text = rules)
        lable_rules.pack()
        lable_game = tk.Label(text = f'Осталось {count} конфет. Ход игрока {name_player}\nВведите количество конфет', height='5')
        lable_game.pack()
        entry_number = tk.Entry()
        entry_number.pack()
        def Get(event):
            Game.number = entry_number.get()
            window_second.destroy()
        entry_number.bind('<Return>', Get)
        tk.mainloop()


window_first = tk.Tk()
window_first.geometry('400x150+600+300')
window_first.title(f'Выбор варианта игры')
lable_name = tk.Label(text = 'Выберети вариант игры', height=5, width= 20)
lable_name.pack()
Game.game = '1'
def Button_one():
    Game.game = '1'
    window_first.destroy()
def Button_two():
    Game.game = '2'
    window_first.destroy()
button_one = tk.Button(text='1 игрок', width=10, height=1, command=partial(Button_one))
button_two = tk.Button(text='2 игрока', width=10, height=1, command=partial(Button_two))
button_one.pack()
button_two.pack()
tk.mainloop()


with open('rules.txt', 'r', encoding='utf_8') as file:
    rules = file.read()


Name_player(1)
name_player_one = Game.name

if Game.game == '2':
    Name_player(2)
    name_player_two = Game.name
    count = 150
    name = name_player_two
    number = 0
    while count != 0:
        if name == name_player_two:
            name = name_player_one
        else:
            name = name_player_two
        text = rules
        while True:
            Game(text, count, name)
            number = Game.number
            if number.isdigit() and int(number) < 29  and int(number) > 0 and int(number) <= count:
                break
            else:
                text = "Вы ввели неверное значение"
        count = count - int(number)

if Game.game == '1':
    count = 150
    name_player_two = 'Компьютер'
    name = name_player_two
    number = 0
    while count != 0:
        if name == name_player_two:
            name = name_player_one
        else:
            name = name_player_two
        text = rules
        while True:
            Game(text, count, name)
            number = Game.number
            if number.isdigit() and int(number) < 29  and int(number) > 0 and int(number) <= count:
                break
            else:
                text = "Вы ввели неверное значение"
        count = count - int(number)



window_second = tk.Tk()
window_second.geometry('400x100+500+300')
window_second.title('Победитель')
lable_win = tk.Label(text = f'Победил игрок {name}')
lable_win.pack()
tk.mainloop()


