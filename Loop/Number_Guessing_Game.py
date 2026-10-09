print("Welcome to the Number Guessing Game!")
secret_number = int(input("Choose a number between 1 and 10 for the other player to guess: "))
max_attempts = 3
attempts = 0

print("Now the other player has to guess the number.")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print(f"Correct! {secret_number} was the right number.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
   
    elif guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
    else:
            print("Too high! Try again.")
else:
    print(f"Sorry! You ran out of attempts. The number was {secret_number}.")
