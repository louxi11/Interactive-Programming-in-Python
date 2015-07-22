#! /usr/bin/env python
#coding=utf-8
# template for "Stopwatch: The Game"
import simplegui

# define global variables
t = 0
interval = 100
count = 0
wins = 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t //600
    B = t % 600 // 100
    C = t % 600 % 100 /10
    D = t % 10
    return str(A)+":"+str(B)+str(C)+"."+str(D)
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():    
    timer.start() 

def Stop():
    global t,count,wins
    if not timer.is_running():  
        return  
    timer.stop()
    count += 1    
    if t % 10 == 0:
        wins += 1
    
    
def Reset():
    global t,count,wins
    t = 0
    count = 0
    wins  = 0
    if not timer.is_running():  
        return 
    timer.stop()  
    
    

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t+=1
    


# define draw handler 
def draw(canvas):
    canvas.draw_text(format(t), [100,100],30,"Red") 
    canvas.draw_text(str(wins) + '/' + str(count), (250, 20), 20, 'white')
    
# create frame
f = simplegui.create_frame("Stopwatch: The Game",300,200)

# register event handlers
f.add_button("Start", Start,200)
f.add_button("Stop",Stop, 200)
f.add_button("Reset",Reset, 200)
f.set_draw_handler(draw)

timer = simplegui.create_timer(interval,timer_handler)

# start frame
f.start()

# Please remember to review the grading rubric
