# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = [True, False]
y = [True, False]
z = [True, False]

for i in x:
    for j in y:
        for k in z:
            result = (x or y or z) == (not x or not y or not z)
            print(f'¬({x[i]} ⋁ {y[j]} ⋁ {z[k]}) = ¬{x[i]} ⋀ ¬{y[j]} ⋀ ¬{z[k]} \t {result}')
            if result == False:
                break
        if result == False:
                break
    if result == False:
                break

if result == False:
    print('\nУсловие не выполнено')
else:
    print('\nУсловие выполнено')
