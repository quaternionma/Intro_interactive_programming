# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui
import math

# initialize global variables used in your code here
upper_limit = 100
secret_number= 0 

# helper function to start and restart the game
def new_game():        
    global secret_number    
    secret_number = random.randrange(0,upper_limit)
    
    print "Game (re)-starts in the range: 0-" + str(upper_limit)
    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global upper_limit
    upper_limit = 100
    new_game()
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global upper_limit
    upper_limit = 1000
    new_game()
    
    
def input_guess(guess):
    # main game logic goes here	
    print "Guess was", guess
    guess = int(guess)
    print "secret", secret_number
    if secret_number < guess:
        print "Lower\n"     
    if secret_number > guess:
        print "Higher\n"
    if secret_number == guess:
        print "Correct!\n"
     
    
# create frame
frame = simplegui.create_frame("Guess the Number", 300, 300)

# register event handlers for control elements and start frame
frame.add_input("Your Guess Please", input_guess, 200)
frame.add_button("Range: [0,100)", range100, 200)
frame.add_button("Range: [0,1000)", range1000, 200)
# call new_game 
new_game()
frame.start()

# always remember to check your completed program against the grading rubric
