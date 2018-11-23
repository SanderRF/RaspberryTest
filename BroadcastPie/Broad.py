import time
from sense_hat import SenseHat
from socket import *
from datetime import datetime

s = socket(AF_INET, SOCK_DGRAM)
#s.bind(('', 6969))  #(ip,port)

s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
while True:
    data = "Current time" + str(datetime.now())
    s.sendto(bytes(data,"UTF-8"), ('<broadcast>', 6969))
    print(data)
    time.sleep(1)