# 1)	Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div_func():
    try:
        divs = float(input('Делимое: ')) / float(input('Делитель: '))
    except ZeroDivisionError:
        print('Деление на ноль!')
        divs = 0
    return divs
result = div_func()
print(result)
