# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('file_05.txt', 'w+') as f:
    f.write('5 6 8 2 1')
    f.seek(0)
    print(sum(map(int, f.readline().split(' '))))
