# implementation of card game - Memory

import simplegui
import random
cards_deck = []
exposed = []
previous, current, turns = 0, 0, 0
# helper function to initialize globals
def new_game():
    global cards_deck, exposed, state, turns
    state, turns = 0, 0 
    exposed = []
    for num in range(16):
        cards_deck.append( num % 8 )  
        exposed.append(False)
        
    random.shuffle(cards_deck) 
    label.set_text("Turns = " + str(turns))

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, state, previous, current, turns         
    click = pos[0]//50 
    #click on a card, the card is exposed, and switch to state 1
    if state == 0:
        state = 1
        previous = click
        exposed[previous] = True
        
    #click on an unexposed card, the card is exposed and switch to state 2    
    elif state == 1:
        if not exposed[click]:                       
            current = click
            exposed[current] = True         
            state = 2
            turns += 1
    else:
        #determine if the previous two cards are paired or unpaired
        if not exposed[click]:
            if cards_deck[current]!= cards_deck[previous]:
                exposed[current], exposed[previous] = False, False                
            
            previous = click            
            exposed[previous] = True
            state = 1
            
    label.set_text("Turns = " + str(turns))
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards_deck, exposed
    for num in range(16):
        if exposed[num]: 
            canvas.draw_text(str(cards_deck[num]), (50*num+15, 60), 50, 'White')
        else:    
            canvas.draw_polygon([[num*50, 0],[(num+1)*50, 0],[(num+1)*50, 100], [num*50, 100]], 2,  'Olive','Green')

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
