from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

c = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
aqua = (0,255,255)
x = 1
y = 0

x1 = 2
y1 = 1
i1 = 0

x2 = 3
y2 = 2
i2 = 0

l = 0
i = 0

c = red

while(l<48):

  if(i<24):
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

  if(i1<16):
    time.sleep(0.05)
    sense.set_pixel(x1,y1,c)
    if x1 < 6 and y1 == 1:
      x1 += 1
    if x1 == 6 and y1 < 6:
      y1 += 1
    if y1 == 6 and x1 > 1:
      x1 -= 1
    if x1 == 1 and y1 > 1:
      y1 -= 1
    i1 += 1
  
  if(i2<8):
    time.sleep(0.05)
    sense.set_pixel(x2,y2,c)
    if x2 < 5 and y2 == 2:
      x2 += 1
    if x2 == 5 and y2 < 5:
      y2 += 1
    if y2 == 5 and x2 > 2:
      x2 -= 1
    if x2 == 2 and y2 > 2:
      y2 -= 1
    i2 += 1

    l += 1

print("done")
time.sleep(3)
sense.clear()