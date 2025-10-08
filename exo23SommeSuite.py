# la somme d'une suite
# Un+1 = 4*Un + 10  and U0=6

con=1
while con:
    n= int ( input("entrer nbr positive: "))
    if n>=0:
        con=0

U0=6
if n !=0:
    for i in range(1,n+1):
         Un = 4* U0 + 10
         U0 = Un

print(f"U{n} = {U0}")