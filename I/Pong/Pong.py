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

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    #ball_vel = [-1,5]
    if direction == LEFT:
        ball_vel = [-(random.randrange(120,240))/60, -(random.randrange(60,180))/60]
    elif direction == RIGHT:
        ball_vel = [(random.randrange(120,240))/60, -(random.randrange(60,180))/60]
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2]
    paddle2_pos = [(WIDTH - 1) - HALF_PAD_WIDTH, HEIGHT/2]
    paddle1_vel = 0
    paddle2_vel = 0
    direction = random.choice([LEFT, RIGHT])
    spawn_ball(direction)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel     
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        spawn_ball(RIGHT)
    elif ball_pos[0] >= (WIDTH - 1) - PAD_WIDTH - BALL_RADIUS:
        spawn_ball(LEFT)
        
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]        
       
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    paddle1_pos[1] += paddle1_vel
    upper_left1 = ((paddle1_pos[0] - HALF_PAD_WIDTH), (paddle1_pos[1] - HALF_PAD_HEIGHT))
    upper_right1 = ((paddle1_pos[0] + HALF_PAD_WIDTH), (paddle1_pos[1] - HALF_PAD_HEIGHT))
    lower_left1 = ((paddle1_pos[0] - HALF_PAD_WIDTH), (paddle1_pos[1] + HALF_PAD_HEIGHT))
    lower_right1 = ((paddle1_pos[0] + HALF_PAD_WIDTH), (paddle1_pos[1] + HALF_PAD_HEIGHT))
    canvas.draw_polygon([upper_left1, upper_right1, lower_right1, lower_left1], 1, 'White', 'White')
   
    paddle2_pos[1] += paddle2_vel
    upper_left2 = ((paddle2_pos[0] - HALF_PAD_WIDTH), (paddle2_pos[1] - HALF_PAD_HEIGHT))
    upper_right2 = ((paddle2_pos[0] + HALF_PAD_WIDTH), (paddle2_pos[1] - HALF_PAD_HEIGHT))
    lower_left2 = ((paddle2_pos[0] - HALF_PAD_WIDTH), (paddle2_pos[1] + HALF_PAD_HEIGHT))
    lower_right2 = ((paddle2_pos[0] + HALF_PAD_WIDTH), (paddle2_pos[1] + HALF_PAD_HEIGHT))
    canvas.draw_polygon([upper_left2, upper_right2, lower_right2, lower_left2], 1, 'White', 'White')
    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    vel_increment = 3
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel += vel_increment
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= vel_increment
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel += vel_increment
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= vel_increment
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    vel_increment = 3
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel -= vel_increment
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel += vel_increment
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel -= vel_increment
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel += vel_increment

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
