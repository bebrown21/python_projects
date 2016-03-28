# template for "Stopwatch: The Game"

import simplegui
import math

# define global variables
inc = 0
time = 0
x = 0
y = 0
start_game = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global time, mseconds
    seconds = (time // 10) % 60
    minutes = time // 600
    mseconds = time % 10
    if seconds < 9:
        return str(minutes) + ":0" + str(seconds) + "." + str(mseconds)
    else:
        return str(minutes) + ":" + str(seconds) + "." + str(mseconds)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global start_game
    timer.start()
    start_game = True

def stop():
    global x, y, inc, start_game
    timer.stop()  
    if inc %10 == 0 and start_game == True:
        x += 1
        start_game = False
    elif start_game == True:
        y += 1
        start_game = False
    else:
        return
    
def reset():
    global inc,x , y, start_game, time
    time = 0
    inc = 0
    x = 0
    y = 0
    timer.stop()
    start_game = False

# define event handler for timer with 0.1 sec interval
def timer():
    global inc, time
    inc += 1
    time = inc 
    print inc

# define draw handler
def draw(canvas):
    global time,x ,y
    text = format(time)
    canvas.draw_text(str(text), (115,150), 30, "White") 
    canvas.draw_text(str(x) + "/" + str(y), (160, 120), 25, "Red")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 300)

# register event handlers
timer = simplegui.create_timer(100, timer)
frame.set_draw_handler(draw)
start = frame.add_button("Start", start, 75)
stop = frame.add_button("Stop", stop, 75)
reset = frame.add_button("Reset", reset, 75)

# start frame
frame.start()


