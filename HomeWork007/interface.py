
from functools import partial
from statistics import geometric_mean
import tkinter as tk

equation = ''
result = ''
close = 0
geometry_current = '205x275+600+300'


def Get_data( temp_equation = '', text_result = 'result'):
    global equation
    equation = temp_equation
    window = tk.Tk()
    window.geometry(geometry_current)
    window.title(f'Калькулятор')
    def Info(event):
        global geometry_current
        geometry_current = window.geometry()
    window.bind('<Configure>', Info)
    text_lable = 'Введите выражение с клавиатуры или\nиспользуйте кнопки под строкой ввода'
    lable_start = tk.Label(text = text_lable, font = 'Arial 8')
    lable_start.place(x=0, y=2)
    lable_result = tk.Label(text = text_result, font = 'Arial 12')
    lable_result.place(x=10, y=65)
    def Get(event):
        global equation
        equation = entry.get()
        if equation != temp_equation and equation[-1].isdigit():
            window.destroy()
    def Get_button():
        global equation
        equation = entry.get()
        if equation != temp_equation and equation[-1].isdigit():
            window.destroy()
    entry = tk.Entry(font = "Arial 12")
    entry.insert(0, equation)
    entry.place(x=2, y=40, width=200, )
    entry.bind('<Return>', Get)
    button_plus = tk.Button(text='+', width=2, height=1, font = 'Arial 14', command=partial(entry.insert, 100, '+'))
    button_plus.place(x=170, y=100)
    button_minus = tk.Button(text='-', width=2, height=1, font = 'Arial 14', command=partial(entry.insert, 100, '-'))
    button_minus.place(x=170, y=140)
    button_multiply = tk.Button(text='x', width=2, height=1, font = 'Arial 14', command=partial(entry.insert, 100, 'x'))
    button_multiply.place(x=135, y=100)
    button_divide = tk.Button(text='/', width=2, height=1, font = 'Arial 14', command=partial(entry.insert, 100, '/'))
    button_divide.place(x=135, y=140)
    button_bracket_left = tk.Button(text='(', width=2, height=1, font = 'Arial 14', command=partial(entry.insert, 100, '('))
    button_bracket_left.place(x=135, y=180)
    button_bracket_right = tk.Button(text=')', width=2, height=1, font = 'Arial 14', command=partial(entry.insert, 100, ')'))
    button_bracket_right.place(x=170, y=180)
    button_equal = tk.Button(text='=', width=4, height=1, font = 'Arial 19', command=partial(Get_button))
    button_equal.place(x=132, y=220)
    button_one = tk.Button(text='1', width=3, height=1, font = 'Arial 14', command=partial(entry.insert, 100, '1'))
    button_one.place(x=2, y=100)
    button_two = tk.Button(text='2', width=3, height=1, font = 'Arial 14', command=partial(entry.insert, 100, '2'))
    button_two.place(x=45, y=100)
    button_Three = tk.Button(text='3', width=3, height=1, font = 'Arial 14', command=partial(entry.insert, 100, '3'))
    button_Three.place(x=90, y=100)
    button_four = tk.Button(text='4', width=3, height=1, font = 'Arial 14', command=partial(entry.insert, 100, '4'))
    button_four.place(x=2, y=140)
    button_fife = tk.Button(text='5', width=3, height=1, font = 'Arial 14', command=partial(entry.insert, 100, '5'))
    button_fife.place(x=45, y=140)
    button_six = tk.Button(text='6', width=3, height=1, font = 'Arial 14', command=partial(entry.insert, 100, '6'))
    button_six.place(x=90, y=140)
    button_seven = tk.Button(text='7', width=3, height=1, font = 'Arial 14', command=partial(entry.insert, 100, '7'))
    button_seven.place(x=2, y=180)
    button_eight = tk.Button(text='8', width=3, height=1, font = 'Arial 14', command=partial(entry.insert, 100, '8'))
    button_eight.place(x=45, y=180)
    button_nine = tk.Button(text='9', width=3, height=1, font = 'Arial 14', command=partial(entry.insert, 100, '9'))
    button_nine.place(x=90, y=180)
    button_zero = tk.Button(text='0', width=4, height=1, font = 'Arial 19', command=partial(entry.insert, 100, '0'))
    button_zero.place(x=2, y=220)
    button_point = tk.Button(text='.', width=3, height=1, font = 'Arial 19', command=partial(entry.insert, 100, '.'))
    button_point.place(x=75, y=220)

    def On_closing():
        global close
        close = 1
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", On_closing)
    tk.mainloop()
