# Program that swaps the contents of two variables based on a condition
x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
if x > y:
    x, y = y, x
    
print("The value of x is:", x)
print("The value of y is:", y)