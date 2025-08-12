import random
secret_number = random.randint(1, 10)
guess = int(input("""
                  Let's play a game!
                  I have generated a secret number between 1 and 10.
                  Your task is to guess the number.
                  Guess a number between 1 and 10: """))
match guess:
    case n if 1 <= n <= 10:
        if guess == secret_number:
            print("Congratulations! You guessed the right number!")
        elif guess > secret_number:
            print(f"""
                  Too high! Try again.
                  The secret number was {secret_number}.
                  """)
        elif guess < secret_number:
            print(f"""
                  Too low! Try again.
                  The secret number was {secret_number}.
                  """)
    case _:
        print("Invalid input. Please enter a number between 1 and 10.") 
