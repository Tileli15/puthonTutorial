#Write a program that calculates and displays the sum:
# s= 1 + 10 + 100 + ... + 10^n

n = int(input("Enter a starting number: "))
s=0
for i in range(n+1):
    s += 10**i

print("The sum is:", s)