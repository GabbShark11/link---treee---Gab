import turtle

t = turtle.Turtle()

t.pen(fillcolor = "yellow", pencolor = "yellow")
t.speed("fast")
t.begin_fill()
for i in range(7):
    h = t.heading()
    t.circle(200,60)
    t.left(120)
    t.circle(200,60)
    t.setheading(h)
    t.left(360/7)
t.end_fill()

t.hideturtle()
t.penup()
t.goto(0, -30)
t.showturtle()
t.pendown()
t.pen(fillcolor = "red", pencolor = "red")
t.begin_fill()
t.circle(30)
t.end_fill()

t.hideturtle()
t.penup()
t.goto(0, -20)
t.showturtle()
t.pendown()
t.pen(fillcolor = "purple", pencolor = "purple")
t.begin_fill()
t.circle(20)
t.end_fill()


t.screen.exitonclick()
