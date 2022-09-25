# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

print('Введите координату Х точки А: ', end = '\t')
pointAX = float(input())
print('Введите координату Y точки A: ', end = '\t')
pointAY = float(input())

print('Введите координату Х точки B: ', end = '\t')
pointBX = float(input())
print('Введите координату Y точки B: ', end = '\t')
pointBY = float(input())

lengthAToB = ((pointAX - pointBX) ** 2 + (pointAY - pointBY) ** 2) ** 0.5
print(f'\nРасстояние между точками А (x = {pointAX}; y = {pointAY}) и B (x = {pointBX}; y = {pointBY}) равно {lengthAToB}')