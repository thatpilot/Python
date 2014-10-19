# template for "Stopwatch: The Game"
import simplegui

# define global variables
interval = 100
i = 0
width = 300
height = 200
running = False
position = [width/2,height/2]
y = 0
x = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    time = int(t)
    minutes = time // 600
    seconds = (time - minutes*600) // 10
    tenths = time - minutes*600 - seconds*10
    if seconds == 0:
        return str(minutes)+':'+"00"+'.'+str(tenths)
    elif seconds < 10:
        return str(minutes)+':0'+str(seconds)+'.'+str(tenths)
    else:
        return str(minutes)+':'+str(seconds)+'.'+str(tenths)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()
    global running
    running = True

def stop_handler():
    global running, y, x
    timer.stop()
    if running == True:
        running = False
        if i % 10 == 0:
            x+=1
            y+=1
        else:
            y+=1
    else:
        pass

def reset_handler():
    timer.stop()
    global i, y, x
    i = 0
    x = 0
    y = 0

# define event handler for timer with 0.1 sec interval
def tick ():
    global i
    i += 1
    print i
    

# define draw handler
def draw (canvas):
    global position, x, y
    canvas.draw_text(format(i), position, 36, "Red")
    canvas.draw_text(str(x)+'/'+str(y), [10,30], 36, "White")
    
# create frame
f = simplegui.create_frame("Home", width, height)

# register event handlers
timer = simplegui.create_timer(interval, tick)
button1 = f.add_button('Start', start_handler)
button2 = f.add_button('Stop', stop_handler)
button3 = f.add_button('Reset', reset_handler)
f.set_draw_handler(draw)
# start frame
f.start()



# Please remember to review the grading rubric