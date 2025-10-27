# Øvelse: Arbejde med filhåndtering i Python
# Format: En studerende læser højt kommentaren, og en anden skriver koden nedenunder.


# lav kode der opretter en ny fil og skriver noget brugerinput til den
with open("textfile.txt", "w") as f:
    f.write(input("insert text\n>")+"\n")

# åben filen igen og tilføj 3 nye linjer med brugerinput og behold det første tekst som blev indsat
with open("textfile.txt", "a") as f:
    f.write(input("insert first line\n>")+"\n")
    f.write(input("insert second line\n>")+"\n")
    f.write(input("insert third line\n>")+"\n")

# åben filen igen og læs teksten og gem den i en variabel

with open("textfile.txt", "r") as f:
    text = f.read()
    print(text)
    # omdan alt teksten til upper case
    upper = text.upper()
    # gem teksten i filen og overskriv den gamle tekst med den nye i upper case
    with open("textfile.txt", "w") as file:
        file.write(upper)

# bed om brugerinput med et nyt filnavn og opret en fil med det navn
# Indsæt 1000 linjer med random tal
new_file = input("Input new file name\n>")
from random import randint
with open(new_file, "w") as f:
    for random_number in range(999):
        f.write(str(randint(0, 1000))+"\n")