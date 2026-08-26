secret_number = 14

while True:
    guess = int(input("Guess the number: "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try agin.")
        continue
    else:
        print("Correct!")
        break