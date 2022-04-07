import turtle

turtle.speed("fast")
turtle.bgcolor('black')
turtle.pensize(3)
def func():
    for i in range(400):
       turtle.right(1)
       turtle.forward(1)
turtle.color('red', 'pink') 
turtle.begin_fill()
turtle.left(120)
turtle.forward(50.4)
func()
turtle.left(120)
func()
turtle.forward(50.4)
turtle.end_fill()
turtle.hideturtle()
turtle.done()