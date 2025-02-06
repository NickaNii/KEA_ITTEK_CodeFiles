# Øvelse 1_5 - Print et random tal fra en liste

from random import choice

terning = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
y = choice(terning)


# range-blok
'''
x=int(input("range: "))
for i in range(x):
    print(choice(terning))
'''
print(y)

if y ==8:
    print("winner winner")

else:
    print("nuhuh")
        

    
