import re
import regex

"""
skriv tests til hver funktion i regex.py filen herinde
kør testen efterfølgende og kontroller at den fuldføres

skriv gerne flere forskellige assert til hver funktion for at 
finde "edge cases".
"""

# eksempel på løsning til den første funktion:
def test_validate_firstletter_capital():
    assert regex.validate_firstletter_capital("name") == False
    assert regex.validate_firstletter_capital("Name") == True


