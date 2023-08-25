import random

def is_valid_card(card):
    valid_values = ['1', '2', '3', '4', '5', '6', '7', 'F', 'C', 'R']
    valid_seeds = ['B', 'S', 'C', 'D']
    if len(card) != 2:
        return False
    value, seed = card[0].upper(), card[1].upper()
    return value in valid_values and seed in valid_seeds


def get_winner(player1_card, player2_card, briscola):
    value1, seed1 = player1_card[0].upper(), player1_card[1].upper()
    value2, seed2 = player2_card[0].upper(), player2_card[1].upper()

    if seed1 == briscola and seed2 != briscola:
        return "Player 1 wins"
    elif seed1 != briscola and seed2 == briscola:
        return "Player 2 wins"
    elif seed1 != seed2:
        return "Player 1 wins"
    else:
        values_order = ['1', '2', '3', '4', '5', '6', '7', 'F', 'C', 'R']
        if values_order.index(value1) > values_order.index(value2):
            return "Player 1 wins"
        else:
            return "Player 2 wins"


def play_briscola():
    briscola = random.choice(['Bastoni', 'Spade', 'Coppe', 'Denari'])
    print("Briscola Seed:", briscola)
    player1_card = input("Player 1: ")
    while not is_valid_card(player1_card.strip()):
        print("Invalid card. Try again.")
        player1_card = input("Player 1: ")
    player2_card = input("Player 2: ")
    while not is_valid_card(player2_card.strip()):
        print("Invalid card. Try again.")
        player2_card = input("Player 2: ")
    print(
        f'You played {player1_card.strip().upper()} and your opponent played {player2_card.strip().upper()}')

    winner = get_winner(player1_card, player2_card, briscola)
    print(winner)


play_briscola()
