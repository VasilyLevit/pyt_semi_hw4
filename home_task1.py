# 1. Вычислить число c заданной точностью d
# Пример:при $d = 0.001, π = 3.141

def round(n, d):
    l = len(d)
    return n[0:l]

num = str(2 ** 0.5)
accur = str(0.0001)
print(num)
print(round(num, accur))