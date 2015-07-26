#! /usr/bin/env python
#coding=utf-8
# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = [] 	# create Hand object

    def __str__(self):
        ans = ''
        for card in self.hand:
            ans += ' '+ card.__str__()
              # return a string representation of a hand
        return 'Hand contains'+ ans

    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        have_ace = 0
        hand_value = 0
        for card in self.hand:
            hand_value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                have_ace = 1
        if have_ace == 0:        
            return hand_value
        else:
            if hand_value + 10 <= 21:
                return hand_value +10
            else:
                return hand_value +1
    def draw(self, canvas, pos):
            # draw a hand on the canvas, use the draw method for cards
        for i, card in enumerate(self.hand):
            if i < 5:
                card.draw(canvas, (pos[0] + i*1.35*CARD_SIZE[0], pos[1]))
            else:
                card.draw(canvas, (pos[0] + (i%5)*1.35*CARD_SIZE[0], pos[1] + 1.2*CARD_SIZE[1]))

        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []	# create a Deck object
        self.deck = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        #self.shuffle()

    def shuffle(self):
        self.__init__()
        random.shuffle(self.deck)

    def deal_card(self):
        if len(self.deck) > 0:
            return self.deck.pop(0)
        else:
            print 'deck is empty'
            return None	# deal a card object from the deck
    
    def __str__(self):
        ans = ''
        for card in self.deck:
            ans += ' '+ card.__str__()
              # return a string representation of a hand
        return 'Deck contains'+ ans
    # return a string representing the deck



#define event handlers for buttons
def deal():
    global outcome, in_play, player, dealer, warning, score, deck

    # your code goes here
    if in_play:
        score = -1
        
    deck = Deck()
    deck.shuffle()
    
    player, dealer = Hand(), Hand()
    
    outcome = ''
    warning = 'Hit or stand?'
    in_play = True

    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    
def hit():
    
    global player, deck, in_play, outcome, warning, score
    if in_play and player.get_value() <= 21:
        player.add_card(deck.deal_card())
        # if busted, assign a message to outcome, update in_play and score
        if player.get_value() > 21:
            outcome = "You went bust and lose."
            warning = "New deal?"
            in_play = False
            score -= 1   
def stand():
    # replace with your code below   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    
    global in_play, dealer, player, outcome, warning, score
    if in_play is True:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        dealer_value = dealer.get_value()
        # assign a message to outcome, update in_play and score
        if  dealer_value > 21:
            outcome = "Dealer went bust. You win."
            score += 1
        else:
            player_value = player.get_value()
            if player_value <= dealer_value:
                outcome = "You lose."
                score -= 1
            else:
                outcome = "You win."
                score += 1
        tips = "New deal?"
        in_play = False

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    canvas.draw_text("Blackjack", (100,40), 40, "Blue")
    canvas.draw_text("Score " + str(score), (400, 40), 30, "Black")
    canvas.draw_text("Dealer", (60, 80), 30, "Black")
    canvas.draw_text(outcome, (200, 80), 30, "Red")
    dealer.draw(canvas, (60, 100))
    # in_play state draw a back card 
    if in_play is True:
        card_loc = (CARD_BACK_CENTER[0] + CARD_BACK_SIZE[0], CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [60 + CARD_BACK_CENTER[0], 100 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    canvas.draw_text(outcome, (200, 80), 30, "Red") 
    canvas.draw_text("Player", (60, 350), 30, "Black")
    canvas.draw_text(warning, (200, 350), 30, "Black")
    player.draw(canvas, (60, 370))
   

  # initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
