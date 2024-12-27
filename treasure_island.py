print("Welcome to Treasure Island\nYour mission is to find the treasure")
action = input("You reached crossroad. Which path do you choose to take - 'left' or 'right'? ")

if action == "left":
    print("Game over")
else:
    action = input("There is a small river in fnront of you. Would you rather 'swim' to the other side of the river or 'wait' until a boat arrives? ")
    
    if action == "swim":
        print("Game over")
    else:
        action = input("You get to a house with three doors - 'red', 'green' and 'blue'. Which one do you choose? ")
        if action == "blue":
            print("Game over")
        elif action == "green":
            print("Game over")
        else:
            print("Congratulations you win the treasure!")