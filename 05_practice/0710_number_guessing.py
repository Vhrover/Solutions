""" Opgave "Number guessing"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Opret et program, der spiller et gættespil med brugeren. Programmet fungerer på følgende måde:
    Forklar reglerne for brugeren.
    Generer tilfældigt et 4-cifret heltal.
    Bed brugeren om at gætte et 4-cifret tal.
    Hvert ciffer, som brugeren gætter korrekt i den rigtige position, tæller som en sort mønt.
    Hvert ciffer, som brugeren gætter korrekt, men i den forkerte position, tæller som en hvid mønt.
    Når brugeren har gættet, udskrives det, hvor mange sorte og hvide mønter gættet er værd.
    Lad brugeren gætte, indtil gættet er korrekt.
    Hold styr på antallet af gæt, som brugeren gætter i løbet af spillet, og print det ud til sidst.

--------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

import random


def number_guessing():
    number_list = [random.randint(1, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]
    guess_list = []
    round = 0
    black_coins = 0
    white_coins = 0
    won = False
    print(number_list)
    print("Welcome to number guessing! Do you want to hear the rules? Y/N")
    rules = input()
    if rules.lower() == "y":
        print("The rules are simple. I have generated a random whole number with 4 digits, you will need to guess the number. Please put a blank space in between each digit or this will not work.")
        print("For every correct digit in the correct position I will give you a black coin, and for every correct digit in the wrong position I will give you a white coin.")
        print("Good luck!")
    while not won:
        round += 1
        white_coins = 0
        black_coins = 0
        guess = int(input(f"Guess number {round}:"))
        guess_list = listify(guess)
        for g in guess_list:
            if g in number_list:
                return


def listify(guess):
    temp_list = guess.split()
    final_list = []
    for t in temp_list:
        final_list.append(int(t))
    return final_list

def test():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    for g in range(len(list1)):
        if list1[g] in list2:
            for i in range(len(list2)):
                if list2[g] == list1[g]:
                    print("Right spot!")
                    break
                elif list1[g] == list2[i]:
                    print(f"Wrong spot! Correct spot is {i}")
                    break
        else:
            print(f"{list1[g]} was not in list 2")


test()
# number_guessing()