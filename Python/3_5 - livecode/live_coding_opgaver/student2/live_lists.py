# Øvelse: Grundlæggende operationer med lister i Python
# Format: En studerende læser højt kommentaren, og en anden skriver koden nedenunder.

# Trin 1: Opret en tom liste kaldet 'frugter'
# Den studerende skal skrive en tom liste med navnet 'frugter'
frugter = []

# Trin 2: Tilføj tre frugter til listen: 'æble', 'banan', 'kirsebær'
# Brug .append() metoden til at tilføje hver frugt
frugter.append('æble')
frugter.append('banan')
frugter.append('kirsebær')

# Trin 3: Udskriv hele listen
# Brug print() til at vise indholdet af listen
print(frugter)

# Trin 4: Udskriv den første frugt i listen
# Brug indeks 0 til at hente den første frugt
print(frugter[0])

# Trin 5: Erstat den anden frugt med 'appelsin'
# Brug indeks 1 til at ændre værdien
frugter[1] = 'appelsin'
print(frugter)

# Trin 6: Fjern den sidste frugt fra listen
# Brug .pop() uden argumenter
frugter.pop()
print(frugter)

# Trin 7: Tæl hvor mange elementer der er i listen
# Brug len() funktionen
print(len(frugter))

# Trin 8: Sortér listen alfabetisk
# Brug .sort() metoden
frugter.sort()
print(frugter)

# Trin 9: Tøm hele listen
# Brug .clear() metoden
frugter.clear()
print(frugter)
