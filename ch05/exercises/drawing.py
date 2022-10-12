import turtle

def drawEqShape(myTurtle=None, num_sides=0, side_length=0):
  for i in range(num_sides):
    myTurtle.forward(side_length)
    myTurtle.left(360/num_sides)

Jen = turtle.Turtle()
Jen.shape("turtle")
Jen.color("green")
num_sides = int(input("How many sides do you want? "))
side_length = int(input("How long do you want the sides to be? "))
drawEqShape(Jen, num_sides, side_length)

    
  