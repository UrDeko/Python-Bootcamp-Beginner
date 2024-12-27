import random

names = input("Input all the names participating in the game, separated, by a comma: ").split(", ")
pick = random.randint(0, len(names) - 1)

print(f"And the winner is .... {names[pick]}")