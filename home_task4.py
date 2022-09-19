# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = 2

list_coeff = random.sample(range(0, 10), k+1)
print(list_coeff)

for coeff in list_coeff:
    if k > 1:
        if coeff > 1:
            print(f'{coeff}*x^{k} +', end = ' ')
        elif coeff == 1:
            print(f'x^{k} + ', end = ' ')
    elif k == 1:
        if coeff > 1:
            print(f'{coeff}*x +', end = ' ')
        elif coeff == 1:
            print(f'x + ', end = ' ')
    else:
        if coeff >= 1:
            print(f'{coeff} = 0')
    k -= 1
