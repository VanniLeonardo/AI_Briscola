import random
from constants import *

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for value in VALUES: 
            for seed in SEEDS:
                self.cards.append((value + seed))
    
    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        
    
class Hand(Deck):
    def __init__(self):
        self.cards = []
        self.card_img = []
        self.points = 0
    
    def add_card(self, card):
        self.cards.append(card)

    def display_cards(self):
        for card in self.cards:
            cards = ''.join((card[0], card[1]))
            if cards not in self.card_img:
                self.card_img.append(cards)


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.points = 0
        self.status = ''
    
    def play_card(self, card):
        self.hand.cards.remove(card)
        return card

def round(player1, player2):
    global played_card1
    global played_card2
    print('Briscola:', briscola)
    if player1.status == 'won':
        played_card1 = input(f'Which card does {player1.name} want to play? ').upper()
        while played_card1 not in player1.hand.cards:
            print('Invalid card. Try again.')
            played_card1 = input(
                f'Which card does {player1.name} want to play? ').upper()
        player1.play_card(played_card1)
        print('Player 1 played', played_card1)
        played_card2 = input(
            f'Which card does {player2.name} want to play? ').upper()
        while played_card2 not in player2.hand.cards:
            print('Invalid card. Try again.')
            played_card2 = input(
                f'Which card does {player1.name} want to play? ').upper()
        player2.play_card(played_card2)
        print(f'{player2.name} played', played_card2)
        return played_card1, played_card2
    elif player2.status == 'won':
        played_card2 = input(
            f'Which card does {player2.name} want to play? ').upper()
        while played_card2 not in player2.hand.cards:
            print('Invalid card. Try again.')
            played_card2 = input(
                f'Which card does {player2.name} want to play? ').upper()
        player2.play_card(played_card2)
        print(f'{player2.name} played', played_card2)
        played_card1 = input(
            f'Which card does {player1.name} want to play? ').upper()
        while played_card1 not in player1.hand.cards:
            print('Invalid card. Try again.')
            played_card1 = input(
                f'Which card does {player1.name} want to play? ').upper()
        player1.play_card(played_card1)
        print(f'{player1.name} played', played_card1)
        return played_card1, played_card2
    
def calculate_points(played_card1, played_card2, player1, player2, briscola):
    if played_card1[1] == briscola[1] and played_card2[1] != briscola[1]:
        player1.add_points(
            VALUES_POINTS[played_card1[0]] + VALUES_POINTS[played_card2[0]])
        player1.status = 'won'
        player2.status = 'lost'
    elif played_card1[1] != briscola[1] and played_card2[1] == briscola[1]:
        player2.add_points(
            VALUES_POINTS[played_card1[0]] + VALUES_POINTS[played_card2[0]])
        player2.status = 'won'
        player1.status = 'lost'
    elif played_card1[1] == played_card2[1]:
        if VALUES_ORDER.index(played_card1[0]) > VALUES_ORDER.index(played_card2[0]):
            player1.add_points(
                VALUES_POINTS[played_card1[0]] + VALUES_POINTS[played_card2[0]])
            player1.status = 'won'
            player2.status = 'lost'
        else:
            player2.add_points(
                VALUES_POINTS[played_card1[0]] + VALUES_POINTS[played_card2[0]])
            player2.status = 'won'
            player1.status = 'lost'
    else:
        if player1.status == 'won':
            player1.add_points(
                VALUES_POINTS[played_card1[0]] + VALUES_POINTS[played_card2[0]])
            player1.status = 'won'
            player2.status = 'lost'
        else:
            player2.add_points(
                VALUES_POINTS[played_card1[0]] + VALUES_POINTS[played_card2[0]])
            player2.status = 'won'
            player1.status = 'lost'         
    print(f'{player1.name} points:', player1.points)
    print(f'{player2.name} points:', player2.points)


def draw_card(deck, player1, player2, briscola):
    if len(deck.cards) > 1:
        if player1.status == 'won':
            new_card = deck.draw()
            player1.hand.add_card(new_card)
            new_card = deck.draw()
            player2.hand.add_card(new_card)
        elif player2.status == 'won':
            new_card = deck.draw()
            player2.hand.add_card(new_card)
            new_card = deck.draw()
            player1.hand.add_card(new_card)
    elif len(deck.cards) == 1:
        new_card = deck.draw()
        if player1.status == 'won':
            player1.hand.add_card(new_card)
            player2.hand.add_card(briscola)
        elif player2.status == 'won':
            player2.hand.add_card(new_card)
            player1.hand.add_card(briscola) 
    print(player1.hand.cards)
    print(player2.hand.cards)
    print(player1.display_hand())
    print(player2.display_hand())
    print(len(deck.cards))

def prepare_game():
    global briscola
    global players_list
    deck = Deck()
    deck.shuffle()
    player1 = Player('Leonardo1')
    player2 = Player('Leonardo2')
    players_list = [player1, player2]
    for player in players_list:
        for i in range(3):
            new_card = deck.draw()
            player.hand.add_card(new_card)
    print(player1.hand.cards)
    print(player2.hand.cards)
    briscola = deck.draw()
    player1.status = 'won'
    play_game(player1, player2, deck, briscola)

def play_game(player1, player2, deck, briscola):
    while len(deck.cards) >= 0:
        round(player1, player2)
        calculate_points(played_card1, played_card2, player1, player2, briscola)
        draw_card(deck, player1, player2, briscola)
        if len(player1.hand.cards) == 0 and len(player2.hand.cards) == 0:
            check_winner(player1, player2)
            break

def check_winner(player1, player2):
    if player1.points > player2.points:
        print(f'{player1.name} won!')
    elif player1.points < player2.points:
        print(f'{player2.name} won!')
    else:
        print('Draw!')

# prepare_game()

