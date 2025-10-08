# nbr premier et non premier

n = int (input("donner un nombre: "))
isPremier = 1
for i in range(2,int(n/2)):
    if(n%i == 0):
        isPremier = 0
        break

if (isPremier == 1):
    print(f"{n} is premier.")
else:
    print(f"{n} is not premier.")