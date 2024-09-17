print("Welcome to the Basic Calculator!")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Select operation:")
print("+","-","*","/")

# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."


choice = input("Enter choice (+,-,*,/): ")

if choice in ['+', '-', '*', '/']:


    if choice == '+':
        print(f"{num1} + {num2} = {add(num1, num2)}")

    elif choice == '-':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")

    elif choice == '*':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")

    elif choice == '/':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")

else:
    print("Invalid input! Please select a valid operation.")


