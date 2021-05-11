income = float(input('Введите значение выручки в млн: '))
costs = float(input('Введите значение издержек в млн: '))
sotr = 0
if income > costs:
    print('Компания принесла прибыль ', round((income - costs), 1), 'млн')
    roi = (income - costs) * 100 / income
    print('Рентабельность выручки составила: ', round(roi, 1), '%')
    sotr = int(input('Введите количество сотрудников: '))
    print('Прибыль на одного сотрудника: ', round(((income - costs) / sotr), 1), 'млн')
else:
    print('Компания принесла убыток ', (costs - income), 'млн')