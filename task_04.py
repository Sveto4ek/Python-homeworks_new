# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color,
# name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что
# машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
# WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите
# результат. Выполните вызов методов итакже покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self, speed):
        print(f'{self.name} едет со скоростью {speed} км/ч')


class TownCar(Car):
    def show_speed(self, speed):
        print('Вы превысили скорость!' if speed > 60 else 'Полет нормальный')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self, speed):
        print('Вы превысили скорость!' if speed > 40 else 'Полет нормальный')


class PoliceCar(Car):
    pass

polosedan = TownCar(50, 'blue', 'Ласточка', False)
print(polosedan.__dict__)
polosedan.go()
polosedan.turn('налево')
polosedan.show_speed(70)
polosedan.stop()

ferrari = SportCar(150, 'red', 'Ракета', False)
print(f'\n{ferrari.__dict__}')
ferrari.go()
ferrari.turn('направо')
ferrari.show_speed(200)
ferrari.stop()

gazel = WorkCar(40, 'white', 'Рабочая лошадка', False)
print(f'\n{gazel.__dict__}')
gazel.go()
gazel.turn('направо')
gazel.show_speed(100)
gazel.stop()

police = PoliceCar(80, 'black', 'Полицейская машина', True)
print(f'\n{police.__dict__}')
police.go()
police.turn('направо')
police.show_speed(80)
police.stop()
