import random

def get_player_guess():
    guess = int(input("Enter your guess: "))
    return guess

def check_guess(secret, guess):
    if guess < secret:
        print("Too low!")
        return False
    elif guess > secret:
        print("Too high!")
        return False
    else:
        print("Correct!")
        return True

def play_game():
    secret_number = random.randint(1, 100)
    correct = False
    while not correct:
        guess = get_player_guess()
        correct = check_guess(secret_number, guess)

play_game()
