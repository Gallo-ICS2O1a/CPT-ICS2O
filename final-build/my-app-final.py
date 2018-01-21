# Rename this file to include the name of your application
# Replace this code with your application's code
# make x and y variables for a bullet
# make speed variable for the bullet
# when mousePressed() give the bullet a speed

x = 100
y = 0
bossx = 100
bossy = 0
bosshp = 200
bossbx = 300
bossby = -10
px = 300
py = 550
bx = -10
by = -10
ebx = 10
eby = 10
speed = 4
speed2 = -15
speed3 = 10
speed4 = 12
score = 0
win = 0
hp = 70
lose = 0
primary_color = color(96, 150, 186)
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
    global bosshp
    global score
    global ebx
    global eby
    global speed3
    global hp
    global lose
    global bossx
    global bossy
    global bossbx
    global bossby
    global win
    px = mouseX
    y += speed 
    by += speed2
    ebx = x
    eby += speed3
    bossx = mouseX
    bossby += speed4
    a=bx-x
    b=by-y
    c=ebx-px
    d=eby-py
    e=bx-bossx
    f=by-bossy
    g=bossbx-px
    h=bossby-py
    dist=sqrt(a**2+b**2)
    if dist < 35:
        score += 1
        y = 600
    dist=sqrt(e**2+f**2)
    if dist < 70:
        bosshp -= 1
    dist=sqrt(c**2+d**2)
    if dist < 8:
        hp -= 1
    dist=sqrt(g**2+h**2)
    if dist < 30:
        hp -= 1
        
    background(255)
    fill(40,40,40)
    textSize(32)
    text(score,50,50)
    fill(40,40,40)
    textSize(32)
    text(hp,550,50)
    

    
    
    ellipse(px,py,70,70)
    
    ellipse(bx,by,5,5)
    
    
    
    
    
  
    ellipse(x,y,70,70)
    
    ellipse(ebx,eby,16,16)

    
    
    
    if eby >= 600:
        eby = y
    
    if x >= 600:
        speed = -speed
    elif x <= 0:
        speed = -speed
    if y >= 600:
        y = 0
        x = random(width)
    


     
    if hp <= 1:
       lose =+ 1
      
    if lose >= 1:
       background(primary_color)
       fill(40,40,40)
       textSize(32)  
       text("GAME OVER NOOB!!!!",300,300)
    
    if score >= 10:
        ellipse(bossx,bossy,140,140)
        ellipse(bossbx,bossby,60,60)
        fill(70,10,20)
        textSize(32)  
        text(bosshp,300,100)
        fill(90,20,10)
        textSize(32)  
        text("kill that god damn freaking fat boss!!!!",300,500)

    if bossby >= 600:
        bossby = bossy  
        bossbx = random(width) 
     
    if bosshp <= 0:
       win =+ 1      
    if win >= 1:
       background(primary_color)
       fill(40,40,40)
       textSize(30)  
       text("Game Clear!",300,300)
