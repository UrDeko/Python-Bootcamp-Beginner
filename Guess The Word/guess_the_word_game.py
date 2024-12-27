import os
import random
from words import word_list

chosen_word = random.choice(word_list)
display = ["_"] * len(chosen_word)
tryouts = 5
end_of_game = False


while not end_of_game:
    print(' '.join(display))
    guess = input("Guess a letter: ").lower()
    os.system("clear")

    if guess in display:
        print(f"You have already guessed letter '{guess}'")
        continue

    if guess in chosen_word:
        for idx, letter in enumerate(chosen_word):
            if letter == guess:
                display[idx] = guess
    else:
        tryouts -= 1
        print(f"Wrong letter! Tryouts: {tryouts}")

    if tryouts == 0:
        print("NOK")
        end_of_game = True
    if "_" not in display:
        print(' '.join(display))
        print("WIN")
        end_of_game = True