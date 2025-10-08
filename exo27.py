import random as rd

n = rd.randint(1,30)
nbrTentatives = 5
while nbrTentatives > 0:
    nbrTentatives -= 1
    var = int(input("Entrez un nombre : "))
    if var == n:
        print("c'est plus")
        
    elif var > n:
        print("c'est moins")

    else:
        break
        
if nbrTentatives != 0:
    print(f"Bravo, vous avez trouve {var} en {5-nbrTentatives} essais !")
else:
    print("Dommage, vous avez perdu ! Le nombre était", n)