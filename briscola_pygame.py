import pygame
from constants import *
from briscola_deck import *
import sys
import time

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Briscola")
screen.fill(BACKGROUND_COLOR)
pygame.draw.rect(screen, grey, pygame.Rect(0, 0, 250, 700))


class Play:
    def __init__(self):
        self.deck = Deck()
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.deck.shuffle()
        self.briscola = self.deck.draw()
         
    def show_deck(self):
        show_deck = pygame.image.load(
            'assets/' + "backside_briscola" + '.png').convert()
        show_deck = pygame.transform.scale(show_deck, (100, 150))
        screen.blit(show_deck, DECK_DISPLAY)

    def show_briscola(self):
        show_briscola = pygame.image.load(
            'assets/' + self.briscola + '.jpg').convert()
        show_briscola = pygame.transform.scale(show_briscola, (100, 150))
        show_briscola = pygame.transform.rotate(show_briscola, 90)
        screen.blit(show_briscola, BRISCOLA_DISPLAY)

    def erase_board(self): # erase the different Rects once you implement them (briscola, deck, player cards)
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, grey, pygame.Rect(0, 0, 250, 700))
        self.show_briscola()
        self.show_deck()
        if self.player1.status == "won":
            self.show_hand_player1()
        elif self.player2.status == "won":
            self.show_hand_player2()
    
    def hide_hand_player1(self):
        hide_player1_card1 = pygame.image.load(
            'assets/' + "backside_briscola" + '.png').convert()
        hide_player1_card1 = pygame.transform.scale(hide_player1_card1, (100, 150))
        screen.blit(hide_player1_card1, CARD_1_PLAYER1_DISPLAY)
        hide_player1_card2 = pygame.image.load(
            'assets/' + "backside_briscola" + '.png').convert()
        hide_player1_card2 = pygame.transform.scale(hide_player1_card2, (100, 150))
        screen.blit(hide_player1_card2, CARD_2_PLAYER1_DISPLAY)
        hide_player1_card3 = pygame.image.load(
            'assets/' + "backside_briscola" + '.png').convert()
        hide_player1_card3 = pygame.transform.scale(hide_player1_card3, (100, 150))
        screen.blit(hide_player1_card3, CARD_3_PLAYER1_DISPLAY)

    def hide_hand_player2(self):
        hide_player2_card1 = pygame.image.load(
            'assets/' + "backside_briscola" + '.png').convert()
        hide_player2_card1 = pygame.transform.scale(hide_player2_card1, (100, 150))
        screen.blit(hide_player2_card1, CARD_1_PLAYER2_DISPLAY)
        hide_player2_card2 = pygame.image.load(
            'assets/' + "backside_briscola" + '.png').convert()
        hide_player2_card2 = pygame.transform.scale(hide_player2_card2, (100, 150))
        screen.blit(hide_player2_card2, CARD_2_PLAYER2_DISPLAY)
        hide_player2_card3 = pygame.image.load(
            'assets/' + "backside_briscola" + '.png').convert()
        hide_player2_card3 = pygame.transform.scale(hide_player2_card3, (100, 150))
        screen.blit(hide_player2_card3, CARD_3_PLAYER2_DISPLAY)


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
            pass

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
            pass

    def show_hand_player1(self):
        self.player1.hand.display_cards()
        show_player1_card1 = pygame.image.load(
            'assets/' + self.player1.hand.card_img[0] + '.jpg').convert()
        show_player1_card1 = pygame.transform.scale(show_player1_card1, (100, 150))
        screen.blit(show_player1_card1, CARD_1_PLAYER1_DISPLAY)
        show_player1_card2 = pygame.image.load(
            'assets/' + self.player1.hand.card_img[1] + '.jpg').convert()
        show_player1_card2 = pygame.transform.scale(show_player1_card2, (100, 150))
        screen.blit(show_player1_card2, CARD_2_PLAYER1_DISPLAY)
        show_player1_card3 = pygame.image.load(
            'assets/' + self.player1.hand.card_img[2] + '.jpg').convert()
        show_player1_card3 = pygame.transform.scale(show_player1_card3, (100, 150))
        screen.blit(show_player1_card3, CARD_3_PLAYER1_DISPLAY)
        self.hide_hand_player2()

    def show_hand_player2(self):
        self.player2.hand.display_cards()
        show_player2_card1 = pygame.image.load(
            'assets/' + self.player2.hand.card_img[0] + '.jpg').convert()
        show_player2_card1 = pygame.transform.scale(show_player2_card1, (100, 150))
        screen.blit(show_player2_card1, CARD_1_PLAYER2_DISPLAY)
        show_player2_card2 = pygame.image.load(
            'assets/' + self.player2.hand.card_img[1] + '.jpg').convert()
        show_player2_card2 = pygame.transform.scale(show_player2_card2, (100, 150))
        screen.blit(show_player2_card2, CARD_2_PLAYER2_DISPLAY)
        show_player2_card3 = pygame.image.load(
            'assets/' + self.player2.hand.card_img[2] + '.jpg').convert()
        show_player2_card3 = pygame.transform.scale(show_player2_card3, (100, 150))
        screen.blit(show_player2_card3, CARD_3_PLAYER2_DISPLAY)
        self.hide_hand_player1()
    
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
        if len(self.deck.cards) > 0:
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
        if len(self.deck.cards) > 0:
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
        if len(self.deck.cards) > 0:
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
        if len(self.deck.cards) > 0:
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
        if len(self.deck.cards) > 0:
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
        if len(self.deck.cards) > 0:
            self.player2.hand.card_img.remove(played_card_player2)

    def calculate_score(self):
            value1, seed1 = played_card_player1[0], played_card_player1[1]
            value2, seed2 = played_card_player2[0], played_card_player2[1]
            if seed1 == self.briscola[1] and seed2 != self.briscola[1]:
                self.player1.status = "won"
                self.player2.status = "lost"
                self.player1.points += int(VALUES_POINTS[played_card_player1[0]]) + int(VALUES_POINTS[played_card_player2[0]])
            elif seed1 != self.briscola[1] and seed2 == self.briscola[1]:
                self.player2.status = "won"
                self.player1.status = "lost"
                self.player2.points += int(VALUES_POINTS[played_card_player1[0]]) + int(VALUES_POINTS[played_card_player2[0]])
            elif seed1 != seed2:
                #HERE IS THE PROBLEM (TO FIX REBUILD ENTIRE APPP WITH AN ARRAY AS THE LIST OF PLAYERS)
                self.player1.status = "won"
                self.player2.status = "lost"
                self.player1.points += int(VALUES_POINTS[played_card_player1[0]]) + int(VALUES_POINTS[played_card_player2[0]])
            else:
                if VALUES_ORDER.index(value1) > VALUES_ORDER.index(value2):
                    self.player1.status = "won"
                    self.player2.status = "lost"
                    self.player1.points += int(VALUES_POINTS[played_card_player1[0]]) + int(VALUES_POINTS[played_card_player2[0]])
                else:
                    self.player2.status = "won"
                    self.player1.status = "lost"
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
    
    def check_winner(self):
        if len(self.deck.cards) == 0 and len(self.player1.hand.cards) == 0 and len(self.player2.hand.cards) == 0:
            if self.player1.points > self.player2.points:
                game_finish("Player 1 wins with " + str(self.player1.points) + " points", 550, 350, red)
            elif self.player2.points > self.player1.points:
                game_finish("Player 2 wins with " + str(self.player2.points) + " points", 550, 350, red)
            else:
                game_finish("It's a tie!", 550, 350, red)

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
            #HERE IS THE PROBLEM
            if play_briscola.player1.status == "played" and play_briscola.player2.status == "played":
                play_briscola.calculate_score()
                print("player 1 points: " + str(play_briscola.player1.points))
                print("player 2 points: " + str(play_briscola.player2.points))
                print (len(play_briscola.deck.cards))
            play_briscola.check_winner()
        pygame.display.flip()
        clock.tick(60)

# PLAYER 1 PLAYS EVEN IF ITS PLAYER 2 TURN IN DECIDE TURN!! STILL SOMEHOW BUGGED 
#DOESNT UPDATE IMAGE OF LAST 6 CARDS

if __name__ == "__main__":
    game_loop()