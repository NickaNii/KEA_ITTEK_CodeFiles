# Øvelse: Arbejde kontrol-strukturer i Python
# Format: En studerende læser højt kommentaren, og en anden skriver koden nedenunder.

# lav et random tal mellem 0 og 10
from random import randint
tal = randint(1, 10)
# brug beslutningslogik til at teste om tallet er større eller mindre end 5
# hvis tallet er større end 5 så print "tallet er større end 5"
# hvis tallet er mindre end 5 men over 0 så print "tallet er mindre end 5"
# hvis tallet er 0 så print "tallet er 0"
if tal > 5:
    print("tallet er større end 5")
elif tal < 5 and tal != 0:
    print("tallet er mindre end 5")
else:
    print("tallet er 0")


# tjek nu om tallet er over 0, og hvis det er så 
# lad en bruger inputte et gæt på tallet
# hvis der gættes rigtigt så print "Du gættede rigtigt!" og så vis tallet
# hvis der gættes forkert så print "Du gættede forkert, prøv igen"
# sørg for at brugeren maks kan gætte 3 gange og vis hvor mange gæt der er tilbage
# hvis brugeren løber tør for gæt skal programmet stoppe og give besked om dette
print("Du har nu 3 gæt")
gaet_tilbage = 3
if tal > 0:
    while True:
        if gaet_tilbage > 0:
            gaet = int(input("Indput dit gæt\n>"))
            if gaet == tal:
                print(f"Du gættede rigtigt!, tallet var: {tal}")
                break
            else:
                print("Du gættede forkert, prøv igen")
                gaet_tilbage -= 1 
                print(f"Du har nu {gaet_tilbage} gæt tilbage!")
        else:
            print("Du er løbet tør for gæt!")
            break
        # tilføj nu logik der tester