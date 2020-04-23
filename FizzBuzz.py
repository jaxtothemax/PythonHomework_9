user_number = int(input("Enter a number from 1 to 100: "))

for i in range(user_number + 1):
    if i == 0:
        print(i)
    elif (i % 3 == 0) and (i % 5 == 0):
        print("fizzubzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
