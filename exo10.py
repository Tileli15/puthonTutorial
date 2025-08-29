# Program that calculates the resistance in series and in parallel
r1 = float(input("Enter the value of the first resistance (in ohms): "))
r2 = float(input("Enter the value of the second resistance (in ohms): "))
r3 = float(input("Enter the value of the third resistance (in ohms): "))
r_series = r1 + r2 + r3
r_parallel = 1 / (1/r1 + 1/r2 + 1/r3)
print(f"The total resistance in series is: {r_series} ohms")
print(f"The total resistance in parallel is: {r_parallel} ohms")