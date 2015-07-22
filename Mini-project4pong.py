#! /usr/bin/env python
#coding=utf-8
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
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel = [random.randrange(120, 240)/60, -random.randrange(60, 180)/60] 
    if direction == LEFT:  
        ball_vel[0] = -ball_vel[0]  

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints    
    paddle1_pos, paddle2_pos = HEIGHT / 2, HEIGHT / 2
    paddle1_vel, paddle2_vel = 0, 0
    score1, score2 = 0, 0
    spawn_ball(random.choice([LEFT, RIGHT]))
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global HEIGHT, HALF_PAD_HEIGHT
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    # if the ball touches  the left gutters
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        
        # if the ball touches the left paddle 
        if ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT and ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT:
            ball_vel[0] = -(ball_vel[0] + 0.1 * ball_vel[0])
            ball_vel[1] = ball_vel[1] + 0.1 * ball_vel[1]
        else:
            score2 += 1
            spawn_ball(RIGHT)
    # if the ball touches  the right gutters        
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
 
        # if the ball touches the right paddle
        if ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT and ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = -(ball_vel[0] + 0.1 * ball_vel[0])
            ball_vel[1] = ball_vel[1] + 0.1 * ball_vel[1]
            
        else:
            score1 += 1
            spawn_ball(LEFT)
   
    # if the ball touches the bottom or top   
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS - 1:
         ball_vel[1] = -ball_vel[1]
      
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, 'White', 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos > HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    elif paddle1_pos < HALF_PAD_HEIGHT:
        paddle1_pos = HALF_PAD_HEIGHT
    else:
        paddle1_pos += paddle1_vel

    if paddle2_pos > HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
    elif paddle2_pos < HALF_PAD_HEIGHT:
        paddle2_pos = HALF_PAD_HEIGHT
    else:
        paddle2_pos += paddle2_vel
 
    # draw paddles    
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], [HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], PAD_WIDTH, "White")
   
    # draw scores
    canvas.draw_text(str(score1), (WIDTH/4, HEIGHT/5), 40, "White")
    canvas.draw_text(str(score2), (WIDTH/4*3, HEIGHT/5), 40, "White")

    
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 6
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel -= acc
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += acc
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel -= acc
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel += acc
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w'] or key == simplegui.KEY_MAP['s']: 
        paddle1_vel = 0
    
    if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
def reset():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Reset', reset, 100)

# start frame

frame.start()
new_game()
