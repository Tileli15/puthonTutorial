# Write a program that displays the solution of a quadratic equation of the form ax²+bx+c
import math

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    print(f"The equation has two distinct real roots: x1 = {x1} and x2 = {x2}")
elif delta == 0:
    x = -b / (2*a)
    print(f"The equation has one real root: x = {x}")
else:
    print("The equation has no real roots.")