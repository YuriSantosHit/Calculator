def sum(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def calculate():
    choice = input("Select operation( + - * / ): ")

    if choice in ('+', '-', '*', '/'):
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")

        if choice == '+':
            print(num1, "+", num2, "=", sum(num1, num2))

        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '/':
            print(num1, "/", num2, "=", divide(num1, num2))

    again()


def again():
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == 'y':
        calculate()
    elif next_calculation == 'n':
        print("Bye Bye")
    else:
        again()


def welcome():
    print('''
Welcome to Calculator
''')


...

welcome()
calculate()
