import turtle
import random 

x=500
y=500
myturtle = turtle.Turtle()
window = turtle.Screen()
turtle.screensize(x, y)
begin_x = x/2
begin_y = y/2

turtle.penup()
turtle.setposition(begin_x, begin_y)



while True:
  flip_coin = random.randrange(0, 2)
  if(flip_coin == 0):
      myturtle.left(90)
      turtle.forward(50)
  elif(flip_coin == 1):
      myturtle.right(90)
      myturtle.forward(50)



    
      


window.exitonclick()

