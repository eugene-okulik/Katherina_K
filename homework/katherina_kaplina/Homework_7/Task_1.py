parameter = 10
while True:
    user_number = int(input("Enter any number to guess the parameter: "))
    if user_number == parameter:
        print("Congratulations! You guessed it!")
        break
    else:
        print("You failed to guess")
