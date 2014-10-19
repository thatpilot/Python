# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global upper_limit
    secret_number = random.randrange(0, upper_limit, 1)
    print 
    print "New Game! Range is from 0 to", upper_limit
    print "Remaining guesses:", n, secret_number
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global upper_limit
    global n
    upper_limit = 100
    n = 7
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global upper_limit
    global n
    upper_limit = 1000
    n = 10
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    guess_int = int(guess)
    global secret_number
    global n
    m = n
    print 'Guess was', guess_int
    if secret_number == guess_int and m != 1:
        print "Correct!"
        new_game()
    elif secret_number > guess_int and m != 1:
        print "Higher! Remaining guesses:" , secret_number, n-1
        m = m-1
    elif secret_number < guess_int and m != 1:
        print "Lower! Remaining guesses:", secret_number, n-1
        m = m-1
    elif secret_number == guess_int and m == 1:
        print "Correct!"
        new_game()
    else:
        print 'YOU LOSE! You run out of guesses'
        new_game()
    
# create frame
frame = simplegui.create_frame ('GMN', 200, 200)

# register event handlers for control elements and start frame
frame.add_button('Range 100',range100, 50)
frame.add_button('Range 1000',range1000, 50)
frame.add_input('GUESS:', input_guess, 50)

# call new_game 
upper_limit = 100
n = 7
new_game()


# always remember to check your completed program against the grading rubric
