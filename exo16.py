#Write a program that asks for a starting number, then displays the next ten numbers using a for loop.
#For example, if the user enters the number 33, the program will display the numbers from 34 to 43

n = int(input("Enter a starting number: "))
for i in range(n+1, n+11):
    print(i)
