from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=500,height=400)
colors=["violet","blue","green","yellow","orange","red"]
user_input=screen.textinput(title="make a bet",prompt="guess who will win the race?""\n""violet"" blue"" green""\n""yellow"" orange"" red")
y=[-70,-40,-10,20,50,80]
list_turtles=[]
for i in range(6):
    tim=Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230,y=y[i])
    list_turtles.append(tim)
if user_input:
    end=True
while end==True:
    for turtle in list_turtles:
        move=random.randint(0,9)
        turtle.forward(move)
        if turtle.xcor()>230:
            winner=turtle.pencolor()
            if winner==user_input:
                print(f'\nyou won!the {winner} turtle is the winnner')
                end=False
            else:
                print(f'\nyou lost!the {winner} turtle is the winnner')
                end=False








# names=['a','b','c','d','e','f']
# all=[]
# y=[-100,-60,-20,20,60,100]
# def turtle_name():
#     x=0
#     for i in names:
#         i=Turtle(shape='turtle')
#         i.color(colors[x])
#         i.penup()
#         i.goto(x=-230, y=y[x])
#         all.append(i)
#         x=x+1
#
# turtle_name()
# print(all)
# if user_input:
#     end=True
#
# while end==True:
#     for turtle in all:
#         move=random.randint(0,9)
#         turtle.forward(move)
#         if turtle.xcor()>230:
#             winner=turtle.color
#             if winner==user_input:
#                 print(f'you won!the {winner} turtle is the winnner')
#                 end=False
#             else:
#                 print(f'you lost!the {winner} turtle is the winnner')
#                 end=False
#



