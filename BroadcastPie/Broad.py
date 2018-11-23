import time
from sense_hat import SenseHat
from socket import *
from datetime import datetime

sense = SenseHat()
sense.clear()

temp = sense.get_temperature()

s = socket(AF_INET, SOCK_DGRAM)
#s.bind(('', 6969))  #(ip,port)

s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
while True:
    data = "Current temperature " + str(temp)
    s.sendto(bytes(data), ('<broadcast>', 6969))
    print(data)
    time.sleep(1)