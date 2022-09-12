import turtle

cdegree = 360
side = int(input("How many sides should the shape have: "))
length = int(input("What is the length of each side: "))
myturtle = turtle.Turtle()
myturtle.color("blue")
myturtle.shape("turtle")

for i in [0]*side:
  myturtle.left(cdegree / side)
  myturtle.forward(length)

window = turtle.Screen()
window.exitonclick()




