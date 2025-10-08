#Write a program that calculates and displays the product: n!
con=1
while con:
    n = int(input("Enter a starting number positive: "))
    if n>=0:
        con = 0
p=1
if n>1:
    for i in range(1,n+1):
        p *= i

print("The product is:", p)