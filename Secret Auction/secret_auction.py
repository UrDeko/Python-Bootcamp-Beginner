import os
from art import logo
print(logo)
bid_log = {}

def find_highest_bidder(bid_status):
    highest_bid = 0
    winner = ""

    for name, bid in bid_status.items():
        if bid > highest_bid:
            highest_bid = bid
            winner = name

    print(f"The winner is {winner} with a bid of ${highest_bid}.")


while True:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bid_log[name] = price

    if input("Are there any other bidders? Type 'yes' or 'no'.\n").lower() == "no":
        break
    os.system('clear')

find_highest_bidder(bid_log)
