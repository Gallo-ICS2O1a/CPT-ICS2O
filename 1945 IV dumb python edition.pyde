# make x and y variables for a bullet
# make speed variable for the bullet
# when mousePressed() give the bullet a speed

x = 100
y = 0
px = 300
py = 550
bx = -10
by = -10
ehp = 2
speed = 4
speed2 = -15
def setup():
    size(600,600)
    
def mousePressed():
    global px
    global py
    global bx
    global by
    global speed2
    print("shoot")
    # put location of bullet at the player location
    bx=px
    by=py
    # give the bullet a speed 
    
def draw():
    global x
    global y
    global px
    global py
    global speed
    global bx
    global by
    global speed2
    global ehp
    px = mouseX
    y += speed 
    by += speed2
    
    
    background(255)
    ellipse(x,y,70,70)
    
    ellipse(px,py,70,70)
    
    ellipse(bx,by,5,5)
    
    
    

    
    if x >= 600:
        speed = -speed
    elif x <= 0:
        speed = -speed
    if y >= 600:
        y = 0
        x = random(width)
    

    
