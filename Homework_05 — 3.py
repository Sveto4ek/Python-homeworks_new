# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

f = open('file_03')
lines = f.readlines()
total = 0
for i in lines:
    i = i.strip()
    i = i.split(' ')
    total = total + float(i[1])
    if float(i[1]) < 20000:
        print(i[0])
print('Средний доход:', round(total / len(lines)), 'руб.')
f.close()
