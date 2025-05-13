# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city
        self.__identity = "Secret"  # Private attribute (encapsulation)

    def introduce(self):
        return f"I am {self.name}, protector of {self.city}!"

    def use_power(self):
        return f"{self.name} uses {self.power}!"

    # Getter for private attribute
    def get_identity(self):
        return self.__identity

    # Setter for private attribute
    def set_identity(self, identity):
        self.__identity = identity

# Subclass (inherits from Superhero)
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    # Override method (Polymorphism)
    def use_power(self):
        return f"{self.name} soars through the sky at {self.flight_speed} km/h using {self.power}!"


if __name__ == "__main__":
    hero1 = Superhero("Night Shadow", "Invisibility", "Johannesburg")
    print(hero1.introduce())
    print(hero1.use_power())
    print("Identity:", hero1.get_identity())
    hero1.set_identity("Lerato D.")
    print("Updated Identity:", hero1.get_identity())

    print()

    hero2 = FlyingHero("Sky Blaze", "Fire Wings", "Cape Town", 500)
    print(hero2.introduce())
    print(hero2.use_power())  # This calls the overridden version

