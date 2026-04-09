import turtle
turtle.Screen().bgcolor("purple")
turtle.Screen().setup(50,50)
polygon = turtle.Turtle()

num_sides = 4
side_length = 10
angle = 360.0 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()