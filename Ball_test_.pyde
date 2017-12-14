x = 100
y = 0
px = 300
py = 300
speed = 4
def setup():
    size(600,600)
    
def draw():
    global x
    global y
    global px
    global py
    global speed
    y += speed 
    background(255)
    ellipse(x,y,70,70)
    
    ellipse(px,py,70,70)
    
    if x >= 600:
        speed = -speed
    elif x <= 0:
        speed = -speed
    elif y >= 600:
        speed = -speed
    elif y <= 0:
        speed = -speed