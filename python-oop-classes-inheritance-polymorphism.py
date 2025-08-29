# =============================================
# OOP Assignment - Python Classes and Polymorphism
# Author: Ojobor Jude Ikechukwu
# GitHub SEO Keywords: Python OOP, Class Inheritance, Polymorphism, Encapsulation, Constructors
# =============================================

# -------------------------------
# Assignment 1: Design Your Own Class (Smartphone Example)
# -------------------------------

class Smartphone:
    """
    Smartphone Class 📱
    This class represents a smartphone with attributes and methods.
    Demonstrates encapsulation, constructors, and object methods in Python OOP.
    """

    def __init__(self, brand, model, battery_capacity):
        # Constructor initializes unique smartphone details
        self.brand = brand
        self.model = model
        self.__battery_capacity = battery_capacity  # Encapsulation (private attribute)

    def make_call(self, number):
        """Simulate making a phone call 📞"""
        print(f"{self.brand} {self.model} is calling {number}...")

    def browse_internet(self):
        """Simulate browsing the internet 🌍"""
        print(f"{self.brand} {self.model} is browsing the internet.")

    def get_battery_capacity(self):
        """Public getter method for encapsulated battery capacity 🔋"""
        return self.__battery_capacity


# Inheritance Example: GamingSmartphone inherits Smartphone
class GamingSmartphone(Smartphone):
    """
    GamingSmartphone 🎮
    Inherits from Smartphone and adds gaming-specific features.
    Demonstrates OOP inheritance and method extension.
    """

    def __init__(self, brand, model, battery_capacity, cooling_system):
        # Call parent constructor
        super().__init__(brand, model, battery_capacity)
        self.cooling_system = cooling_system

    def play_game(self, game_name):
        """Simulate playing a mobile game 🎮"""
        print(f"{self.brand} {self.model} is playing {game_name} with {self.cooling_system} cooling system.")


# -------------------------------
# Assignment 2: Polymorphism Challenge (Vehicles Example)
# -------------------------------

class Vehicle:
    """
    Vehicle Base Class 🚙
    Defines a move() method to be overridden by subclasses.
    Demonstrates polymorphism in Python OOP.
    """
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")


# -------------------------------
# Example Run
# -------------------------------
if __name__ == "__main__":
    # Assignment 1 Test
    phone1 = Smartphone("Samsung", "Galaxy S24", "5000mAh")
    phone1.make_call("+2348061599859")
    phone1.browse_internet()
    print("Battery Capacity:", phone1.get_battery_capacity())

    gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", "6000mAh", "Liquid Cooling")
    gaming_phone.play_game("PUBG Mobile")
    print("Battery Capacity:", gaming_phone.get_battery_capacity())

    print("\n--- Polymorphism Example ---")
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        v.move()
