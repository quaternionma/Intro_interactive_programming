# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

# initialize global variables used in your code here
upper_limit = 100
secret_number = 0
number_of_guesses = 0

# helper function to start and restart the game
def new_game():        
    global secret_number    
    secret_number = random.randrange(0,upper_limit)
    
    print "Game (re)-starts in the range: [0," + str(upper_limit)+")"
    
    global number_of_guesses
    if upper_limit == 100:
        number_of_guesses = 7
    elif upper_limit == 1000:
        number_of_guesses = 10
    
    print "Number of remaining guesses is", number_of_guesses
    print ""

# helper function to check if there are remaining guesses    
def remaining_guesses():
    if number_of_guesses == 0:
        print "You loose! You have no more guesses!\n"
        new_game()
    else:
        return

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
    guess = int(guess)
    print "Guess was", guess
    
    # checks if the input guess is in the range
    if (upper_limit == 100) and (guess < 0 or guess > 99):
        print "Allowed range is 0-99! Try again\n"
        return
    if (upper_limit == 1000) and (guess < 0 or guess > 999):
        print "Allowed range is 0-999! Try again\n"
        return
    
    #print "secret", secret_number #That's for debugging
    
    global number_of_guesses
    if secret_number < guess:
        number_of_guesses = number_of_guesses - 1        
        print "Number of remaining guesses is", number_of_guesses
        print "Lower!\n"
        # calls the helper function to check for remaining guesses
        remaining_guesses()
    if secret_number > guess:
        number_of_guesses = number_of_guesses - 1        
        print "Number of remaining guesses is", number_of_guesses
        print "Higher!\n"
        # calls the helper function to check for remaining guesses
        remaining_guesses()
    if secret_number == guess:
        print "Correct!\n"
        new_game()
         
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
