# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

# 1 вариант ******************************************
# list = [1, 1, 2, 3, 4, 5, 5]
# list_res = []
# for i in list:
#     count = 0
#     for j in list:
#         if j == i:
#             count += 1
#     if count == 1:
#         list_res.append(i)
# print(list_res)

# 2 вариант (с использованием функции count)**********
def unique_num(list_in):
        list_out = []
        for i in list_in:
                if (list_in.count(i)) == 1:
                        list_out.append(i)
        return list_out

list = [1, 1, 2, 3, 4, 5, 5]
print(unique_num(list))