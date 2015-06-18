# template for "Stopwatch: The Game"
import simplegui
# define global variables
time = 0
canvas_width = 200
canvas_height = 150

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    timer.stop()
    
def reset():
    global time
    time = 0
    
# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1
#    print time

# define draw handler
def draw_time(canvas):
    global time
    time_canvas = str(time)
    
    # gets the textwidth drawn on the canvas in order to center the text
    textwidth = frame.get_canvas_textwidth(time_canvas, 32, 'sans-serif')
    text_center = textwidth / 2
    
    # draws the text on canvas
    canvas.draw_text(time_canvas, ((canvas_width/2) - text_center, 90), 32, 'White', 'sans-serif')
    
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", canvas_width, canvas_height)

# register event handlers
frame.set_draw_handler(draw_time)
button_start = frame.add_button('START', start, 100)
frame.add_label( "" )
button_stop = frame.add_button('STOP', stop, 100)
frame.add_label( "" )
button_reset = frame.add_button('RESET', reset, 100)
# create a timer with 100 ms interval
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()
#timer.start()

# Please remember to review the grading rubric
