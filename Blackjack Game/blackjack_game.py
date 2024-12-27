import random

def deal_card():
    '''Deal a card'''

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    '''Compute score'''

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_scores(computer_score, player_score):
    '''Compare final result'''

    if computer_score == 0 and player_score == 0:
        print(f"Computer has Blackjack\nYou lose")
    elif player_score == 0:
        print(f"You have Blackjack\nYou win")
    elif player_score > 21:
        print(f"Your score is over 21\nYou lose")
    elif player_score < 22 and computer_score > 21:
        print("You win")
    elif player_score > computer_score:
        print("You win")
    elif player_score == computer_score:
        print("Draw")
    else:
        print("You lose")

def play_regular_game():
    player_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            print(f"Your cards: {player_cards}, current score: {sum(player_cards)}\nComputer's first card: {computer_cards[0]}")
            choice = input("Type 'y' to get another card, type 'n' to pass: ")

            if choice == 'y':
                player_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        
    print(f"Player score: {player_score} - {player_cards}")
    print(f"Player score: {computer_score} - {computer_cards}")
    compare_scores(computer_score, player_score)

if __name__ == "__main__":
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") != 'n':
        play_regular_game()