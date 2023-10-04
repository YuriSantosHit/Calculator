def celsius_to_fahreinheit(x):
    y = (x * 9/5) + 32
    return y


def celsius_to_kelvin(x):
    y = x + 273.15
    return y


def fahrenheit_to_celsius(x):
    x = (32 * x - 32) * 5/9
    return x


def fahrenheit_to_kelvin(x):
    y = (32 * x - 32) * 5/9 + 273.15
    return y


def kelvin_to_celsius(x):
    y = x - 273.15
    return y


def kelvin_to_fahreinheit(x):
    y = (x - 273.15) * 9/5 + 32
    return y


def conversion():
    print("Select conversion:")
    print(" 1-) celsius to fahreinheit")
    print(" 2-) celsius to kelvin")
    print(" 3-) fahreinheit to celsius")
    print(" 4-) fahreinheit to kelvin")
    print(" 5-) kelvin to celsius")
    print(" 6-) kelvin to fahreinheit")
    choice = input("What is the option? ")
    if choice in ('1', '2', '3', '4', '5', '6'):
        try:
            num1 = int(input("What is the temperature? "))
        except ValueError:
            print("Invalid input.")

        if choice == '1':
            print(
                f'''{num1} celsius is {celsius_to_fahreinheit(num1)} fahreinheit''')

        elif choice == '2':
            print(
                f'''{num1} celsius is {celsius_to_kelvin(num1)} kelvin''')

        elif choice == '3':
            print(
                f'''{num1} fahreinheit is {fahrenheit_to_celsius(num1)} celsius''')

        elif choice == '4':
            print(
                f'''{num1} fahreinheit is {fahrenheit_to_kelvin(num1)} kelvin''')
        elif choice == '5':
            print(
                f'''{num1} kelvin is {kelvin_to_celsius(num1)} celsius''')
        elif choice == '6':
            print(
                f'''{num1} kelvin is {kelvin_to_fahreinheit(num1)} fahreinheit''')
        again()


def again():
    next_conversion = input("Let's do next conversion? (yes/no)")
    if next_conversion == "yes" or next_conversion == "y":
        conversion()
    elif next_conversion == "no" or next_conversion == "n":
        print("See you!")


conversion()
