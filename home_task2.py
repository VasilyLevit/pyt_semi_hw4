# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

n = 20

def find_div(n):
    dividers = []

    for i in range(2, n):
        while n % i == 0:
            n //= i
            dividers.append(i)
    return dividers

print(find_div(n))