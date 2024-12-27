import random

ATTEMPTS_HARD = 10
ATTEMPTS_EASY = 5

def set_difficulty():
    if input("Choose difficulty level - 'hard' or 'easy': ") == "easy":
        return ATTEMPTS_HARD

    return ATTEMPTS_EASY

def check_result(guess, number, attempts):
    if guess == number:
        print(f"You guessed the number: {guess}")
    elif guess > number:
        print(f"Too high")
        attempts -= 1
    else:
        print(f"Too low")
        attempts -= 1

    return attempts

def number_guessing_game():
    print("Welcome to the number guessing game\nI am thinking of a number between 0 and 100")
    number = random.randint(0, 100)
    attempts = set_difficulty()
    guess = 0

    while guess != number:
        print(f"Attempts: {attempts}")
        guess = int(input("Make a guess: "))
        
        attempts = check_result(guess, number, attempts)  
        if attempts == 0:
            print("You have run out of attempts.")
            return


if __name__ == "__main__":  
    number_guessing_game()