# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
            return 1
    elif name == 'paper' : 
            return 2
    elif name == 'lizard' : 
            return 3
    elif name == 'scissors' : 
            return 4
    else: return 'Error in name_to_number()'


def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else: return 'Error in number_to_name()'

def rpsls(player_choice): 
    #empty line
    print ''
    #print given input    
    print 'Player chooses', player_choice+'.'
    #computer guess
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5,1)
    comp_choice = number_to_name(comp_number)
    print 'Computer chooses', comp_choice+'.'
    #compute!
    player_number = name_to_number(player_choice)
    outcome = (comp_number - player_number)%5
    #determine outcome text 
    if outcome == 4 or outcome == 3: print 'Player wins!'
    elif outcome == 1 or outcome == 2: print 'Computer wins!'
    else: print 'Player and computer tie!'
   
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
