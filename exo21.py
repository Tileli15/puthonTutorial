#Write a program that calculates and displays the sum:
# s= 1^2 + 3^2 + 5^2 + ....+(r+1)^2 | n fois exomple: n=5 s= 1^2 + 3^2 + 5^2 + 7^2 + 9^2

con =1
while con:
    n= int (input("donner nbr positive: "))
    if n>=0 :
        con =0

s= 0
p=1
while n>0:
    n-=1
    s+= p**2
    p+=2

print("s= ",s)
