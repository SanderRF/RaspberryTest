from sense_hat import SenseHat

sense = SenseHat()

red = (255,0,0)

while True:
    acc = sense.get_accelerometer_raw()
    x = acc['x']
    y = acc['y']
    z = acc['z']

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 1 or y > 1 or z > 1:
        sense.show_letter("!", red)
    else:
        sense.clear() 