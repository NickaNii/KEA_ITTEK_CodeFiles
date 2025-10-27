# Øvelse: Arbejde med collections i Python
# Format: En studerende læser højt kommentaren, og en anden skriver koden nedenunder.

import random
# opret en list med 4 navne
navne = ["Kevin", "Marco", "Anders", "Alexander"]
# tag et random navn fra listen og gem i en variabel og print dens indhold
random_navn = random.choice(navne)
print(random_navn)
# opret nu en dictionary med samme navne, hvor navnet er key value er en ny dictionary med adresse tilhørende navnet
# adressen finder du bare på

adresser = {
    "Kevin" : {"adresse" : "guldbagersgade 29N"},
    "Marco" : {"adresse" : "Kronegade 14"},
    "Anders" : {"adresse" : "Valbyvej 16"},
    "Alexander" : {"adresse" : "Hellerupvej 12"}
    
}

# prøv nu at anvende variablen med et tilfældigt navn til at printe
# adressen tilhørende navnet fra din dictionary
print(adresser.get(random_navn).get("adresse"))

# lav et loop hvor et random navn printes 10 gange og kør koden
#for i in range(9):
#    print(random.choice(navne))