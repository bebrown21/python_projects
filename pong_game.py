# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
intial_pos = [WIDTH / 2, HEIGHT / 2]
paddle1_vel = 1
paddle2_vel = 1
speed_inc = 5
speed1 = 0
speed2 = 0


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel, x, y, time # these are vectors stored as lists
    if direction == RIGHT:
        x = random.randrange(2, 6)
        y = - random.randrange(1, 3)
    elif direction == LEFT:
        x = - random.randrange(2, 6)
        y = - random.randrange(1, 3)
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [x, y]
      
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    speed1 = 0
    speed2 = 0    
    paddle1_pos = [[0, 160 + paddle1_vel], [PAD_WIDTH, 160 + paddle1_vel], [PAD_WIDTH, 240 + paddle1_vel], [0, 240 + paddle1_vel]]
    paddle2_pos = ([WIDTH - PAD_WIDTH, 160], [WIDTH, 160], [WIDTH, 240], [WIDTH - PAD_WIDTH, 240])
    spawn_ball(True)
    
def reset():
    new_game()
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, intial_pos, x, y, time       
    global paddle1_vel, paddle2_vel
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
 
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White")  
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_vel += speed1
    paddle2_vel += speed2
    paddle_range = (HEIGHT / 2 - PAD_HEIGHT / 2)
    
    if paddle1_vel <= - paddle_range:
        paddle1_vel = - paddle_range
    elif paddle1_vel >= paddle_range:
        paddle1_vel = paddle_range
    if paddle2_vel <= - paddle_range:
        paddle2_vel = - paddle_range
    elif paddle2_vel >= paddle_range:
        paddle2_vel = paddle_range
        
    paddle1_pos = [[0, 160 + paddle1_vel], [PAD_WIDTH, 160 + paddle1_vel], [PAD_WIDTH, 240 + paddle1_vel], [0, 240 + paddle1_vel]]
    paddle2_pos = ([WIDTH - PAD_WIDTH, 160 + paddle2_vel], [WIDTH, 160 + paddle2_vel], [WIDTH, 240 + paddle2_vel], [WIDTH - PAD_WIDTH, 240 + paddle2_vel])
    
    # Extracting the paddle_pos on the y-axis to 
    paddle1_bot = paddle1_pos[1]
    paddle1_top = paddle1_pos[2]
    paddle2_bot = paddle2_pos[1]
    paddle2_top = paddle2_pos[2]
    
    # draw paddles
    canvas.draw_polygon(paddle1_pos, 2, "White", "White")
    canvas.draw_polygon(paddle2_pos, 2, "White", "White") 
    
    # determine whether paddle and ball collide    
    
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    
    # Paddle Collision check
    elif ball_pos[0] <= PAD_WIDTH + BALL_RADIUS and ball_pos[1] <= paddle1_top[1] and ball_pos[1] >= paddle1_bot[1]:
        ball_vel[0] = - ball_vel[0]
        ball_vel[0] += ball_vel[0] * 0.1
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS and ball_pos[1] <= paddle2_top[1] and ball_pos[1] >= paddle2_bot[1]:
        ball_vel[0] = - ball_vel[0]
        ball_vel[0] += ball_vel[0] * 0.1
    
    # Point awarding from gutter check 
    elif ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        score2 += 1
        spawn_ball(RIGHT)   
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        score1 += 1
        spawn_ball(LEFT)   
    
    # draw scores
    canvas.draw_text(str(score1), [50, 50], 50, "Red")
    canvas.draw_text(str(score2), [525, 50], 50, "Red")
    
def keydown(key):
    global paddle1_vel, paddle2_vel, speed1, speed2
    if key == simplegui.KEY_MAP["w"]:
        speed1 = - speed_inc
    elif key == simplegui.KEY_MAP["s"]:
        speed1 = speed_inc        
    if key == simplegui.KEY_MAP["up"]:
        speed2 = - speed_inc
    elif key == simplegui.KEY_MAP["down"]:
        speed2 = speed_inc  
        
def keyup(key):
    global paddle1_vel, paddle2_vel, speed1, speed2
    if key == simplegui.KEY_MAP["w"]:
        speed1 = 0
    elif key == simplegui.KEY_MAP["s"]:
        speed1 = 0        
    if key == simplegui.KEY_MAP["up"]:
        speed2 = 0
    elif key == simplegui.KEY_MAP["down"]:
        speed2 = 0
           
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button("Reset Game", reset)
# start frame
new_game()
frame.start()
