#affich les diviseurs un nbr n entier positif non nul

con =1
while con:
    n= int (input("donner nbr positive non nul: "))
    if n>0 :
        con =0

list1= []

for i in range(1,n+1):
    if( n%i==0):
        list1.append(i)

print(f"touts les diviseurs de {n} est: {list1}")
