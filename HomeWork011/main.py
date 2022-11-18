import math
import numpy as np
import matplotlib.pyplot as plt


def func(x):
    result = -12*x**4*np.sin(np.cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30
    return result

start_point = -11
end_point = 11
interval = 0.00001
x = np.arange(start_point, end_point, interval)
y = func(x)


roots = []
roots = [round(x[i], 2) for i in range(len(y)-1) if (y[i] < 0 and y[i+1] > 0) or (y[i] > 0 and y[i+1] < 0)]
top_func = [round(x[i+1], 2) for i in range(len(y)-3) if (y[i] < y[i+1] and y[i+1] > y[i+2]) or (y[i] > y[i+1] and y[i+1] < y[i+2])]
check = True if func(top_func[0]) > func(top_func[1]) else False
positive = []
negative = []
start = 0
end = 0

for i in range(len(y)):
    if i + 1 < len(y):
        if y[i] > 0 and y[i+1] < 0:
            positive.append((round(x[start], 1), round(x[i], 1)))
        elif y[i] < 0 and y[i+1] > 0:
            start = i + 1
    elif y[i] > 0:
        positive.append((round(x[start], 1), round(x[i], 1)))

for i in range(len(y)):
    if i + 1 < len(y):
        if y[i] < 0 and y[i+1] > 0:
            negative.append((round(x[start], 1), round(x[i], 1)))
        elif y[i] > 0 and y[i+1] < 0:
            start = i + 1
    elif y[i] < 0:
        negative.append((round(x[start], 1), round(x[i], 1)))
    


plt.figure(figsize=(10, 7))
plt.title(f'Корни функции: {roots}\nЭкстремумы функции:{top_func}\nf>0 на участках: {positive}\nf<0 на участках: {negative}')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.grid()
collor = 'r'
if check:
    x_range = np.arange(start_point, top_func[0], interval)
    y_range = func(x_range)
    collor = 'r'
    plt.plot(x_range, y_range, collor, label="Возростание")
else:
    x_range = np.arange(start_point, top_func[0], interval)
    y_range = func(x_range)
    collor = 'b'
    plt.plot(x_range, y_range, collor, label="Убывание")
current = 0
for i in range(len(top_func) - 1):
    x_range = np.arange(top_func[i], top_func[i+1], interval)
    y_range = func(x_range)
    if collor == 'r':
        collor = 'b'
        if current == 0:
            plt.plot(x_range, y_range, collor, label="Убывание")
            current += 1
        plt.plot(x_range, y_range, collor)
    else:
        collor = 'r'
        if current == 0:
            plt.plot(x_range, y_range, collor, label="Возростание")
            current += 1
        plt.plot(x_range, y_range, collor)
x_range = np.arange(top_func[len(top_func) - 1], end_point, interval)
y_range = func(x_range)
if collor == 'r':
    collor = 'b'
else:
    collor = 'r'
plt.plot(x_range, y_range, collor)
add_y=4000
for i in top_func:
    plt.plot(i, func(i), 'ro')
    plt.text(i, func(i)+add_y, f'x={i}')
    add_y *= -1
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.legend()
plt.show()

