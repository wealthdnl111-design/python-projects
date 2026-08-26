while True:
    number_input = input("Enter a positive even number: ")
    try:
        number = int(number_input)
    except ValueError:
        print(f"{number_input} invalid. Please enter a number.")
        continue

    if number % 2 == 0 and number > 0:
        print(f"Yes! {number} is a positive even number")
    else:
        print(f"{number} is not a positive even number. Try again.")