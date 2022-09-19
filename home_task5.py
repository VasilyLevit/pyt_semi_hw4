# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('file1.txt','w') as data_one:
    data_one.write('5x^2+2x+9')
with open('file2.txt','w') as data_two:
    data_two.write('12x^2+6x+1')

data = open('file1.txt','r')
for line in data:
    lst_one = line.split('+')
data.close

data = open('file2.txt','r')
for line in data:
    lst_two = line.split('+')
data.close

print(lst_one)
print(lst_two)

lst_out1 = []
for term in lst_one:
    if 'x^' in term:
        term_spl = term.split('x^')
        lst_out1.append(term_spl[0])
    elif 'x' in term:
        term_spl = term.split('x')
        lst_out1.append(term_spl[0])
    else:
        lst_out1.append(term)

lst_out2 = []
data = open('file12.txt', 'a')
i = 0
for term in lst_two:
    if 'x^' in term:
        term_spl = term.split('x^')
        lst_out2.append(term_spl[0])
        data.write(str(int(lst_out1[i]) + int(term_spl[0])))
        data.write('x^2+')

    elif 'x' in term:
        term_spl = term.split('x')
        lst_out2.append(term_spl[0])
        data.write(str(int(lst_out1[i]) + int(term_spl[0])))
        data.write('x+')

    else:
        lst_out2.append(term)
        data.write(str(int(lst_out1[i]) + int(term)))
    i += 1

data.close

