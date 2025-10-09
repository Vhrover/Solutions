"""Opgave "Number pyramid"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

--------

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Se de første 93 sekunder af denne video: https://www.youtube.com/watch?v=NsjsLwYRW8o

Del 2:
    Skriv en funktion "pyramid", der producerer de tal, der er vist i videoen.
    Funktionen har en parameter "lines", der definerer, hvor mange talrækker der skal produceres.
    Funktionen udskriver tallene i hver række og også deres sum.

Del 3:
    I hovedprogrammet kalder du funktionen med fx 7 som argument.

Del 4:
    Tilføj en mere generel funktion pyramid2.
    Denne funktion har som andet parameter "firstline" en liste med pyramidens øverste rækkens tallene.

Del 5:
    I hovedprogrammet kalder du pyramid2 med fx 10 som det første argument
    og en liste med tal efter eget valg som andet argument.
    Afprøv forskellige lister som andet argument.

Hvis du ikke aner, hvordan du skal begynde, kan du åbne 0812_pyramid_help.py og starte derfra

--------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""


def pyramid(lines):
    numbers = [1, 1]
    temp_numbers = []
    value = 0
    for l in range(1, lines+1):
        if l > 1:
            for n in numbers:
                temp_numbers.append(n)
            for x in range(len(numbers)):
                if x > 0:
                    if numbers[x] + numbers[x-1] == l:
                        temp_numbers.insert(x+value, l)
                        value += 1
            numbers.clear()
            for i in temp_numbers:
                    numbers.append(i)
            temp_numbers.clear()
            value = 0
        print(numbers)

def pyramid2(lines, firstline):
    if isinstance(firstline, list):
        numbers = firstline
        temp_numbers = []
        value = 0
        for l in range(1, lines + 1):
            if l > 1:
                for n in numbers:
                    temp_numbers.append(n)
                for x in range(len(numbers)):
                    if x > 0:
                        if numbers[x] + numbers[x - 1] == l:
                            temp_numbers.insert(x + value, l)
                            value += 1
                numbers.clear()
                for i in temp_numbers:
                    numbers.append(i)
                temp_numbers.clear()
                value = 0
            print(numbers)
    else:
        print("This is not a valid first line!")


# pyramid(7)
pyramid2(7, [2, 2, 1, 1])