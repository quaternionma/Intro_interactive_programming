# Rock-paper-scissors-lizard-Spock


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
# helper functions

import random

def name_to_number(name):
    """Assigns strings a number between 0 and 4 accordingly to the rules mentioned"""
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3    
    elif name == "scissors":
        number = 4
    else:
        number = 'name must be either "rock", "Spock", "paper", "lizard", or "scissors"'
    return number

def number_to_name(number):
    """Assigns a number between 0 and 4 to one of the five strings accordingly to the rules mentioned"""
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"    
    elif number == 4:
        name = "scissors"
    else:
        name = 'number must an integer between 0 and 4'
    return name

def rpsls(player_choice): 
    
    print "" 										# blank line to separate consecutive games 
    print "Player chooses", player_choice 			#prints the Player's choice
    
    player_number = name_to_number(player_choice) 	# converts the player_choice in to number using 
                                                    # name_to_number helper function											 
    
    comp_number = random.randrange(0,5) 			# computes a random integer between 0 and 4
    
    comp_choice = number_to_name(comp_number)     	# converts random number in to string using 
                                                    # number_to_name helper function
    
    print "Computer chooses", comp_choice 			# prints computer's choice
    
    modulo = (player_number - comp_number) % 5		#computes the difference between player's and comp number  taken modulo five
    
    if (modulo == 1) or (modulo == 2):
        print "Player wins!"
    elif (modulo == 3) or (modulo == 4):
        print "Computer wins!"
    else:
        print "Player and Computer tie!"

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


