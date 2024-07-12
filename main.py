from turtle import Turtle,Screen
tim=Turtle()
screen=Screen()
tim.color("green")
def forward():
    tim.forward(15)
def backward():
    tim.backward(15)
def left():
    tim.left(10)
def right():
    tim.right(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen.listen()
screen.onkey(forward,"w")
screen.onkey(backward,"s")
screen.onkey(left,"a")
screen.onkey(right,"d")
screen.onkey(clear,"c")
screen.exitonclick()