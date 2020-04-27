typeOfConversion_input = input(
    "Enter 1 to convert Mi --> Km or enter 2 to convert Km --> Mi: ")

user_input_number = int(input("Enter a number you want to convert: "))

FACTOR = 0.621


def conversion_function(typeOfConversion_input, user_input_number):
    if typeOfConversion_input == "1":
        print(f"{user_input_number} miles is {user_input_number / FACTOR} kilometers.")
    elif typeOfConversion_input == "2":
        print(f"{user_input_number} kilometers is {user_input_number * FACTOR} miles.")
    else:
        print("Command not recognised.")


conversion_function(typeOfConversion_input, user_input_number)
