import random
from images import OPTIONS

def play_game():
    computer = random.randint(0, len(OPTIONS) - 1)
    player = int(input("Rock-Paper-Scissors Choose 1, 2 or 3 correspondingly! ")) - 1
    
    try:
        print(f"You:\n{OPTIONS[player]}\nComputer:\n{OPTIONS[computer]}")
    except IndexError:
        raise Exception("You entered invalid number.")

    result = ""
    if player == computer:
        result = "Draw"
    elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
        result = "Win"
    else:
        result = "Lose"

    return result

if __name__ == "__main__":
    print(play_game())