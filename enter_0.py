

while True:
    real_number = input("Enter a number: ")
    try:
        number = int(real_number)
    except ValueError:
        print(f"{real_number} invalid.")
    if number != 0:
        print(f"You entered {number}.")
    else:
        print("Program ended.")
        break