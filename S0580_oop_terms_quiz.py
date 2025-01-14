"""
Kør dette program.
Tilføj oop-relaterede kommentarer til denne kode.
    Eksempler:
        class definition / klasse definition
        constructor / konstruktor
        inheritance / nedarvning
        object definition / objekt definition
        attribute / attribut
        method / metode
        polymorphism / polymorfisme
        encapsulation: protected attribute / indkapsling: beskyttet attribut
        encapsulation: protected method / indkapsling: beskyttet metode
"""


class Building: # This is a Class Definition
    def __init__(self, area, floors, value): # This is a constructor
        self.area = area    # This is an attribute
        self.floors = floors
        self._value = value # This is a protected attribute

    def renovate(self): # This is a method
        print("Installing an extra bathroom...")
        self._adjust_value(10) # This calls a protected method withing the same class

    def _adjust_value(self, percentage):  # This is a protected method
        self._value *= 1 + (percentage / 100) # This changes a protected attribute
        print(f'Value has been adjusted by {percentage}% to {self._value:.2f}\n')


class Skyscraper(Building): # This is another Class Definition that inherits from the previous class

    def renovate(self): # Method
        print("Installing a faster elevator.")
        self._adjust_value(6)


small_house = Building(160, 2, 200000)  # This creates an object of the class Building
skyscraper = Skyscraper(5000, 25, 10000000) # This creates an object of the class Skyscraper

for building in [small_house, skyscraper]: # Polymorphism
    print(f'This building has {building.floors} floors and an area of {building.area} square meters.')
    building.renovate()
