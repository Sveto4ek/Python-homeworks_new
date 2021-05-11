# 3)	Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.

def my_func(var_1, var_2, var_3):
    my_list = sorted([var_1, var_2, var_3])
    print(my_list[1] + my_list[2])
print(my_func(10,2,15))
