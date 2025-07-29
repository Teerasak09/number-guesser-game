import random

print("🎮 Welcome to the Number Guessing Game!")
secret = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret:
    print("🎉 Correct! You win!")
else:
    print(f"❌ Sorry, the number was {secret}. Better luck next time!")
def get_player_guess():
    guess = int(input("Enter your guess: "))
    return guess
