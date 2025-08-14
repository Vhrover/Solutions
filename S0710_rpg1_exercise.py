"""Opgave: Objektorienteret rollespil, afsnit 1 :

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Definer en klasse "Character" med attributterne "name", "max_health", "_current_health", "attackpower".
    _current_health skal være en protected attribut, det er ikke meningen at den skal kunne ændres udefra i klassen.

Del 2:
    Tilføj en konstruktor (__init__), der accepterer klassens attributter som parametre.

Del 3:
    Tilføj en metode til udskrivning af klasseobjekter (__repr__).

Del 4:
    Tilføj en metode "hit", som reducerer _current_health af en anden karakter med attackpower.
    Eksempel: _current_health=80 og attackpower=10: et hit reducerer _current_health til 70.
    Metoden hit må ikke ændre den private attribut _current_health i en (potentielt) fremmed klasse.
    Definer derfor en anden metode get_hit, som reducerer _current_health for det objekt, som den tilhører, med attackpower.

Del 5:
    Tilføj en klasse "Healer", som arver fra klassen Character.
    En healer har attackpower=0 men den har en ekstra attribut "healpower".

Del 6:
    Tilføj en metode "heal" til "Healer", som fungerer som "hit" men forbedrer sundheden med healpower.
    For at undgå at "heal" forandrer den protected attribut "_current_health" direkte,
    tilføj en metode get_healed til klassen Character, som fungerer lige som get_hit.

Hvis du er gået i stå, kan du spørge google, de andre elever, en AI eller læreren.
Hvis du ikke aner, hvordan du skal begynde, kan du åbne S0720_rpg1_help.py og starte derfra.

Når dit program er færdigt, skal du skubbe det til dit github-repository
og sammenlign det med lærerens løsning i S0730_rpg1_solution.py

Send derefter denne Teams-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

class Character():
    def __init__(self, name, max_health=100, attackpower=10,):
        self.name = name
        self.max_health = max_health
        self.attackpower = attackpower
        self._current_health = max_health

    def __repr__(self):
        return f"Character Name: {self.name} Class: (Insert Class here), Stats: {self.attackpower} ATK {self.max_health} HP"


    def hit(self, other):
        other.get_hit(self.attackpower)


    def get_hit(self, damage_amount):
        if self._current_health > 0:
            self._current_health -= damage_amount

    def get_healed(self, heal_amount):
        if self._current_health < self.max_health:
            self._current_health += heal_amount



class Healer(Character):
    def __init__(self, name, max_health, healpower=10):
        super().__init__(name, max_health, 0 )
        self.healpower = healpower


    def heal(self, other):
        other.get_healed(self.healpower)


Warrior1 = Character("Warrior1", 100, 10)
Warrior2 = Character("Warrior2", 100, 10)
Healer = Healer("Healer", 100, 10)
Warrior1.hit(Warrior2)
print(Warrior2._current_health)
Healer.heal(Warrior2)
print(Warrior2._current_health)