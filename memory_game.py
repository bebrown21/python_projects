# implementation of card game - Memory

import simplegui
import random

choice1 = 0
choice2 = 0


# helper function to initialize globals
def new_game():
    global game_list, exposed, state, turn
    state = 0
    turn = 0
    game_list = [i%8 for i in range(16)]
    exposed = [False for i in range(16)]
    random.shuffle(game_list)
    label.set_text("Turns = " + str(turn))
     
# define event handlers
def mouseclick(pos):
    global state, exposed, choice1, choice2, turn, game_list
    # add game state logic here
    mouseclick = pos[0] / 50
     
    if state == 0:
        state = 1
        choice1 = mouseclick
        exposed[choice1] = True
        
    elif state == 1:
        if not exposed[mouseclick]:
            state = 2
            choice2 = mouseclick
            exposed[choice2] = True
            turn += 1
    else:
        if not exposed[mouseclick]:
            if game_list[choice1] == game_list[choice2]:
                pass  
            else:
                exposed[choice1] = False
                exposed[choice2] = False
            choice1 = mouseclick
            exposed[choice1] = True
            state = 1
    label.set_text("Turns = " + str(turn))
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(16):
        if exposed[i]:
            canvas.draw_text(str(game_list[i]), (50*i + 10, 60), 40, "Red")
        else:
            canvas.draw_polygon([(50*i, 0), (50*i + 50, 0),(50*i + 50, 100), (50*i, 100)], 1, "White", "Green")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric