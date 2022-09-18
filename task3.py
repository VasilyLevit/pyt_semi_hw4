# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# Ответ записать в файл.

# алгоритм Евклида
""" a = 13
b = 7

count = a * b

while (a != b):
    if a > b:
        a = a - b
    else:
        b = b - a
print(count/b) """

# библиотеки
""" import math
a = int(input('Введите a: '))
b = int(input('Введите b: '))
print(math.lcm(a, b))

with open('file1.txt', 'w') as f:
    f.write(str(math.lcm(a, b))) """

# разложение чисел на простые множители 
# (далее нужно найти объединение полученных списков (множеств?) и разделить на пересечение их)
""" a = int(input('Введите a: '))
b = int(input('Введите b: '))

def find_div(n):
    dividers = []

    for i in range(2, n):
        while n % i == 0:
            n //= i
            dividers.append(i)
    return dividers

print(find_div(a))
print(find_div(b)) """

# еще один алгоритм: 
# взять большее из чисел, проверить не является ли оно кратным меньшему,  
# далее начать прибавлять к нему в цикле по единичке, 
# пока не получим число, которое делится на оба исходных числа без остатка

a = int(input('Введите a: '))
b = int(input('Введите b: '))

def nok(a, b):
    start = max(a, b)
    while True:
        if start % a == 0 and start % b == 0:
            break
        start += 1
    return start

print(nok(a, b))