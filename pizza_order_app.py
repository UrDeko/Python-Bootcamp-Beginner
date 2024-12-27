print("Welcome to Python Pizza Deliveries!")
pizza_size = input("What size pizza do you want? S, M or L? ")
add_pepperoni = input("Do you want pepperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")
bill = 0

if pizza_size == 'S':
    bill += 15
elif pizza_size == 'M':
    bill += 20
elif pizza_size == 'L':
    bill += 25

if add_pepperoni == 'Y' and pizza_size == 'S':
    bill += 2
elif add_pepperoni == 'Y' and pizza_size in ('M', 'L'):
    bill += 3

if extra_cheese == 'Y':
    bill += 1
    
print(f"Your final bill is: ${bill}")