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
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0.0
paddle2_vel = 0.0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball (direction):
    global ball_pos , ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2 , HEIGHT /2]
    ball_vel = [0.0, 0.0]
    if direction == True :
        ball_vel [0] = random.randrange (120, 240 ) / 60
        ball_vel [1] = 0 - random .randrange(60, 180) / 60
    else:
        ball_vel [0] = 0 - random .randrange(120, 240) / 60
        ball_vel [1] = 0 - random .randrange(60, 180) / 60


# define event handlers
def new_game ():
    global paddle1_pos , paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1 , score2  # these are ints
    spawn_ball(RIGHT )
    score1 = 0
    score2 = 0
    paddle1_pos = HEIGHT / 2.0
    paddle2_pos = HEIGHT / 2.0
def draw (canvas):
    global score1 , score2, paddle1_pos, paddle2_pos , ball_pos, ball_vel
    # Update ball position
    ball_pos[0 ] += ball_vel[0 ]
    ball_pos[1 ] += ball_vel[1 ]
   
    # collide and reflect off of left hand side of canvas
    if ball_pos [0] <= PAD_WIDTH + BALL_RADIUS and ( ball_pos[1 ] <= (paddle1_pos + HALF_PAD_HEIGHT) and ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT):
            ball_vel [0] = - ball_vel [0]
            ball_vel [0] = ball_vel[0 ] + 0.1 *ball_vel[0]
            ball_vel [1] = ball_vel[1 ] + 0.1 *ball_vel[1]
    elif ball_pos [0] <= PAD_WIDTH + BALL_RADIUS :
            spawn_ball (RIGHT)
            score2 += 1
    elif ball_pos [0] >= WIDTH -1 - PAD_WIDTH - BALL_RADIUS and (ball_pos[1] <= ( paddle2_pos + HALF_PAD_HEIGHT ) and ball_pos[1 ] >= (paddle2_pos - HALF_PAD_HEIGHT)):#right wall
            ball_vel [0] = - ball_vel [0]
            ball_vel [0] = ball_vel[0 ] + 0.1 *ball_vel[0]
            ball_vel [1] = ball_vel[1 ] = ball_vel[1 ] + 0.1 *ball_vel[1]
    elif ball_pos [0] >= WIDTH - 1 - PAD_WIDTH - BALL_RADIUS:
            spawn_ball (LEFT)
            score1 += 1
           
    elif ball_pos [1] <= BALL_RADIUS: # ceilling
        ball_vel [1] = - ball_vel [1]
       
    elif ball_pos [1] >= HEIGHT - 1 - BALL_RADIUS: # floor
        ball_vel [1] = - ball_vel [1]
       
    # Draw ball
    canvas.draw_circle (ball_pos, BALL_RADIUS, 2, "Red", "White")
       
    # draw mid line and gutters
    canvas.draw_line ([WIDTH / 2 , 0 ],[WIDTH / 2 , HEIGHT], 1, "White" )
    canvas.draw_line ([PAD_WIDTH, 0],[ PAD_WIDTH, HEIGHT ], 1 , "White" )
    canvas.draw_line ([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
       
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos = paddle1_pos + paddle1_vel
    paddle2_pos = paddle2_pos + paddle2_vel
    # draw paddles
    #left paddle (1)
    if paddle1_pos <= 0 +HALF_PAD_HEIGHT:
        paddle1_pos = 0 + HALF_PAD_HEIGHT
        canvas .draw_line([HALF_PAD_WIDTH,paddle1_pos - HALF_PAD_HEIGHT], [HALF_PAD_WIDTH,paddle1_pos + HALF_PAD_HEIGHT ], PAD_WIDTH, 'Blue')
    elif paddle1_pos >= HEIGHT - 1 - HALF_PAD_HEIGHT :
        paddle1_pos = HEIGHT - 1 - HALF_PAD_HEIGHT
        canvas .draw_line([HALF_PAD_WIDTH,paddle1_pos - HALF_PAD_HEIGHT], [HALF_PAD_WIDTH,paddle1_pos + HALF_PAD_HEIGHT ], PAD_WIDTH, 'Blue')
    else:
        canvas .draw_line([HALF_PAD_WIDTH,paddle1_pos - HALF_PAD_HEIGHT], [HALF_PAD_WIDTH,paddle1_pos + HALF_PAD_HEIGHT ], PAD_WIDTH, 'Blue')
    #right paddle (2)
    if paddle2_pos <= 0 +HALF_PAD_HEIGHT:
        paddle2_pos = 0 + HALF_PAD_HEIGHT
        canvas .draw_line([WIDTH - 1 - HALF_PAD_WIDTH,paddle2_pos - HALF_PAD_HEIGHT], [WIDTH - 1 - HALF_PAD_WIDTH,paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH, 'Blue')
    elif paddle2_pos >= HEIGHT - 1 - HALF_PAD_HEIGHT :
        paddle2_pos = HEIGHT - 1 - HALF_PAD_HEIGHT
        canvas .draw_line([WIDTH - 1 - HALF_PAD_WIDTH,paddle2_pos - HALF_PAD_HEIGHT], [WIDTH - 1 - HALF_PAD_WIDTH,paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH, 'Blue')
    else:
        canvas .draw_line([WIDTH - 1 - HALF_PAD_WIDTH,paddle2_pos - HALF_PAD_HEIGHT], [WIDTH - 1 - HALF_PAD_WIDTH,paddle2_pos + HALF_PAD_HEIGHT ], PAD_WIDTH, 'Blue')
    #draw scores      
    canvas.draw_text (str( score1), (230, 60 ), 30 , "White" )
    canvas.draw_text (str( score2), (350, 60 ), 30 , "White" )
   
def keydown (key):
    global paddle1_vel , paddle2_vel
   
    if key == simplegui.KEY_MAP['w' ]:
        paddle1_vel = - 2.5
    elif key == simplegui.KEY_MAP['s' ]:
        paddle1_vel = 2.5
    elif key == simplegui.KEY_MAP['up' ]:
        paddle2_vel = - 2.5
    elif key == simplegui.KEY_MAP['down' ]:
        paddle2_vel = 2.5

  
def keyup (key):
    global paddle1_vel , paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0


# create frame
frame = simplegui .create_frame("Pong" , WIDTH, HEIGHT)
frame.set_draw_handler (draw)
frame.set_keydown_handler (keydown)
frame.set_keyup_handler (keyup)
frame.add_button ('Reset', new_game)

# start frame
new_game()
frame.start ()
