from sense_hat import SenseHat
import time
import threading

sense = SenseHat()
sense.clear()

g = (0,255,0)
b = (0,0,255)
w = (0,0,0)
r = (255,0,0)
image = [
w,w,w,w,w,w,w,w,
w,w,w,g,g,w,w,w,
w,w,w,g,g,w,w,w,
w,r,r,r,r,r,r,w,
w,w,w,r,r,w,w,w,
w,w,b,b,b,b,w,w,
w,w,b,w,w,b,w,w,
w,w,w,w,w,w,w,w
]

sense.set_pixels(image)