


n = int (input("donner nombre d'equipes: "))
for i in range (1, n+1): 
    for j in range (1, n+1):
        if i != j:
            print (f"equipe {i} VS equipe {j}")