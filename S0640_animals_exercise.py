"""
Opgave "Animals"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Alt, hvad du har brug for at vide for at løse denne opgave, finder du i cars_oop-filerne.

Del 1:
    Definer en klasse ved navn Animal.
    Hvert objekt i denne klasse skal have attributterne name (str), sound (str), height (float),
    weight (float), legs (int), female (bool).
    I parentes står data typerne, dette attributterne typisk har.

Del 2:
    Tilføj til klassen meningsfulde metoder __init__ og __repr__.
    Kald disse metoder for at oprette objekter af klassen Animal og for at udskrive dem i hovedprogrammet.

Del 3:
    Skriv en metode ved navn make_noise, som udskriver dyrets lyd i konsollen.
    Kald denne metode i hovedprogrammet.

Del 4:
    Definer en anden klasse Dog, som arver fra Animal.
    Hvert objekt af denne klasse skal have attributterne tail_length (int eller float)
    og hunts_sheep (typisk bool).

Del 5:
    Tilføj til klassen meningsfulde metoder __init__ og __repr__.
    Ved skrivning af konstruktoren for Dog skal du forsøge at genbruge kode fra klassen Animal.
    Kald disse metoder for at oprette objekter af klassen Hund og for at udskrive dem i hovedprogrammet.

Del 6:
    Kald metoden make_noise på Dog-objekter i hovedprogrammet.

Del 7:
    Skriv en metode ved navn wag_tail for Dog. Denne metode udskriver i konsollen noget i stil
    med "Hunden Snoopy vifter med sin 32 cm lange hale".
    Kald denne metode i hovedprogrammet.

Del 8:
    Skriv en funktion mate(mother, father) undenfor klassen. Begge parametre er af typen Dog.
    Denne funktion skal returnere et nyt objekt af typen Dog.
    I denne funktion skal du lave meningsfulde regler for den nye hunds attributter.
    Hvis du har lyst, brug random numbers så mate() producerer tilfældige hunde.
    Sørg for, at denne funktion kun accepterer hunde med det korrekte køn som argumenter.

Del 9:
    I hovedprogrammet kalder du denne metode og udskriver den nye hund.

Del 10:
    Gør det muligt at skrive puppy = daisy + brutus i stedet for puppy = mate(daisy, brutus)
    for at opnå den samme effekt.  Du bliver nok nødt til at google hvordan man laver det.

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import random

class Animal:
    def __init__(self, name: str, sound: str, height: float, weight: float, legs: int, female: bool):
        self.animal_name = name
        self.animal_sound = sound
        self.animal_height = height
        self.animal_weight = weight
        self.animal_legs = legs
        self.isFemale = female

    def __repr__(self):
        return f"Animal: {self.animal_name} Sound: {self.animal_sound} Height: {self.animal_height} Weight: {self.animal_weight} Legs: {self.animal_legs} Female: {self.isFemale}"

    def makeNoise(self):
        print(self.animal_sound)

class Dog(Animal):
    def __init__(self, name: str, sound: str, height: float, weight: float, legs: int, female: bool, tailLength: float, huntsSheep: bool):
        super().__init__(name, sound, height, weight, legs, female)
        self.tail_length = tailLength
        self.hunts_sheep = huntsSheep

    def __repr__(self):
        return f"Animal: {self.animal_name} Sound: {self.animal_sound} Height: {self.animal_height} Weight: {self.animal_weight} Legs: {self.animal_legs} Female: {self.isFemale} Tail Length: {self.tail_length} Hunts: {self.tail_length} Hunts Sheep: {self.hunts_sheep}"

    def __add__(self, other):
        name = self.animal_name + other.animal_name
        is_female = [True, False]
        height = random.randint(self.animal_height, other.animal_height)
        weight = random.randint(self.animal_weight, other.animal_weight)
        tail_length = random.randint(self.tail_length, other.tail_length)
        if self.isFemale and not other.isFemale:
            return Dog(name, "Woof", height, weight, 4, is_female[random.randint(0, 1)], tail_length, False)
        else:
            print("Is not compatible")


    def wag_tail(self):
        print(f"The {self.animal_name} wags its {self.tail_length}cm long tail eagerly")


def mate(mother, father, name):
    is_female = [True, False]
    height = random.randint(mother.animal_height, father.animal_height)
    weight = random.randint(mother.animal_weight, father.animal_weight)
    tail_length = random.randint(mother.tail_length, father.tail_length)
    if mother.isFemale and not father.isFemale:
    # if mother.isFemale == True and father.isFemale == False:
        return Dog(name, "Woof", height, weight, 4, is_female[random.randint(0, 1)], tail_length, False)
    else:
        print("Is not compatible")


Cheetah = Animal("Cheetah", "Chirp", 80, 50, 4, False)
print(Cheetah)
Cheetah.makeNoise()

Wolf = Dog("Wolf", "Auuuuuuuuu", 70, 60, 4, False, 40, True)
print(Wolf)
Wolf.makeNoise()
Wolf.wag_tail()

MotherDog = Dog("Mother Dog", "Woof", 40, 30, 4, True, 20, False)
FatherDog = Dog("Father Dog", "Woof", 60, 45, 4, False, 35, False)
print(MotherDog)
print(FatherDog)
BabyDog = mate(MotherDog, FatherDog, "Baby Dog")
print(BabyDog)

Mom = Dog("Susan", "Woof", 40, 30, 4, True, 20, False)
Dad = Dog("Brutus", "Woof", 60, 45, 4, False, 35, False)
Puppy = Mom + Dad
print(Puppy)