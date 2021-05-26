# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

f = open('file_01.txt', 'w')
data = []
while True:
    data_add = input('Введите данные: ')
    if data_add == '':
        break
    data.append(data_add)
f.writelines('\n'.join(data))
f.close()
