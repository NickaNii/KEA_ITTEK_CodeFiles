# Øvelse: Arbejde med funktioner i Python
# Format: En studerende læser højt kommentaren, og en anden skriver koden nedenunder.

# opret en funktion der printer dit navn, og som ikke tager nogle parametrer.
def print_name():
    print("Kevin")

# lav et funktionskald og kontrollér at navnet printes
print_name()

# omkskriv funktionen så den tager navnet som parameter og returnere navnet
def print_name(name):
    return name

# lav nu et funktionskald og print et andet navn
print(print_name("Lars"))


# lav en funktion med standardværdier i parametre
# funktionen skal tage højde og længde og returnere arealet af en firkant

def square_area(height = 10, length = 10):
    return height * length

# lav en funktion der tager et arbitrært antal parametre med tal og returnerer summen af dem
def numbers_sum(*numbers):
    return sum(numbers)

print(numbers_sum(10, 30 , 30))