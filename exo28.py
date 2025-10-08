# calculater with menu

while True:
    print("------------calculater : MENU------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Reste d'un division entiere")
    print("6. Puissance")
    choice =int( input("Choose an operation (1-6): "))
    a = int(input("Enter 1er terme: "))
    b = int(input("Enter 2eme terme: "))
    if choice == 1:
        print(f"{a} + {b} = {a + b}")
    elif choice == 2:
        print(f"{a} - {b} = {a - b}")
    elif choice == 3:
        print(f"{a} * {b} = {a * b}")
    elif choice == 4:
        if b != 0:
            print(f"{a} / {b} = {a / b}")
        else:
            print("Error: Division sur zero")
    elif choice == 5:
        if b != 0:
            print(f"{a} % {b} = {a % b}")
        else:
            print("Error: Division sur zero")
    elif choice == 6:
        print(f"{a} ** {b} = {a ** b}")
    else:
        print("Invalid choice. Please choose a number between 1 and 6.")

        cont = input("Veux-tu faire un autre calcul? (yes/no): ")
    if cont.lower() == 'no':
        break
    
