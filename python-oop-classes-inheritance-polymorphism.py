"""2026 recovery revision; operations are string-returning simulations, not network calls."""

class Smartphone:

    def __init__(self, brand, model, battery_capacity):
        if not isinstance(battery_capacity, int) or isinstance(battery_capacity, bool) or battery_capacity <= 0:
            raise ValueError('Battery capacity must be a positive integer in mAh')
        self.brand, self.model = (brand, model)
        self.__battery_capacity = battery_capacity

    def make_call(self, number):
        return f'{self.brand} {self.model}: simulated call to {number}'

    def browse_internet(self):
        return f'{self.brand} {self.model}: simulated browsing'

    def get_battery_capacity(self):
        return self.__battery_capacity

class GamingSmartphone(Smartphone):

    def __init__(self, brand, model, battery_capacity, cooling_system):
        super().__init__(brand, model, battery_capacity)
        self.cooling_system = cooling_system

    def play_game(self, game_name):
        return f'Simulated {game_name} with {self.cooling_system} cooling'

class Vehicle:

    def move(self):
        raise NotImplementedError('Subclasses define movement')

class Car(Vehicle):

    def move(self):
        return 'Driving'

class Plane(Vehicle):

    def move(self):
        return 'Flying'

class Boat(Vehicle):

    def move(self):
        return 'Sailing'

def main():
    phone = Smartphone('Example', 'Study', 5000)
    print(phone.make_call('example-number'))
    print(phone.browse_internet())
    for vehicle in (Car(), Plane(), Boat()):
        print(vehicle.move())
if __name__ == '__main__':
    main()
