import random
import os
from blackjack_game import deal_card, calculate_score, compare_scores

def play_custom_game():
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    while choice == 'y':
        os.system("clear")
        
        player_cards = [deal_card(), deal_card()]
        computer_cards = [deal_card(), deal_card()]

        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        
        while choice != 'n':
            if player_score == 0 or computer_score == 0 or player_score > 21:
                break

            print(f"Your cards: {player_cards}, current score: {sum(player_cards)}\nComputer's first card: {computer_cards[0]}")
            choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if choice == 'y':
                player_cards.append(random.randint(1, 11))
                player_score = calculate_score(player_cards)

        choice = ''
        options = ['n', 'y']

        while choice != 'n':
            if computer_score == 0 or computer_score > 21:
                break

            choice = random.choice(options)
            if choice == 'y':
                computer_cards.append(random.randint(1, 11))
                computer_score = calculate_score(computer_cards)

        print(f"Player score: {player_score} - {player_cards}")
        print(f"Player score: {computer_score} - {computer_cards}")
        compare_scores(computer_score, player_score)

        choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")


if __name__ == "__main__":
    play_custom_game()