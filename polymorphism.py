class Vehicles:
    def __init__(self, name):
        self.name = name

    def move(self):
        pass  # To be overridden


class Car(Vehicles):
    def __init__(self):
        super().__init__("Car")

    def move(self):
        print(f"{self.name} is driving ")


class Plane(Vehicles):
    def __init__(self):
        super().__init__("Plane")

    def move(self):
        print(f"{self.name} is flying ")


class Boat(Vehicles):
    def __init__(self):
        super().__init__("Boat")

    def move(self):
        print(f"{self.name} is sailing ")


# Usage
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()
