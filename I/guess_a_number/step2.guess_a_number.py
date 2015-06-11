# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui
import math

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randrange(0,100)
    
    frame.start()



# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    # remove this when you add your code    
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    pass
    
def input_guess(guess):
    # main game logic goes here	
    print "Guess was", guess
    guess = int(guess)
    print "secret", secret_number
    if secret_number < guess:
        print "Lower"     
    if secret_number > guess:
        print "Higher"
    if secret_number == guess:
        print "Correct!"
     
    
# create frame
frame = simplegui.create_frame("Guess the Number", 300, 300)

# register event handlers for control elements and start frame
frame.add_input("Your Guess Please", input_guess, 100)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
