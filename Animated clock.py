import turtle
screen=turtle.Screen()
turt=turtle.Turtle()
screen.setup(700,700)
screen.bgcolor('black')
turt.pensize(4)
turt.shape('turtle')
turt.penup()
turt.pencolor('orange')
m=0
for i in range(12):
    m=m+1
    turt.penup()
    turt.setheading(-30*i+60)
    turt.forward(150)
    turt.pendown()
    turt.forward(25)
    turt.penup()
    turt.forward(20)
    turt.write(str(m),align="center",font=("Arial",12,"normal"))
    if m==12:
        m=0
    turt.home()
turt.home()
turt.setpos(0,-250)
turt.pendown()
turt.pensize(10)
turt.pencolor('yellow')
turt.circle(260)
turt.penup()
turt.setpos(150,-270)
turt.pendown()
turt.pencolor('olive')
turt.write('Xcode Emulators',font=("calibri",18,"normal"))
turt.ht()    