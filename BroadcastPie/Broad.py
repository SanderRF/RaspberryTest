from sense_hat import SenseHat
import time
from socket import *
from datetime import datetime

s = socket(AF_INET, SOCK_DGRAM)
sense = SenseHat()

s.bind ('',6969)

s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
while True:
	data = "Current time " + str(datetime.now())
	s.sendto(bytes(data, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
	print(data)
    time.sleep(1)