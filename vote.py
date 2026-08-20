def eligibility():
    while True:
        age_input = input("Enter your age: ")
        try:
            value = int(age_input)
        except ValueError:
            print("Please enter a valid age.")
        if value < 0:
            print("Please enter a valid age.")
        if value < 18 or value > 65:
            print("You are not eligible to vote!")
        else:
            print("You are eligible to vote.")
        return age_input
eligibility()