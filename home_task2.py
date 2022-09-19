# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

def find_prime(n):
    prime_num = []
    for i in range(2, n):
        while n % i == 0:
            n //= i
            prime_num.append(i)
    return prime_num

n = 52
print(find_prime(n))