def Calculator():
    print("\n===== Welcome to the Calculator! =====")
    while True:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")

        if operator == "+":
            print(num1 + num2)
        elif operator == "-":
            print(num1 - num2)
        elif operator == "*":
            print(num1 * num2)
        elif operator == "/":
            if num2 != 0:
                print(num1 / num2)
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operator!")

        choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if choice == "yes":
            continue
        elif choice == "no":
            print("Exiting Calculator...")
            print("Thanks for using the Calculator! \nGoodbye.")
            break
        else:
            print("Invalid input\nPlease enter 'yes' or 'no'.")