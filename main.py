import turtle
length1 =  200
turtle.left(180)
for i in range(6):
    length1 = length1 - 30
    for i in range(2):
        turtle.forward(length1)
        turtle.left(90)
turtle.exitonclick()