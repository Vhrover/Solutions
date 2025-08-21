"""opgave: Objektorienteret rollespil, afsnit 2 :

Som altid skal du læse hele øvelsesbeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Byg videre på din løsning af afsnit 1.

Del 1:
    Opfind to nye klasser, som arver fra klassen Character. For eksempel Hunter og Magician.
    Dine nye klasser skal have deres egne ekstra metoder og/eller attributter.
    Måske overskriver de også metoder eller attributter fra klassen Character.

Del 2:
    Lad i hovedprogrammet objekter af dine nye klasser (dvs. rollespilfigurer) kæmpe mod hinanden,
    indtil den ene figur er død. Udskriv, hvad der sker under kampen.

I hver omgang bruger en figur en af sine evner (metoder). Derefter er det den anden figurs tur.
Det er op til dig, hvordan dit program i hver tur beslutter, hvilken evne der skal bruges.
Beslutningen kan f.eks. være baseret på tilfældighed eller på en smart strategi

Del 3:
    Hver gang en figur bruger en af sine evner, skal du tilføje noget tilfældighed til den anvendte evne.

Del 4:
    Lad dine figurer kæmpe mod hinanden 100 gange.
    Hold styr på resultaterne.
    Prøv at afbalancere dine figurers evner på en sådan måde, at hver figur vinder ca. halvdelen af kampene.

Hvis du går i stå, kan du spørge google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-besked til din lærer: <filename> done
Fortsæt derefter med den næste fil."""

import random


class Character():
    def __init__(self, name, max_health=100, attackpower=10,):
        self.name = name
        self.max_health = max_health
        self.attackpower = attackpower
        self._current_health = max_health
        self.dot_time = 0
        self.current_afflictions = []
        self.dot_damage = 0

    def __repr__(self):
        return f"Character Name: {self.name} Class: (Insert Class here), Stats: {self.attackpower} ATK {self.max_health} HP Current HP: {self._current_health}"


    def current_health(self):
        return self._current_health

    def hit(self, other):
        other.get_hit(self.attackpower)


    def get_hit(self, damage_amount, iscrit):
        if self._current_health > 0:
            self._current_health -= damage_amount

    def full_health(self):
        self._current_health = self.max_health


    def get_healed(self, heal_amount):
        if self._current_health < self.max_health:
            self._current_health += heal_amount

    def get_dot(self, other,  duration, damage, dot_type):
        if not self.current_afflictions:
            self.dot_time = duration
            self.current_afflictions.append(dot_type)
            self.dot_damage = damage

    def remove_dot(self):
        self.dot_time = 0
        if self.current_afflictions:
            del self.current_afflictions[0]

    def dot_checker(self):
        if self.dot_time > 0:

            self.dot_proc(self.dot_damage)

            # print(f"{self.name}'s {self.current_afflictions[0]} damaged {self.dot_damage}")

            if self.dot_time == 1:
                self.remove_dot()

            self.dot_time -= 1

            # print(self.current_afflictions)

    def dot_proc(self, damage):
        self.get_hit(damage, False)

    def enter_combat(self, other):
        turns = 0
        fighter1 = self
        fighter2 = other
        while self.current_health() > 0 and other.current_health() > 0:
            turns += 1
            fighter1.dot_checker()
            if fighter2.current_health() < 1 or fighter1.current_health() < 1:
                return fighter1.winchecker(fighter2)
            fighter2.dot_checker()
            # fighter1.dot_checker()
            # fighter2.dot_checker()
            # if self.dot_time > 0:
            #
            #     self.dot_proc(self.dot_damage)
            #
            #     print(f"{self.name}'s {self.current_afflictions[0]} damaged {self.dot_damage}")
            #
            #     if self.dot_time == 1:
            #         del self.current_afflictions[0]
            #
            #     self.dot_time -= 1
            #
            #     print(self.current_afflictions)
            #
            # elif other.dot_time > 0:
            #
            #     other.dot_proc(other.dot_damage)
            #
            #     print(f"{other.name}'s {other.current_afflictions[0]} damaged {other.dot_damage}")
            #
            #     if other.dot_time == 1:
            #         del other.current_afflictions[0]
            #
            #     other.dot_time -= 1
            #
            #     print(other.current_afflictions)

            # elif self.dot_time == 1:
            #     self.dot_time -= 1
            #     del self.current_afflictions[0]
            #     print(self.current_afflictions)
            #
            # elif self.dot_time == 1:
            #     self.dot_time -= 1
            #     del self.current_afflictions[0]
            #     print(self.current_afflictions)

            # fighter1.fireball(fighter2)
            # fighter2.bleed_test(fighter1)
            fighter1.use_ability(fighter2)
            if fighter2.current_health() < 1 or fighter1.current_health() < 1:
                return fighter1.winchecker(fighter2)
            fighter2.use_ability(fighter1)

            # print(f"Turn: {turns} {fighter1.name} {fighter1._current_health}/{fighter1.max_health} {fighter2.name} {fighter2._current_health}/{fighter2.max_health}")

        fighter1.remove_dot()
        fighter2.remove_dot()

        return fighter1.winchecker(fighter2)

        # if self.current_afflictions:
        #     del self.current_afflictions[0]
        # elif other.current_afflictions:
        #     del other.current_afflictions[0]

    def winchecker(self, other):
        if self.current_health() > 0 and other.current_health() <= 0:
            return self
        elif other.current_health() > 0 and self.current_health() <= 0:
            return other


