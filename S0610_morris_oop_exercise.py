"""
Opgave "Morris The Miner" (denne gang objekt orienteret)

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Genbrug din oprindelige Morris-kode og omskriv den til en objektorienteret version.

Definer en klasse Miner med attributter som sleepiness, thirst osv.
og metoder som sleep, drink osv.
Opret Morris og initialiser hans attributter ved at kalde konstruktoren for Miner:
stats = Miner()

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

class Morris:

    # def __init__(self, turn=0, sleepiness=0, thirst=0, hunger=0, whiskey=0, gold=0):
    #     self.turn = turn
    #     self.sleepiness = sleepiness
    #     self.thirst = thirst
    #     self.hunger = hunger
    #     self.whiskey = whiskey
    #     self.gold = gold

    def __init__(self):
        self.stats = {"turn": 0, "sleepiness": 0, "thirst": 0, "hunger": 0, "whisky": 0, "gold": 0}

    def sleep(self):
        self.stats["sleepiness"] -= 10
        self.stats["thirst"] += 0
        self.stats["hunger"] += 1
        self.stats["whisky"] += 0
        self.stats["gold"] += 0

    def mine(self):
        self.stats["sleepiness"] += 5
        self.stats["thirst"] += 5
        self.stats["hunger"] += 5
        self.stats["whisky"] += 0
        self.stats["gold"] += 5

    def eat(self):
        self.stats["sleepiness"] += 5
        self.stats["thirst"] -= 5
        self.stats["hunger"] -= 20
        self.stats["whisky"] += 0
        self.stats["gold"] -= 2

    def buy_whisky(self):
        self.stats["sleepiness"] += 5
        self.stats["thirst"] += 1
        self.stats["hunger"] += 1
        self.stats["whisky"] += +1
        self.stats["gold"] -= 1

    def drink(self):
        self.stats["sleepiness"] += 5
        self.stats["thirst"] -= 15
        self.stats["hunger"] -= 1
        self.stats["whisky"] -= 1
        self.stats["gold"] += 0

    def is_dead(self):
        return self.stats["sleepiness"] > 100 or self.stats["thirst"] > 100 or self.stats["hunger"] > 100

morris = Morris()

while not morris.is_dead() and morris.stats["turn"] < 1000:
    morris.stats["turn"] += 1
    if morris.stats["sleepiness"] >= 10:
        morris.sleep()
    elif morris.stats["thirst"] >= 15:
        if morris.stats["whisky"] == 0:
            morris.buy_whisky()
        else:
            morris.drink()
    elif morris.stats["hunger"] >= 20:
        morris.eat()
    else:
        morris.mine()
    print(morris.stats)

if morris.is_dead() == True:
    print("Morris is dead")

