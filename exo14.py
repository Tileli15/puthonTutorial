# Write a program that asks the user for the age of a child.
# Then, it tells them their category:
# "Poussin" from 6 to 7 years old,
#"Pupille" from 8 to 9 years old,
#"Minime" from 10 to 11 years old,
#"Cadet" after 12 years old

age = int(input("Enter the age of the child: "))
if 6 <= age <= 7:
    category = "Poussin"
elif 8 <= age <= 9:
    category = "Pupille"
elif 10 <= age <= 11:
    category = "Minime"
elif age >= 12:
    category = "Cadet"
else:
    category = "Too young for a category"


print("The category of the child is:", category)