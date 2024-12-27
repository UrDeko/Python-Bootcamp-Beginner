#!/usr/bin/env python3
import os
import random

from art import logo, vs
from game_data import data

def format_output(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']

    return f"{account_name}, {account_description}, {account_country}"

def check_result(guess, account_a, account_b):
    followers_a = account_a["follower_count"]
    followers_b = account_b["follower_count"]

    if followers_a > followers_b:
        return guess == 'a'
    if followers_a < followers_b:
        return guess == 'b'
    
def start_game():
    print(logo)

    score = 0
    is_game_over = False
    account_b = random.choice(data)

    while not is_game_over:
        account_a = account_b
        account_b = random.choice(data)

        while account_b == account_a:
            account_b = random.choice(data)

        print(f"Compare A: {format_output(account_a)}.")
        print(vs)
        print(f"Against B: {format_output(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        result = check_result(guess, account_a, account_b)
        os.system("clear")
        print(logo)

        if result:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            is_game_over = True
            print(f"You're wrong! Final score: {score}.")


if __name__ == "__main__":
    start_game()