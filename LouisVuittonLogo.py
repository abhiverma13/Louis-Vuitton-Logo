import turtle
def draw_logo(window,x,y,scale=1,angle=0): #the default values for scale and angle
    window.window_height() #height
    window.window_width() #width
    turt=turtle.Turtle() #sets up turtle
    turt.hideturtle()
    turt.shape('turtle')
    turt.color('black')
    turt.speed(0)
    turt.penup()
    turt.goto(x,y) #goto function to move turtle to starting position from function parameters
    turt.pendown()
    turt.lt(angle)#draws logo at angle if angle parameter is given
    turt.fillcolor("red")
    turt.begin_fill() #drawing V shape
    turt.fd(50*scale)
    turt.rt(90)
    turt.fd(12*scale)
    turt.rt(90)
    turt.fd(10*scale)
    turt.lt(115)
    turt.fd(100*scale)
    turt.lt(130)
    turt.fd(105*scale)
    turt.lt(115)
    turt.fd(15*scale)
    turt.rt(90)
    turt.fd(12*scale)
    turt.rt(90)
    turt.fd(45*scale)
    turt.rt(90)
    turt.fd(12*scale)
    turt.rt(90)
    turt.fd(15*scale)
    turt.lt(65)
    turt.fd(135*scale)
    turt.rt(65)
    turt.fd(15*scale)
    turt.rt(65)
    turt.fd(131*scale)
    turt.lt(65)
    turt.fd(15*scale)
    turt.rt(90)
    turt.fd(12*scale)
    turt.rt(90)
    turt.end_fill()
    turt.penup() #repositioning
    turt.fd(60*scale)
    turt.rt(90)
    turt.fd(20*scale)
    turt.lt(90)
    turt.pendown()
    turt.begin_fill() #drawing L shape
    turt.fd(45*scale)
    turt.rt(90)
    turt.fd(10*scale)
    turt.rt(90)
    turt.fd(10*scale)
    turt.lt(65)
    turt.fd(125*scale)
    turt.lt(115)
    turt.fd(70*scale)
    for i in range(10):
        turt.lt(6)
        turt.fd(6*scale)
    turt.lt(10)
    turt.fd(10*scale)
    turt.rt(70)
    turt.fd(12*scale)
    turt.rt(115)
    turt.fd(55*scale)
    turt.rt(65)
    turt.fd(160*scale)
    turt.rt(90)
    turt.fd(10*scale)
    turt.rt(90)
    turt.fd(8*scale)
    for i in range(8):
        turt.lt(4)
        turt.fd(2*scale)
    turt.lt(33)
    turt.fd(120*scale)
    turt.lt(115)
    turt.fd(11*scale)
    turt.rt(90)
    turt.fd(10*scale)
    turt.rt(90)
    turt.end_fill()
    turt.penup() #repositioning
    turt.fd(90*scale)
    turt.rt(90)
    turt.fd(30*scale)
    turt.lt(90)
    turt.pendown()
    turt.fillcolor("red")
    turt.begin_fill() #drawing first star
    turt.lt(15)
    for i in range(4):
        turt.fd(15*scale)
        turt.lt(60)
        turt.fd(15*scale)
        turt.rt(150)
    turt.end_fill()
    turt.penup()
    turt.rt(25)
    turt.fd(18*scale)
    turt.pendown()
    turt.fillcolor("white")
    turt.begin_fill()
    turt.circle(3*scale)
    turt.lt(12)
    turt.end_fill()
    turt.penup() #repositioning
    turt.bk(165*scale)
    turt.rt(90)
    turt.fd(15*scale)
    turt.pendown()
    turt.fillcolor("red")
    turt.begin_fill() #drawing second star
    turt.lt(45)
    for i in range(4):
        turt.fd(25*scale)
        turt.rt(90)
    turt.end_fill()
    turt.fillcolor("white")
    turt.rt(45)
    turt.begin_fill()
    turt.lt(15)
    for i in range(4):
        turt.fd(15 * scale)
        turt.lt(60)
        turt.fd(15 * scale)
        turt.rt(150)
    turt.end_fill()
    turt.penup()
    turt.rt(25)
    turt.fd(18 * scale)
    turt.pendown()
    turt.fillcolor("red")
    turt.begin_fill()
    turt.circle(3 * scale)
    turt.lt(12)
    turt.end_fill()














