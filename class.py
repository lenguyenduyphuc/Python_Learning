#11.10 LAB: Plant information
class Plant:
    def __init__(self, plant_name, plant_cost):
        self.plant_name = plant_name
        self.plant_cost = plant_cost
    
    def print_info(self):
        print(f'   Plant name: { self.plant_name }')
        print(f'   Cost: { self.plant_cost }')

class Flower(Plant):
    def __init__(self, plant_name, plant_cost, is_annual, color_of_flowers):
        Plant.__init__(self, plant_name, plant_cost)
        self.is_annual = is_annual
        self.color_of_flowers = color_of_flowers

    def print_info(self):
        Plant.print_info(self)
        print(f'   Annual: { self.is_annual }')
        print(f'   Color of flowers: { self.color_of_flowers }')

def print_list(garden):
    for i, plant in enumerate(garden, 1):
        print(f"Plant {i} Information:")
        plant.print_info()
        print()

if __name__ == "__main__":
    my_garden = []
    user_string = input()
    while user_string != '-1':
        parts = user_string.split()
        if parts[0] == 'flower':
            _, name, cost, is_annual, color = parts
            flower_obj = Flower(name, int(cost), is_annual, color)
            my_garden.append(flower_obj)
        elif parts[0] == 'plant':
            _, name, cost = parts
            plant_obj = Plant(name, int(cost))
            my_garden.append(plant_obj)

        user_string = input()

    print_list(my_garden)


