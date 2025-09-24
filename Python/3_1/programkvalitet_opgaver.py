# 1 - Opgave 1: Funktionalitet og Robusthed
# Lavkvalitetskode:​
def divide(a, b):

    return a / b

# Problem: Ingen håndtering af division med nul eller ikke-numeriske inputs.
# Forbedringsmål:
#   Tilføj typeannoteringer.
#   Håndter exceptions.
#   Gør funktionen mere robust.
def divide_numbers(a: int | float, b: int | float) -> float:
    
    a, b = float(a), float(b)
    
    try: 
        return print("Result = ",a / b) 
    
    except ZeroDivisionError: 
        return float('inf')
    
    except ValueError:
        print("Please enter a number")
        return(divide_numbers())

divide_numbers(input("A: "), input("B: "))


# Opgave 2: Læsbarhed og Dokumentation
# Lavkvalitetskode:
def f(x):
    return x * 3.14 * x

# Problem: Uklart formål, ingen dokumentation, dårligt navn.
# Forbedringsmål:
#   Giv funktionen et beskrivende navn.
#   Tilføj docstring.
#   Brug konventionelle navne og typeannoteringer.

# Opgave 3: Genbrugelighed og Vedligeholdbarhed
# Lavkvalitetskode:
def process_data():
    data = [1, 2, 3, 4]
    result = []
    for i in data:
        result.append(i * 2)
    print(result)

# Problem: Hårdkodet data, ingen parameterisering, print i stedet for return.

# Forbedringsmål:

# Gør funktionen genbrugelig ved at tage input som parameter.
# Returnér resultatet i stedet for at printe.
# Tilføj typeannoteringer og dokumentation.