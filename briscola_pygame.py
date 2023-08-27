import pygame
from constants import *
from briscola_deck import *
import sys
import time
import threading

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Briscola")
screen.fill(BACKGROUND_COLOR)
pygame.draw.rect(screen, grey, pygame.Rect(0, 0, 250, 700))

# FIX RECTANGLES
class Play:
    def __init__(self):
        self.deck = Deck()
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.players_list = [self.player1, self.player2]
        self.deck.shuffle()
        self.briscola = self.deck.draw()
         
    def show_deck(self):
        deck = pygame.image.load(
            'assets/' + "backside_briscola" + '.png').convert()
        deck = pygame.transform.scale(deck, (100, 150))
        deck_rect = deck.get_rect()
        deck_rect.center = (DECK_DISPLAY)
        screen.blit(deck, deck_rect)

    def erase_deck(self):
        x = pygame.image.load(
            'assets/' + "backside_briscola" + '.png').convert()
        x = pygame.transform.scale(x, (100, 150))
        x.fill(BACKGROUND_COLOR)
        x_rect = x.get_rect()
        x_rect.center = (DECK_DISPLAY)
        screen.blit(x, x_rect)
        y = pygame.image.load(
            'assets/' + "backside_briscola" + '.png').convert()
        y = pygame.transform.scale(y, (100, 150))
        y = pygame.transform.rotate(y, 90)
        y.fill(BACKGROUND_COLOR)
        y_rect = y.get_rect()
        y_rect.center = (BRISCOLA_DISPLAY)
        screen.blit(y, y_rect)

    def show_briscola(self):
        show_briscola = pygame.image.load(
            'assets/' + self.briscola + '.jpg').convert()
        show_briscola = pygame.transform.scale(show_briscola, (100, 150))
        show_briscola = pygame.transform.rotate(show_briscola, 90)
        show_briscola_rect = show_briscola.get_rect()
        show_briscola_rect.center = (BRISCOLA_DISPLAY)
        screen.blit(show_briscola, show_briscola_rect)

    def erase_played(self):
        x = pygame.image.load(
            'assets/' + "backside_briscola" + '.png').convert()
        x = pygame.transform.scale(x, (100, 150))
        x.fill(BACKGROUND_COLOR)
        screen.blit(x, PLAYER1_PLAYEDCARD_DISPLAY)
        screen.blit(x, PLAYER2_PLAYEDCARD_DISPLAY)


    def erase_board(self):
        if len(self.deck.cards) < 1:
            x = pygame.image.load(
                'assets/' + "backside_briscola" + '.png').convert()
            x = pygame.transform.scale(x, (100, 150))
            x.fill(BACKGROUND_COLOR)
            if len(self.player1.hand.cards) == 2:
                screen.blit(x, show_player1_card3_rect)
            elif len(self.player1.hand.cards) == 1:
                screen.blit(x, show_player1_card3_rect)
                screen.blit(x, show_player1_card2_rect)
            elif len(self.player1.hand.cards) == 0:
                screen.blit(x, show_player1_card1_rect)
                screen.blit(x, show_player1_card2_rect)
                screen.blit(x, show_player1_card3_rect)
            if len(self.player2.hand.cards) == 2:
                screen.blit(x, show_player2_card3_rect)
            elif len(self.player2.hand.cards) == 1:
                screen.blit(x, show_player2_card3_rect)
                screen.blit(x, show_player2_card2_rect)
            elif len(self.player2.hand.cards) == 0:
                screen.blit(x, show_player2_card1_rect)
                screen.blit(x, show_player2_card2_rect)
                screen.blit(x, show_player2_card3_rect)

    def show_hand_player1(self):
        global show_player1_card1_rect, show_player1_card2_rect, show_player1_card3_rect
        self.player1.hand.display_cards()
        if len(self.player1.hand.cards) > 0:
            show_player1_card1 = pygame.image.load(
                'assets/' + self.player1.hand.card_img[0] + '.jpg').convert()
            show_player1_card1 = pygame.transform.scale(show_player1_card1, (100, 150))
            show_player1_card1_rect = show_player1_card1.get_rect()
            show_player1_card1_rect.center = (CARD_1_PLAYER1_DISPLAY)
            screen.blit(show_player1_card1, show_player1_card1_rect)
            if len(self.player1.hand.cards) > 1:
                show_player1_card2 = pygame.image.load(
                    'assets/' + self.player1.hand.card_img[1] + '.jpg').convert()
                show_player1_card2 = pygame.transform.scale(show_player1_card2, (100, 150))
                show_player1_card2_rect = show_player1_card2.get_rect()
                show_player1_card2_rect.center = (CARD_2_PLAYER1_DISPLAY)
                screen.blit(show_player1_card2, show_player1_card2_rect)
                if len(self.player1.hand.cards) > 2:
                    show_player1_card3 = pygame.image.load(
                        'assets/' + self.player1.hand.card_img[2] + '.jpg').convert()
                    show_player1_card3 = pygame.transform.scale(show_player1_card3, (100, 150))
                    show_player1_card3_rect = show_player1_card3.get_rect()
                    show_player1_card3_rect.center = (CARD_3_PLAYER1_DISPLAY)
                    screen.blit(show_player1_card3, show_player1_card3_rect)
        self.hide_hand_player2()

    def show_hand_player2(self):
        global show_player2_card1_rect, show_player2_card2_rect, show_player2_card3_rect
        self.player2.hand.display_cards()
        if len(self.player2.hand.cards) > 0:
            show_player2_card1 = pygame.image.load(
                'assets/' + self.player2.hand.card_img[0] + '.jpg').convert()
            show_player2_card1 = pygame.transform.scale(show_player2_card1, (100, 150))
            show_player2_card1_rect = show_player2_card1.get_rect()
            show_player2_card1_rect.center = (CARD_1_PLAYER2_DISPLAY)
            screen.blit(show_player2_card1, show_player2_card1_rect)
            if len(self.player2.hand.cards) > 1:
                show_player2_card2 = pygame.image.load(
                    'assets/' + self.player2.hand.card_img[1] + '.jpg').convert()
                show_player2_card2 = pygame.transform.scale(show_player2_card2, (100, 150))
                show_player2_card2_rect = show_player2_card2.get_rect()
                show_player2_card2_rect.center = (CARD_2_PLAYER2_DISPLAY)
                screen.blit(show_player2_card2, show_player2_card2_rect)
                if len(self.player2.hand.cards) > 2:
                    show_player2_card3 = pygame.image.load(
                        'assets/' + self.player2.hand.card_img[2] + '.jpg').convert()
                    show_player2_card3 = pygame.transform.scale(show_player2_card3, (100, 150))
                    show_player2_card3_rect = show_player2_card3.get_rect()
                    show_player2_card3_rect.center = (CARD_3_PLAYER2_DISPLAY)
                    screen.blit(show_player2_card3, show_player2_card3_rect)
        self.hide_hand_player1()

    def hide_hand_player1(self):
        hide_player1_card1 = pygame.image.load(
            'assets/' + "backside_briscola" + '.png').convert()
        hide_player1_card1 = pygame.transform.scale(hide_player1_card1, (100, 150))
        hide_player1_card1_rect = hide_player1_card1.get_rect()
        hide_player1_card1_rect.center = (CARD_1_PLAYER1_DISPLAY)
        screen.blit(hide_player1_card1, hide_player1_card1_rect)
        hide_player1_card2 = pygame.image.load(
            'assets/' + "backside_briscola" + '.png').convert()
        hide_player1_card2 = pygame.transform.scale(hide_player1_card2, (100, 150))
        hide_player1_card2_rect = hide_player1_card2.get_rect()
        hide_player1_card2_rect.center = (CARD_2_PLAYER1_DISPLAY)
        screen.blit(hide_player1_card2, hide_player1_card2_rect)
        hide_player1_card3 = pygame.image.load(
            'assets/' + "backside_briscola" + '.png').convert()
        hide_player1_card3 = pygame.transform.scale(hide_player1_card3, (100, 150))
        hide_player1_card3_rect = hide_player1_card3.get_rect()
        hide_player1_card3_rect.center = (CARD_3_PLAYER1_DISPLAY)
        screen.blit(hide_player1_card3, hide_player1_card3_rect)

    def hide_hand_player2(self):
        hide_player2_card1 = pygame.image.load(
            'assets/' + "backside_briscola" + '.png').convert()
        hide_player2_card1 = pygame.transform.scale(hide_player2_card1, (100, 150))
        hide_player2_card1_rect = hide_player2_card1.get_rect()
        hide_player2_card1_rect.center = (CARD_1_PLAYER2_DISPLAY)
        screen.blit(hide_player2_card1, hide_player2_card1_rect)
        hide_player2_card2 = pygame.image.load(
            'assets/' + "backside_briscola" + '.png').convert()
        hide_player2_card2 = pygame.transform.scale(hide_player2_card2, (100, 150))
        hide_player2_card2_rect = hide_player2_card2.get_rect()
        hide_player2_card2_rect.center = (CARD_2_PLAYER2_DISPLAY)
        screen.blit(hide_player2_card2, hide_player2_card2_rect)
        hide_player2_card3 = pygame.image.load(
            'assets/' + "backside_briscola" + '.png').convert()
        hide_player2_card3 = pygame.transform.scale(hide_player2_card3, (100, 150))
        hide_player2_card3_rect = hide_player2_card3.get_rect()
        hide_player2_card3_rect.center = (CARD_3_PLAYER2_DISPLAY)
        screen.blit(hide_player2_card3, hide_player2_card3_rect)


    def draw_player1(self):
        if len(self.deck.cards) > 1:
            self.player1.hand.add_card(self.deck.draw())
        elif len(self.deck.cards) == 1:
            if self.player1.status == "won":
                self.player1.hand.add_card(self.deck.draw())
                self.player2.hand.add_card(self.briscola)
            elif self.player2.status == "won":
                self.player2.hand.add_card(self.deck.draw())
                self.player1.hand.add_card(self.briscola)
        else:
            self.erase_deck()

    def draw_player2(self):
        if len(self.deck.cards) > 1:
            self.player2.hand.add_card(self.deck.draw())
        elif len(self.deck.cards) == 1:
            if self.player2.status == "won":
                self.player2.hand.add_card(self.deck.draw())
                self.player1.hand.add_card(self.briscola)
            elif self.player1.status == "won":
                self.player1.hand.add_card(self.deck.draw())
                self.player2.hand.add_card(self.briscola)
        else:
            self.erase_deck()

    
    def play_card1_player1(self):
        global played_card_player1
        played_card_player1 = self.player1.hand.cards[0]
        self.player1.play_card(played_card_player1)
        show_player1_playedcard = pygame.image.load(
            'assets/' + played_card_player1 + '.jpg').convert()
        show_player1_playedcard = pygame.transform.scale(show_player1_playedcard, (100, 150))
        screen.blit(show_player1_playedcard, PLAYER1_PLAYEDCARD_DISPLAY)
        self.player1.status = "played"
        if self.player2.status != "played":
            self.show_hand_player2()
        self.player1.hand.card_img.remove(played_card_player1)

    def play_card2_player1(self):
        global played_card_player1
        played_card_player1 = self.player1.hand.cards[1]
        self.player1.play_card(played_card_player1)
        show_player1_playedcard = pygame.image.load(
            'assets/' + played_card_player1 + '.jpg').convert()
        show_player1_playedcard = pygame.transform.scale(show_player1_playedcard, (100, 150))
        screen.blit(show_player1_playedcard, PLAYER1_PLAYEDCARD_DISPLAY)
        self.player1.status = "played"
        if self.player2.status != "played":
            self.show_hand_player2()
        self.player1.hand.card_img.remove(played_card_player1)

    def play_card3_player1(self):
        global played_card_player1
        played_card_player1 = self.player1.hand.cards[2]
        self.player1.play_card(played_card_player1)
        show_player1_playedcard = pygame.image.load(
            'assets/' + played_card_player1 + '.jpg').convert()
        show_player1_playedcard = pygame.transform.scale(show_player1_playedcard, (100, 150))
        screen.blit(show_player1_playedcard, PLAYER1_PLAYEDCARD_DISPLAY)
        self.player1.status = "played"
        if self.player2.status != "played":
            self.show_hand_player2()
        self.player1.hand.card_img.remove(played_card_player1)

    def play_card1_player2(self):
        global played_card_player2
        played_card_player2 = self.player2.hand.cards[0]
        self.player2.play_card(played_card_player2)
        show_player2_playedcard = pygame.image.load(
            'assets/' + played_card_player2 + '.jpg').convert()
        show_player2_playedcard = pygame.transform.scale(show_player2_playedcard, (100, 150))
        screen.blit(show_player2_playedcard, PLAYER2_PLAYEDCARD_DISPLAY)
        self.player2.status = "played"
        if self.player1.status != "played":
            self.show_hand_player1()
        self.player2.hand.card_img.remove(played_card_player2)
        
        
    def play_card2_player2(self):
        global played_card_player2
        played_card_player2 = self.player2.hand.cards[1]
        self.player2.play_card(played_card_player2)
        show_player2_playedcard = pygame.image.load(
            'assets/' + played_card_player2 + '.jpg').convert()
        show_player2_playedcard = pygame.transform.scale(show_player2_playedcard, (100, 150))
        screen.blit(show_player2_playedcard, PLAYER2_PLAYEDCARD_DISPLAY)
        self.player2.status = "played"
        if self.player1.status != "played":
            self.show_hand_player1()
        self.player2.hand.card_img.remove(played_card_player2)
    
    def play_card3_player2(self):
        global played_card_player2
        played_card_player2 = self.player2.hand.cards[2]
        self.player2.play_card(played_card_player2)
        show_player2_playedcard = pygame.image.load(
            'assets/' + played_card_player2 + '.jpg').convert()
        show_player2_playedcard = pygame.transform.scale(show_player2_playedcard, (100, 150))
        screen.blit(show_player2_playedcard, PLAYER2_PLAYEDCARD_DISPLAY)
        self.player2.status = "played"
        if self.player1.status != "played":
            self.show_hand_player1()
        self.player2.hand.card_img.remove(played_card_player2)

    def deck_length(self):
        if len(self.deck.cards) > 0:
            self.show_deck()
            game_finish(str(len(self.deck.cards)), DECK_DISPLAY[0], DECK_DISPLAY[1], red)

    def calculate_score(self):
            value1, seed1 = played_card_player1[0], played_card_player1[1]
            value2, seed2 = played_card_player2[0], played_card_player2[1]
            if seed1 == self.briscola[1] and seed2 != self.briscola[1]:
                self.player1.status = "won"
                self.player2.status = "lost"
                self.players_list = [self.player1, self.player2]
                self.player1.points += int(VALUES_POINTS[played_card_player1[0]]) + int(VALUES_POINTS[played_card_player2[0]])
            elif seed1 != self.briscola[1] and seed2 == self.briscola[1]:
                self.player2.status = "won"
                self.player1.status = "lost"
                self.players_list = [self.player2, self.player1]
                self.player2.points += int(VALUES_POINTS[played_card_player1[0]]) + int(VALUES_POINTS[played_card_player2[0]])
            elif seed1 != seed2:
                if self.players_list[0] == self.player1:
                    self.player1.status = "won"
                    self.player2.status = "lost"
                    self.player1.points += int(VALUES_POINTS[played_card_player1[0]]) + int(VALUES_POINTS[played_card_player2[0]])
                elif self.players_list[0] == self.player2:
                    self.player2.status = "won"
                    self.player1.status = "lost"
                    self.player2.points += int(VALUES_POINTS[played_card_player1[0]]) + int(VALUES_POINTS[played_card_player2[0]])
            else:
                if VALUES_ORDER.index(value1) > VALUES_ORDER.index(value2):
                    self.player1.status = "won"
                    self.player2.status = "lost"
                    self.players_list = [self.player1, self.player2]
                    self.player1.points += int(VALUES_POINTS[played_card_player1[0]]) + int(VALUES_POINTS[played_card_player2[0]])
                else:
                    self.player2.status = "won"
                    self.player1.status = "lost"
                    self.players_list = [self.player2, self.player1]
                    self.player2.points += int(VALUES_POINTS[played_card_player1[0]]) + int(VALUES_POINTS[played_card_player2[0]])
            self.decide_turn()
    
    def decide_turn(self): 
        if self.player1.status == "won":
            self.draw_player1()
            self.draw_player2()
            self.show_hand_player1()
        elif self.player2.status == "won":
            self.draw_player2()
            self.draw_player1()
            self.show_hand_player2()
        self.deck_length()
        start_time = threading.Timer(2.5, self.erase_played)
        start_time.start()
    
    def check_winner(self):
        if len(self.deck.cards) == 0 and len(self.player1.hand.cards) == 0 and len(self.player2.hand.cards) == 0:
            if self.player1.points > self.player2.points:
                game_finish("Player 1 wins with " + str(self.player1.points) + " points", 550, 350, red)
            elif self.player2.points > self.player1.points:
                game_finish("Player 2 wins with " + str(self.player2.points) + " points", 550, 350, red)
            else:
                game_finish("It's a tie!", 550, 350, red)
            game_ended = True

    def exit(self):
        pygame.quit()
        sys.exit()


