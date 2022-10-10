import turtle
import random 

#x=500
#y=500
myturtle = turtle.Turtle()
wn = turtle.Screen()
#turtle.screensize(x, y)
distance = 10
angle = 90
is_in_screen = True


while is_in_screen:
  flip_coin = random.randrange(0, 2)
  if(flip_coin == 0):
      myturtle.left(angle)
  else:
      myturtle.right(angle) 
  myturtle.forward(distance)

  turtle_x = myturtle.xcor()
  turtle_y = myturtle.ycor()

  x_range = wn.window_width()/2
  y_range = wn.window_height()/2
      
  if abs(turtle_x) > x_range or abs(turtle_y) > y_range:
    is_in_screen = False

wn.exitonclick()