class Healer(Character):
    def __init__(self, name, max_health, healpower=10):
        super().__init__(name, max_health, 0)
        self.healpower = healpower


    def heal(self, other):
        other.get_healed(self.healpower)

class Mage(Character):
    def __init__(self, name, max_health, magicpower=10, mana=100):
        super().__init__(name, max_health, 0)
        self.magicpower = magicpower
        self.mana = mana
        self.abilitylist = [self.fireball]

    def fireball(self, other):
        potency = 1.5
        accuracy = 80
        accuracy_roll = random.randint(1, 100)
        dot_roll = random.randint(1, 100)
        self.mana -= 10
        if accuracy_roll > accuracy:
            # print("Miss!")
            return
        elif dot_roll >= 20:
            other.get_dot(self, 2, 15, "Burn")
        elif accuracy_roll <= accuracy:
            other.get_hit(self.magicpower * potency, False)
    def use_ability(self, other):
        random_number = random.randint(0, len(self.abilitylist)-1)
        self.abilitylist[random_number](other)

class Rogue(Character):
    def __init__(self, name, max_health, crit_chance=25, crit_bonus=4):
        super().__init__(name, max_health, 8)
        self.crit_chance = crit_chance
        self.crit_bonus = crit_bonus
        self.abilitylist = [self.stab, self.bleed_test]

    def stab(self, other):
        crit_roll = random.randint(1,100)
        if crit_roll <= self.crit_chance:
            iscrit = True
            other.get_hit(self.attackpower * self.crit_bonus, iscrit)
            # print("Critical Hit!")
        else:
            iscrit = False
            other.get_hit(self.attackpower, iscrit)

    def bleed_test(self, other):
        other.get_dot(self, 3, 10, "Bleed")

    def use_ability(self, other):
        # random_number = random.randint(0, len(self.abilitylist)-1)
        # self.abilitylist[random_number](other)
        if not other.current_afflictions:
            self.bleed_test(other)
        else:
            random_number = random.randint(0, len(self.abilitylist)-1)
            self.abilitylist[random_number](other)

def simulate_fights(fighter1, fighter2, rounds):
    fighter1_wins = 0
    fighter2_wins = 0
    for x in range(rounds):
        fighter1.full_health()
        fighter2.full_health()
        fighter1.enter_combat(fighter2)
        print(f"[{fighter1.winchecker(fighter2)}")
        # if fighter1.winchecker(fighter1) == fighter1:
        #     fighter1_wins += 1
        # elif fighter1.winchecker(fighter2) == fighter2:
        #     fighter2_wins += 1
        if fighter1.enter_combat(fighter2) == fighter1:
            fighter1_wins += 1
        elif fighter1.enter_combat(fighter2) == fighter2:
            fighter2_wins += 1
    print(f"{fighter1.name} won {fighter1_wins}/{rounds}, {fighter2.name} won {fighter2_wins}/{rounds}")

# def fight(fighter1, fighter2):
#     turn = 0
#     while fighter1._current_health > 0 and fighter2._current_health > 0:
#         turn += 1
#         fighter1.fireball(fighter2)
#         fighter2.stab(fighter1)
#         print(f"Turn: {turn} {fighter1.name} {fighter1._current_health}/{fighter1.max_health} {fighter2.name} {fighter2._current_health}/{fighter2.max_health}")
#
#
harris = Mage("Harris", 100)
morris = Rogue("Morris", 100)

simulate_fights(harris, morris, 100)
# harris.enter_combat(morris)
# print(harris.current_afflictions, "after combat test")
# print(morris.current_afflictions, "after combat test")
# fight(harris, morris)

# def game_over(isover):
#     print("Game Over")
#     return isover
#
# def fight():
#     fighter1 = Mage("Mage", 100)
#     fighter2 = Rogue("Rogue", 100)
#     while not game_over():

# dummy = Character("Target Dummy", 100, 0)
# rogue = Rogue("Rogue", 100)
# rogue.stab(dummy)
# print(dummy._current_health)
