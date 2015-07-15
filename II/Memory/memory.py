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
EXPOSED = True
NOT_EXPOSED = False
turn = 0

# helper function to initialize globals
def new_game():
    global deck, exposed, state, clicked_idx_store, turn
    state = 0
    clicked_idx_store = [None, None]
    turn = 0
    label.set_text("Turns = " + str(turn))
    deck_1 = range(8)
    deck_2 = range(8)
    deck_1.extend(deck_2)
    deck = deck_1
    exposed = [NOT_EXPOSED] * NUMBER_OF_CARDS
    random.shuffle(deck)
    label.set_text("Turns = " + str(turn))

    # define event handlers
def mouseclick(pos):
    # returns the index of the card clicked
    clicked = filter(lambda card: ((pos[0] >= (card - x_card)) and (pos[0] < (card + x_card))), x_pos)
    clicked_idx = x_pos.index(clicked[0])

    # mai game logic
    global state, clicked_idx_store, turn
    if not exposed[clicked_idx]:
        exposed[clicked_idx] = EXPOSED
        if state == 0:
            state = 1
            # uses a two elements list to store card index
            clicked_idx_store[0] = clicked_idx 
        elif state == 1:
            state = 2
            clicked_idx_store[1] = clicked_idx        
        else:
            state = 1     
            if deck[clicked_idx_store[0]] != deck[clicked_idx_store[1]]:
                exposed[clicked_idx_store[0]] = NOT_EXPOSED
                exposed[clicked_idx_store[1]] = NOT_EXPOSED
            clicked_idx_store[0] = clicked_idx
            turn += 1
            label.set_text("Turns = " + str(turn))

# cards are logically 50x100 pixels in size    
def draw(canvas):
    global x_pos
    # generates a list with x positions of the card centers
    x_pos=range(25, 776, 50)
    ind_pos = 0
    ind_exp = 0
    
    for card_number in deck:
        num_width = frame.get_canvas_textwidth(str(card_number), 40, 'sans-serif')
        canvas.draw_text(str(card_number), (x_pos[ind_pos] - (num_width / 2), 65), 50, 'Gray', 'sans-serif')
        ind_pos += 1
    
    for card_stat in exposed:
        if  not card_stat:
            left = x_pos[ind_exp] - x_card
            right = x_pos[ind_exp] + x_card
            canvas.draw_polygon([[left, 0], [right, 0], [right, 100], [left, 100]], 2, 'Gray', 'Green')
        ind_exp += 1

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", canvas_w, canvas_h)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turn))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric