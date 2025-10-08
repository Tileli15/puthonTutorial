#Write a program that asks for a starting number, then displays the next ten numbers using a while loop.
#For example, if the user enters the number 33, the program will display the numbers from 34 to 43

n = int(input("Enter a starting number: "))
count = 0
while count < 10:
    n += 1
    print(n)
    count += 1
