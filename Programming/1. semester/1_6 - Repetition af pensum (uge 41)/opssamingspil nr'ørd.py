import random
hemmeligt_nummer = random.randint(1, 10)

for i in range(10):
    mit_gaet = input("Gæt et tal (mellem 1 - 10): ")

    print("du gættede:", mit_gaet)
    print("det rigtige svar var altså", hemmeligt_nummer)

    if hemmeligt_nummer == mit_gaet:
        print("Du stadigvæk cringe men du vandt altsåååå")
        break
    else:
        print("du cringe og har tabt")
