
# Øvelse: Arbejde med tekststrenge og brug af strip()-metoden i Python
# Format: En studerende læser højt kommentaren, og en anden skriver koden nedenunder.

# Trin 1: Opret en streng med navnet 'tekst' som indeholder mellemrum før og efter
# Skriv en streng med indholdet '  Hej med dig  '
tekst = '  Hej med dig  '

# Trin 2: Udskriv strengen som den er
# Brug print() til at vise strengen med mellemrum
print(tekst)

# Trin 3: Brug strip() til at fjerne mellemrum i starten og slutningen
# Brug tekst.strip() og gem resultatet i en ny variabel 'renset_tekst'
renset_tekst = tekst.strip()
print(renset_tekst)

# Trin 4: Udskriv længden af den originale og den rensede streng
# Brug len() til at vise forskellen
print(len(tekst))
print(len(renset_tekst))

# Trin 5: Brug lstrip() til kun at fjerne mellemrum i starten
# Gem resultatet i 'venstre_rens'
venstre_rens = tekst.lstrip()
print(venstre_rens)

# Trin 6: Brug rstrip() til kun at fjerne mellemrum i slutningen
# Gem resultatet i 'højre_rens'
højre_rens = tekst.rstrip()
print(højre_rens)

# Trin 7: Brug strip() til at fjerne specifikke tegn, fx punktummer
# Opret en ny streng 'sætning' med indholdet '...Velkommen...'
sætning = '...Velkommen...'
print(sætning.strip('.'))
