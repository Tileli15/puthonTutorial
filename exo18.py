#Write a program that calculates and displays the sum:
# s= 1+ 1/2 + 1/3 + ... + 1/n

n = int(input("Enter a starting number: "))

s=0
for i in range(1,n+1):
    s += 1/i


print("la somme est: ",s)