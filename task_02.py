vvod = int(input('Введите время в секундах: '))
minutes_1 = vvod // 60
chas = minutes_1 // 60
if chas < 10:
    chas = '0' + str(chas)
minutes = minutes_1 % 60
if minutes < 10:
    minutes = '0' + str(minutes)
sec = vvod % 60
if sec < 10:
    sec = '0' + str(sec)
print(f'{chas}:{minutes}:{sec}')
