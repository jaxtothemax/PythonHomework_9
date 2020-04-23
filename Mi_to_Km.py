typeOfConversion_input = input(
    "Enter 1 to convert Mi --> Km or enter anything else to convert Km --> Mi: ")

user_input_number = int(input("Enter a number you want to convert: "))


def conversion_function(typeOfConversion_input, user_input_number):
    if typeOfConversion_input == "1":
        print(f"{user_input_number} miles is {user_input_number / 0.621} kilometers.")
    else:
        print(f"{user_input_number} kilometers is {user_input_number * 0.621} miles.")


conversion_function(typeOfConversion_input, user_input_number)
