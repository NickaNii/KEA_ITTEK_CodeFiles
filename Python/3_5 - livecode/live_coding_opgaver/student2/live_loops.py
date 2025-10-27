# Øvelse: Arbejde med loops i Python
# Format: En studerende læser højt kommentaren, og en anden skriver koden nedenunder.


# lav et loop der printer et tilfældigt tal mellem 1 og 100
# tallene skal printes indtil at tallet 55 forekommer hvorefter loopet skal stoppes
from random import randint

while True:
    tal = randint(1, 100)
    print(tal)
    if tal == 55:
        print("Loopet slutter da tallet er 55")
        break

# lav et loop der fylder en liste op med 30 random tal mellem 97 og 122
random_numbers = []
for number in range(30):
    random_numbers.append(randint(97, 122))

# print nu listens indhold
print(random_numbers)
# lav nu et loop som 