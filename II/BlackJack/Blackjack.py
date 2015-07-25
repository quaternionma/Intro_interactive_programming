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
player_hand=[]

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
        self.hand = []	# create Hand object

    def __str__(self):   # return a string representation of a hand
        message = "Hand contains"
        for i in range(len(self.hand)):
            message += (" " + str(self.hand[i]))
        return message     
    
    def add_card(self, card):
        self.hand.append(card)        	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_value = 0
        hand_ranks =[]
        for card in self.hand:
            card_value = VALUES.get(card.get_rank())
            hand_value += card_value
            hand_ranks.append(card.get_rank())
        if 'A' not in hand_ranks:
            return hand_value
        else:
            if hand_value + 10 <= 21:
                return hand_value + 10
            else:
                return hand_value
            
    def draw(self, canvas, pos):
    # draw a hand on the canvas, use the draw method for cards
        for card in self.hand:
            card.draw(canvas, pos)
            pos[0] = pos[0] + CARD_SIZE[0] + 5 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = [Card(i,j) for i in SUITS for j in RANKS]	# create a Deck object
 
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)    # use random.shuffle()

    def deal_card(self):
        return self.deck.pop()    # deal a card object from the deck
    
    def __str__(self):
        message = "Deck contains" # return a string representing the deck
        for i in range(len(self.deck)):
            message += (" " + str(self.deck[i]))
        return message	
    
#define event handlers for buttons
def deal():
    global outcome, in_play, score, new_deck, player_hand, dealer_hand
  
    if in_play:
        outcome = "You Loose! New Deal."
        score -= 1
    else:
        outcome = ""
    
    new_deck = Deck()
    new_deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(new_deck.deal_card())
    player_hand.add_card(new_deck.deal_card())
    
    dealer_hand = Hand()
    dealer_hand.add_card(new_deck.deal_card())
    dealer_hand.add_card(new_deck.deal_card())
    in_play = True
    
def hit():
    # replace with your code below
    global outcome, in_play, score
    if outcome == "You Loose! New Deal.":
        outcome = ""
    # if the hand is in play, hit the player
    if (player_hand.get_value() <= 21) and in_play:
        player_hand.add_card(new_deck.deal_card())
    # if busted, assign a message to outcome, update in_play and score
    if (player_hand.get_value() > 21) and in_play:
        outcome = "You have busted!"
        in_play = False
        score -= 1
        
def stand():
    # replace with your code below
    global outcome, in_play, score
    if outcome == "You Loose! New Deal.":
        outcome = ""
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(new_deck.deal_card())
        if dealer_hand.get_value() > 21:
            outcome = "Dealer has busted!"
            in_play = False
            score += 1
        else:
            if dealer_hand.get_value() == player_hand.get_value():
                outcome = "Dealer wins ties!"
                score -= 1
            elif dealer_hand.get_value() > player_hand.get_value():
                outcome = "Dealer wins!"
                score -=1
            else:
                outcome = "You win!"
                score += 1
            in_play = False
    elif (not in_play) and (player_hand.get_value() > 21):
        outcome = "You have busted!" 
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):    
    player_hand.draw(canvas, [50, 450])
    dealer_hand.draw(canvas, [50, 150])
    width = frame.get_canvas_textwidth("Blackjack", 28)
    canvas.draw_text("Blackjack", (300 - (width/2), 50), 34, 'Red', 'sans-serif')
    canvas.draw_text(outcome, (300, 125), 28, 'Black', 'sans-serif')
    canvas.draw_text("Dealer", (50, 125), 28, 'Black', 'sans-serif')
    canvas.draw_text("Player", (50, 425), 28, 'Black', 'sans-serif')
    if in_play:
        canvas.draw_text("Hit or Stand?", (300, 425), 28, 'Black', 'sans-serif')
        canvas.draw_image(card_back, (CARD_CENTER[0], CARD_CENTER[1]), CARD_SIZE, [50 + CARD_CENTER[0], 150 + CARD_CENTER[1]], CARD_SIZE)
    else:
        canvas.draw_text("New Deal?", (300, 425), 28, 'Black', 'sans-serif')
    canvas.draw_text("Score: " + str(score), (475, 75), 20, 'Black', 'sans-serif')
    
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