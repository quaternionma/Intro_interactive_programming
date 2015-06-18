# template for "Stopwatch: The Game"
import simplegui
# define global variables
time = 0

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
    canvas.draw_text(time_canvas, (140, 110), 32, 'White')
    
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 200)

# register event handlers
frame.set_draw_handler(draw_time)
button_start = frame.add_button('START', start, 100)
button_stop = frame.add_button('STOP', stop, 100)
button_reset = frame.add_button('RESET', reset, 100)
# create a timer with 100 ms interval
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()
timer.start()

# Please remember to review the grading rubric
