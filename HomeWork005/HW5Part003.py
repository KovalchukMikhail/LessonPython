# 3. Создайте программу для игры в 'Крестики-нолики'.

from asyncio import events
from encodings import utf_8
import tkinter as tk
from functools import partial


class Game:
    player = 1
    win_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    list_check = []
    player_one_list = []
    player_two_list = []

def Win(sign):
    window_second = tk.Tk()
    window_second.geometry('200x100+600+300')
    window_second.title(f'Крестики нолики')
    lable_name = tk.Label(text = f'Игра окончена. \nПобедили {sign}', height=5, width= 20)
    lable_name.pack()
    tk.mainloop()
    
sign = 'O'
def Button(number_button, sign):
    if number_button in Game.list_check:
        return
    Game.list_check.append(number_button)
    sign = sign_in_game.get()
    if sign == 'X':
        Game.player_one_list.append(number_button)
    else:
        Game.player_two_list.append(number_button)
    sign = 'X' if sign == 'O' else 'O'
    sign_in_game.set(sign)
    if number_button == 1:
        button_one['text'] = sign
    elif number_button == 2:
        button_two['text'] = sign
    elif number_button == 3:
        button_three['text'] = sign
    elif number_button == 4:
        button_four['text'] = sign
    elif number_button == 5:
        button_fife['text'] = sign
    elif number_button == 6:
        button_six['text'] = sign
    elif number_button == 7:
        button_seven['text'] = sign
    elif number_button == 8:
        button_eight['text'] = sign
    elif number_button == 9:
        button_nine['text'] = sign
    count = 0
    for i in Game.win_list:
        for j in i:
            for k in Game.player_one_list:
                if k == j:
                    count += 1
        if count == 3:
            window_first.destroy()
            Win(sign)
        count = 0
            
    for i in Game.win_list:
        for j in i:
            for k in Game.player_two_list:
                if k == j:
                    count += 1
        if count == 3:
            window_first.destroy()
            Win(sign)
        count = 0
            



window_first = tk.Tk()
window_first.geometry('200x250+600+300')
window_first.title(f'Крестики - нолики')
sign_in_game = tk.StringVar()
sign_in_game.set(sign)
lable_name = tk.Label(text = 'Игра началась', height=5, width= 20)
lable_name.pack()
button_one = tk.Button(text=' ', width=3, height=2, command=partial(Button, 1, sign))
button_two = tk.Button(text=' ', width=3, height=2, command=partial(Button, 2, sign))
button_three = tk.Button(text=' ', width=3, height=2, command=partial(Button, 3, sign))
button_four = tk.Button(text=' ', width=3, height=2, command=partial(Button, 4, sign))
button_fife = tk.Button(text=' ', width=3, height=2, command=partial(Button, 5, sign))
button_six = tk.Button(text=' ', width=3, height=2, command=partial(Button, 6, sign))
button_seven = tk.Button(text=' ', width=3, height=2, command=partial(Button, 7, sign))
button_eight = tk.Button(text=' ', width=3, height=2, command=partial(Button, 8, sign))
button_nine = tk.Button(text=' ', width=3, height=2, command=partial(Button, 9, sign))
button_one.place(x=40, y=50)
button_two.place(x=80, y=50)
button_three.place(x=120, y=50)
button_four.place(x=40, y=100)
button_fife.place(x=80, y=100)
button_six.place(x=120, y=100)
button_seven.place(x=40, y=150)
button_eight.place(x=80, y=150)
button_nine.place(x=120, y=150)
tk.mainloop()