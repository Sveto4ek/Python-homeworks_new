# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
# с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
my_list = [6, 4, 4, 2]
while True:
    try:
        if input('Ввести еще число? да/нет ') == 'да':
            el = int(input('Введите натуральное число: '))
            my_list.append(el)
        else:
            my_list.sort(reverse=True)
            print(my_list)
            break
    except ValueError:
        print('Не число')

