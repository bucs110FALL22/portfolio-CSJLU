import turtle


myturtle = turtle.Turtle()  
angle = 90 
distance = 50 
myturtle.shape("turtle")
myturtle.color("purple")
myturtle.forward(distance)
myturtle.left(angle)
myturtle.down()


for i in [1,2,3]:
  myturtle.forward(distance)
  myturtle.left(angle)

myturtle.up()
myturtle.forward(55)
myturtle.color("red")
myturtle.down()


for i in[1,2,3]:
  myturtle.forward(distance)
  myturtle.left(angle)
myturtle.forward(distance)


window = turtle.Screen()
window.exitonclick()
