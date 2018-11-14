from sense_hat import sense_hat
import time
sense = sense_hat()

x = 3
y = 3

def draw_ball():
    sense.clear()
    sense.set_pixel(x,y,255,90,90)

def push_up():
    global y
    y -= 1
    if y < 0:
        y = 0
    draw_ball()

def push_down():
    global y
    y += 1
    if y > 7:
        y = 7
    draw_ball()

def push_left():
    global x
    x -= 1
    if x < 0:
        x = 0
    draw_ball()

def push_right():
    global x
    x += 1
    if x > 7:
        x = 7
    draw_ball()

sense.stick.direction_up = push_up
sense.stick.direction_down = push_down
sense.stick.direction_left = push_left
sense.stick.direction_right = push_right

draw_ball()