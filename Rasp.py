from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

c = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

x = 1
y = 0

l = 0
i = 0

c = white

while(l<10):
  print("run: " + str(l+1))
  while(i<24):
    time.sleep(0.05)
    sense.set_pixel(x,y,c)
    if x < 7 and y == 0:
      x += 1
    if x == 7 and y < 7:
      y += 1
    if y == 7 and x > 0:
      x -= 1
    if x == 0 and y > 0:
      y -= 1
    i += 1
  time.sleep(0.1)
  l += 1
  i = 0
  x = 1
  y = 0
  if c == red:
    c = white
  if c == green:
    c = red
  if c == blue:
    c = green
  if c==white:
    c = blue
  sense.clear()

print("done")
time.sleep(5)
sense.clear()
  
