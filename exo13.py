# A shop charges 0.30 dz for the first ten photocopies, 0.25 dz for the next twenty, and 0.20 dz beyond that.
# Write a program that asks the user for the number of photocopies made and displays the corresponding bill
n = int(input("Enter the number of photocopies made: "))
if n <= 10:
    bill = n * 0.30
elif n <= 30:
    bill = (10 * 0.30) + ((n - 10) * 0.25)
else:
    bill = (10 * 0.30) + (20 * 0.25) + ((n - 30) * 0.20)
print(f"The total bill for {n} photocopies is: {bill} dz")