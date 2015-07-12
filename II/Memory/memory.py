# implementation of card game - Memory

import simplegui
import random
CARD_WIDTH = 50
CARD_HEIGTH = 100
x_card = CARD_WIDTH / 2
y_card = CARD_HEIGTH / 2
NUMBER_OF_CARDS = 16
canvas_w = CARD_WIDTH * NUMBER_OF_CARDS
canvas_h = CARD_HEIGTH

# helper function to initialize globals
def new_game():
    global deck, exposed
    
    deck_1 = range(8)
    deck_2 = range(8)
    deck_1.extend(deck_2)
    deck = deck_1
    exposed = [True,False] * 8
    random.shuffle(exposed)
    random.shuffle(deck)

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    x_pos=range(25, 776, 50)
    ind_pos = 0
    ind_exp = 0
    for card_number in deck:
        num_width = frame.get_canvas_textwidth(str(card_number), 40, 'sans-serif')
        canvas.draw_text(str(card_number), (x_pos[ind_pos] - (num_width / 2), 65), 50, 'Gray', 'sans-serif')
        ind_pos += 1
    for card_stat in exposed:
        if card_stat:
            left = x_pos[ind_exp] - x_card
            right = x_pos[ind_exp] + x_card
            canvas.draw_polygon([[left, 0], [right, 0], [right, 100], [left, 100]], 3, 'Green', 'Green')
        ind_exp += 1
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", canvas_w, canvas_h)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric