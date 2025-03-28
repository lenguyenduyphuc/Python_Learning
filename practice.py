class Vehicle:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed_to_set):
        self.speed = speed_to_set

    def print_speed(self):
        print(self.speed)


class Car(Vehicle):
    def print_car_speed(self):
        print('Speed: ', end = '')
        self.print_speed()


class ElectricCar(Car):
    def __init__(self):
        self.battery_level = 0

    def set_battery_level(self, level_to_set):
        self.battery_level = level_to_set

    def print_battery_level(self):
        print(f'Battery: {self.battery_level}')


myCar = ElectricCar()
myCar.set_speed(20)
myCar.set_battery_level(80)

myCar.print_car_speed()
myCar.print_battery_level()	
