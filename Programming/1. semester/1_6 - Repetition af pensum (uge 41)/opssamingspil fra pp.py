import random

hemmeligt_nummer = random.randint(1,10)

def faa_input_fra_bruger():
    input_str = input('Tast dit gæt: ')
    return int(input_str)

bruger_gaet = []
resultat = {}
for i in range(10):
    mit_gaet = faa_input_fra_bruger()
    
    if hemmeligt_nummer == mit_gaet:
        print('Du gættede rigtigt')
        resultat[i] = 'Rigtigt'
        break
    else:
        print('Du gættede forkert')
        bruger_gaet.append(mit_gaet)
        resultat[i] = 'Forkert'

print('Her er dine gæt:')
print(bruger_gaet)
print('Resultatet:')
print(resultat)