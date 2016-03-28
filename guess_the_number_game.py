# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

num_range = 100
n = 7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, n
    secret_number = random.randrange(0, num_range)
    if num_range == 1000:
        return n == 10
    else:
        return n == 7
print "New Game!"
print "Begin guessing within the range of [0,", num_range, ")!"
print "You have ", n, "guesses left"
print
           
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range, n
    num_range = 100
    n = 7
    print "New Game!"
    print "Begin guessing within the range of [0, 100)!"
    print "You have ", n, "guesses left"
    print
    new_game()
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range, n
    num_range = 1000
    n = 10
    print "New Game!"
    print "Begin guessing within the range of [0, 1000)"
    print "You have ", n, "guesses left"
    print
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number, n
    inp = int(guess)
    n = n - 1
    print "Guess was ", guess
    print "You have ", n, "guesses left"
    if int(guess) < secret_number and n > 0:
        print "Higher"
        print
    elif int(guess) > secret_number and n > 0:
        print "Lower"
        print        
    elif int(guess) == secret_number and n > 0:
        print "Correct!"
        print
    else:
        print "Sorry, you're out of guesses!"
        print "Try again!"
        print
    return new_game()
    
# create frame
frame = simplegui.create_frame("Guess the Number", 200, 200)
button1 = frame.add_button("Range is [0, 100)", range100, 125)
button2 = frame.add_button("Range is [0, 1000)", range1000, 125)
inp = frame.add_input("Enter Guess", input_guess, 100)
# register event handlers for control elements and start frame
frame.start

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
