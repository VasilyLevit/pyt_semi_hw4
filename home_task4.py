# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = 2

list_coef = random.sample(range(0, 10), k)
print(list_coef)

for i in range(k, 0, -1):
    coef = random.randint(0,2)
    if coef > 1:
        print(f'{coef}*x^{i} +', end = ' ')
    elif coef == 1:
        print(f'x^{i} + ', end = ' ')
