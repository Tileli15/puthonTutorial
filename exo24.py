#Program that calculates and displays the terms of the Fibonacci sequence
# U0 = 0
# U1 = 1
#Un+2 = Un+1 + Un

con=1
while con:
    n= int ( input("entrer nbr positive: "))
    if n>=0:
        con=0
U0 = 0
U1 = 1
if(n>1):
    for i in range(2,n+1):
        Un = U1 + U0
        U1 = Un
        U0 = U1

if (n == 0) :
    print("U0 = ",U0)

elif(n == 1):
    print("U1 = ",U1)

else:
    print(f"U{n} = {Un}")