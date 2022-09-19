# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# *2) с помощью дополнительных библиотек Python
# a * (x**2) + b * x + c = 0

def xx(a, b, c):
    d = (b * b) - (4 * a * c)
    if d > 0:
        d = d ** 0.5
        x1 = (-b + d) / 2 * a
        x2 = (-b - d) / 2 * a
        return x1, x2
    if d == 0:
        d = d ** 0.5
        x = -b / 2 * a
        return x
    else:
        print ('Корней нет')
    # return None  # вместо else

a = 1
b = -12
c = 9

print(xx(a, b, c))