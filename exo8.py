a = int (input("Enter the number a : "))
b = int(input("Enter the number b : "))

# échange le contenu des deux variables
# This is a classique operation
# int c = a     a = b      b = c

# This is a simple swap operation
a,b = b,a
print(f"The value of a is now: {a}")
print(f"The value of b is now: {b}")
