secret = 25

guess = int(input("Guess the secret number (between 1 and 30): "))

if guess == secret:
    print("You've guessed correctly - It's the number " + str(secret))
else:
    print("Sorry, your guess is not correct. It's not the number " + str(guess))
