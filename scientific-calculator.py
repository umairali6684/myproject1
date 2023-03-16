import math

# Define the main function, here we use math function for trying calculation 
def calculator():
    print("Welcome to the Scientific Calculator!")
    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiation")
    print("6. Square root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Logarithm")
    print("11. Quit")

    # Read the user's choice
    choice = int(input("Enter choice: "))

    # Perform the selected operation
    if choice == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "+", num2, "=", num1 + num2)
    elif choice == 2:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "-", num2, "=", num1 - num2)
    elif choice == 3:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "*", num2, "=", num1 * num2)
    elif choice == 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "/", num2, "=", num1 / num2)
    elif choice == 5:
        num1 = float(input("Enter base: "))
        num2 = float(input("Enter exponent: "))
        print(num1, "^", num2, "=", num1 ** num2)
    elif choice == 6:
        num = float(input("Enter a number: "))
        print("Square root of", num, "=", math.sqrt(num))
    elif choice == 7:
        angle = float(input("Enter angle in degrees: "))
        print("Sine of", angle, "degrees =", math.sin(math.radians(angle)))
    elif choice == 8:
        angle = float(input("Enter angle in degrees: "))
        print("Cosine of", angle, "degrees =", math.cos(math.radians(angle)))
    elif choice == 9:
        angle = float(input("Enter angle in degrees: "))
        print("Tangent of", angle, "degrees =", math.tan(math.radians(angle)))
    elif choice == 10:
        num = float(input("Enter a number: "))
        print("Natural logarithm of", num, "=", math.log(num))
    elif choice == 11:
        print("Goodbye!")
        return
    else:
        print("Invalid input, please try again.")
       
    # Ask the user if they want to perform another operation
    again = input("Do you want to perform another operation? (Y/N)").lower()
    if again == "y":
        calculator()
    else:
        print("Goodbye!")
        return

# Call the main function
calculator()
