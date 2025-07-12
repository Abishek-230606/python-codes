# Simple Calculator in Python
import math
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def logarithm(x, base=10):
    return math.log(x, base)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Start loop here
while True:
    print("Select operation:")
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")

    choice = input("Enter choice (1-7): ")

    if choice in ['1', '2', '3', '4', '5', '7']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: ")) if choice != '6' else None

    if choice == '1':
        print(Fore.GREEN + f"Result: {add(num1, num2)}")
    elif choice == '2':
        print(Fore.GREEN + f"Result: {subtract(num1, num2)}")
    elif choice == '3':
        print(Fore.GREEN + f"Result: {multiply(num1, num2)}")
    elif choice == '4':
        print(Fore.GREEN + f"Result: {divide(num1, num2)}")
    elif choice == '5':
        print(Fore.GREEN + f"Result: {power(num1, num2)}")
    elif choice == '6':
        num1 = float(input("Enter number: "))
        if num1 < 0:
            print(Fore.RED + "Error! Cannot calculate square root of a negative number.")
        else:
            print(Fore.GREEN + f"Result: {square_root(num1)}")
    elif choice == '7':
        if num1 <= 0:
            print(Fore.RED + "Error! Logarithm is undefined for non-positive numbers.")
        else:
            base = input("Enter base (default is 10): ")
            base = float(base) if base else 10
            print(Fore.GREEN + f"Result: {logarithm(num1, base)}")
    else:
        print(Fore.RED + "Invalid input!")

    again = input(Style.BRIGHT + "\nDo you want to perform another calculation? (yes/no): ").lower()
    if again != 'yes':
        print(Fore.CYAN + "Thank you for using the calculator! Exiting...")
        break
