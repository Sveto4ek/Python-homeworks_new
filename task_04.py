vvod = int(input('Введите целое положительное число: '))
max = 0
while vvod > 0:
    if (vvod % 10) > max:
        max = vvod % 10
    vvod = vvod // 10
print(max)