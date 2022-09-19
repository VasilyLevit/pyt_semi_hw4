# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k_max = 3
k = k_max

list_coeff = random.sample(range(0, 100), k+1)

data = open('file40.txt', 'w')

for coeff in list_coeff:
    if k == k_max:
        if coeff > 1:
            data.write(str(coeff) + '*x^' + str(k))
        elif coeff == 1:
            data.write('x^' + str(k))    
    elif k > 1 and k != k_max:
        if coeff > 1:
            data.write(' + ' + str(coeff) + '*x^' + str(k))
        elif coeff == 1:
            data.write(' + ' + 'x^' + str(k))
    elif k == 1:
        if coeff > 1:
            data.write(' + ' + str(coeff) + '*x')
        elif coeff == 1:
            data.write(' + ' + 'x')
    else:
        if coeff >= 1:
            data.write(' + ' + str(coeff))
    k -= 1
data.write(' = 0')
data.close