# Text
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def end_text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def game_texts(text, x, y):
    TextSurf, TextRect = text_objects(text, textfont)
    TextRect.center = (x, y)
    screen.blit(TextSurf, TextRect)
    pygame.display.update()


def game_finish(text, x, y, color):
    TextSurf, TextRect = end_text_objects(text, game_end, color)
    TextRect.center = (x, y)
    screen.blit(TextSurf, TextRect)
    pygame.display.update()


# button display
def button(
    msg, x, y, w, h, ic, ac, action=None
):  # w = width, h = height, ic = inactive color, ac = active color
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))
    TextSurf, TextRect = text_objects(msg, font)
    TextRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(TextSurf, TextRect)

def game_loop():
    running = True
    play_briscola = Play()
    play_briscola.show_briscola()
    play_briscola.show_deck()
    for i in range(3):
        play_briscola.draw_player1()
        play_briscola.draw_player2()
    play_briscola.show_hand_player1()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
            play_briscola.erase_board()
            button("Card 1", 30, 100, 150, 50, light_slat,
                        dark_slat, play_briscola.play_card1_player1 if play_briscola.player1.status == "" or play_briscola.player1.status == "won" or play_briscola.player2.status == "played" else play_briscola.play_card1_player2
                        )
            button("Card 2", 30, 200, 150, 50, light_slat,
                        dark_slat, play_briscola.play_card2_player1 if play_briscola.player1.status == "" or play_briscola.player1.status == "won" or play_briscola.player2.status == "played" else play_briscola.play_card2_player2
                        )
            button("Card 3", 30, 300, 150, 50, light_slat,
                        dark_slat,  play_briscola.play_card3_player1 if play_briscola.player1.status == "" or play_briscola.player1.status == "won" or play_briscola.player2.status == "played" else play_briscola.play_card3_player2
                        )
            button("EXIT", 30, 500, 150, 50, light_slat,
                        dark_red, play_briscola.exit
                        )
            mouse_pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                if show_player1_card1_rect.collidepoint(mouse_pos) and (play_briscola.player1.status == "" or play_briscola.player1.status == "won" or play_briscola.player2.status == "played"):
                    play_briscola.play_card1_player1()
                if show_player1_card2_rect.collidepoint(mouse_pos) and (play_briscola.player1.status == "" or play_briscola.player1.status == "won" or play_briscola.player2.status == "played"):
                    play_briscola.play_card2_player1()
                if show_player1_card3_rect.collidepoint(mouse_pos) and (play_briscola.player1.status == "" or play_briscola.player1.status == "won" or play_briscola.player2.status == "played"):
                    play_briscola.play_card3_player1()
                if show_player2_card1_rect.collidepoint(mouse_pos) and (play_briscola.player2.status == "" or play_briscola.player2.status == "won" or play_briscola.player1.status == "played"):
                    play_briscola.play_card1_player2()
                if show_player2_card2_rect.collidepoint(mouse_pos) and (play_briscola.player2.status == "" or play_briscola.player2.status == "won" or play_briscola.player1.status == "played"):
                    play_briscola.play_card2_player2()
                if show_player2_card3_rect.collidepoint(mouse_pos) and (play_briscola.player2.status == "" or play_briscola.player2.status == "won" or play_briscola.player1.status == "played"):
                    play_briscola.play_card3_player2()
            if play_briscola.player1.status == "played" and play_briscola.player2.status == "played":
                play_briscola.calculate_score()
                print("player 1 points: " + str(play_briscola.player1.points))
                print("player 2 points: " + str(play_briscola.player2.points))
                print (f"Cards in deck: {len(play_briscola.deck.cards)}")
            play_briscola.check_winner()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    game_loop()