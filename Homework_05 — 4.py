# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый
# текстовый файл.
#
in_f = open('file_04', encoding='UTF-8')
ln = in_f.readlines()
my_list = []
for el in ln:
    my_list.append(el.split(' '))
while True:
    for i, x in enumerate(my_list):
        if i == 0:
            x[0] = 'Один'
            my_list[i] = ' '.join(x)
        if i == 1:
            x[0] = 'Два'
            my_list[i] = ' '.join(x)
        if i == 2:
            x[0] = 'Три'
            my_list[i] = ' '.join(x)
        if i == 3:
            x[0] = 'Четыре'
            my_list[i] = ' '.join(x)
    else:
        break
in_f.close()
out_f = open('file_04_1', 'w', encoding='UTF-8')
out_f.writelines(''.join(my_list))
out_f.close()
