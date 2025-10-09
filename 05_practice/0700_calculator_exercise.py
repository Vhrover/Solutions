""" Øvelse: "Calculator"

Som altid, læs hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning i kopien.

-------

Opret et program, der fungerer som en simpel lommeregner. Programmet skal fungere som følger:
    1. Forklar brugeren hvordan man betjener programmet.
    2. Præsenter en menu med følgende muligheder:
        - Addition
        - Subtraktion
        - Multiplikation
        - Division
        - Afslut
    3. Bed brugeren om at vælge en mulighed fra menuen.
    4. Hvis brugeren vælger en aritmetisk operation, bed om to tal.
    5. Udfør den valgte operation og vis resultatet.
    6. Gentag processen, indtil brugeren vælger at afslutte.

-------

Hvis du går i stå, spørg Google, andre elever, en AI eller læreren.

Når dit program er færdigt, skub det til dit GitHub-repository.
"""


def calculator():
    print("Hey, welcome to the calculator.\nThe calculator will prompt you to input a number. You will then have to input the number corresponding to the operation you want to use.")
    confirmation = input("Do you want to proceed? Y/N ")
    if confirmation_checker(confirmation.lower()):
        num1 = int(input("\nEnter first number: "))
        num2 = int(input("\nEnter second number: "))
        print(f"\nWhat operation would you like to use?\n\n(1) Addition\n(2) Subtraction\n(3) Multiplication\n(4) Division\n(0) Cancel\n")
        operation = input("Input: ")
        if operation == "1":
            print(num1 + num2)
        elif operation == "2":
            print(num1 - num2)
        elif operation == "3":
            print(num1 * num2)
        elif operation == "4":
            print(num1 / num2)
        elif operation == "0":
            print("\nGoodbye!")
        else:
            print("\nInvalid input.")


def confirmation_checker(confirmation):
    if confirmation == 'y':
        return True
    elif confirmation == 'n':
        return False
    else:
        print("Not a valid input.")


calculator()
