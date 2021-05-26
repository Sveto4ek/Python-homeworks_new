# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый
# текстовый файл.
#

num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_list = []

with open('file_04', encoding='UTF-8') as in_f:
    with open('file_04_1', 'w', encoding='UTF-8') as out_f:
        ln = in_f.readlines()
        for el in ln:
            el = el.split(' ', 1)
            my_list.append(num[el[0]] + ' ' + el[1])
        out_f.writelines(my_list)
