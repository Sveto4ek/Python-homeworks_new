# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать
# формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в
# 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    consumption = 25
    def __init__(self, length, width, thickness):
        self.__length = length
        self.__width = width
        self.thickness = thickness

    def mass(self):
        print(f'{self.__length}m * {self.__width}m * {Road.consumption}kg * {self.thickness}cm = {(float(self.__length) * float(self.__width) * Road.consumption * float(self.thickness))/1000}t')

e_95 = Road(10, 3, 10)
e_95.mass()