from sense_hat import SenseHat
import time
import threading

sense = SenseHat()
sense.clear()

g = (0,100,0)
b = (0,0,100)
w = (0,0,0)
r = (100,0,0)

temp = sense.get_temperature()
print(temp)

sense.show_message(str(temp)