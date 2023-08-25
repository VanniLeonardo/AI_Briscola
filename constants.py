import pygame

VALUES = ['1', '2', '3', '4', '5', '6', '7', 'F', 'C', 'R']
SEEDS = ['B', 'S', 'C', 'D'] # Bastoni, Spade, Coppe, Denari
VALUES_ORDER = ['2', '4', '5', '6', '7', 'F', 'C', 'R', '3', '1']
VALUES_POINTS = {'1': 11, '2': 0, '3': 10, '4': 0, '5': 0, '6': 0, '7': 0, 'F': 2, 'C': 3, 'R': 4} 
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)

DISPLAY_WIDTH = 900
DISPLAY_HEIGHT = 700
CARD_1_PLAYER1_DISPLAY = (650, 500)
CARD_2_PLAYER1_DISPLAY = (525, 500)
CARD_3_PLAYER1_DISPLAY = (400, 500)
CARD_1_PLAYER2_DISPLAY = (650, 50)
CARD_2_PLAYER2_DISPLAY = (525, 50)
CARD_3_PLAYER2_DISPLAY = (400, 50)
BRISCOLA_DISPLAY = (350, 300)
DECK_DISPLAY = (300, 275)
PLAYER1_PLAYEDCARD_DISPLAY = (575, 275)
PLAYER2_PLAYEDCARD_DISPLAY = (575, 275)

BACKGROUND_COLOR = (34, 139, 34)
grey = (220, 220, 220)
black = (0, 0, 0)
green = (0, 200, 0)
red = (255, 0, 0)
light_slat = (119, 136, 153)
dark_slat = (47, 79, 79)
dark_red = (255, 0, 0)
pygame.init()
font = pygame.font.SysFont("Arial", 20)
textfont = pygame.font.SysFont('Comic Sans MS', 35)
game_end = pygame.font.SysFont('dejavusans', 52)
blackjack = pygame.font.SysFont('roboto', 70)
