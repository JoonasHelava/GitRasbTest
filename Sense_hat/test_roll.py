from sense_hat import SenseHat
import time

sense = SenseHat()

r = [255,0,0]
o = [255,127,0]
y = [255,255,0]
g = [0,255,0]
b = [0,0,255]
i = [75,0,130]
v = [159,0,255]
e = [0,0,0]

image = [
    y,y,y,b,b,y,y,y,
    y,y,y,b,b,y,y,y,
    y,y,y,b,b,y,y,y,
    y,y,y,b,b,y,y,y,
    y,y,y,b,b,y,y,y,
    y,y,y,y,y,y,y,y,
    y,y,y,b,b,y,y,y,
    y,y,y,b,b,y,y,y
    ]

sense.set_pixels(image)

angles = [0,90,180,270,0,90,180,270]
for r in angles:
    sense.set_rotation(r)
    time.sleep(0.5)
image = [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e
    ]
sense.set_pixels(image)
