# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

""" string = '1 75 43 2 -5 375 21'
print(string)
str_num = string.split( )
numbers = []
for i in range(len(str_num)):
    numbers.append(int(str_num[i]))
print(numbers)
print(min(numbers), max(numbers)) """

string = '1 75 43 2 -5 375 21'
print(string)
str_num = string.split( )
numbers = []
for i in str_num:
    numbers.append(int(i))
print(numbers)
print(min(numbers), max(numbers))