import turtle

window = turtle.Screen()
myPen = turtle.Turtle()
myPen.shape("arrow")
myPen.color("blue")


def askUser():
  notAnswered = True
  while notAnswered:
    question = int(input("Choose number 5 or 15 to see something interested(try out both numbers):  "))
    if question==5:
      return 5
    elif question==15:
      return 15
    else: 
      print("You did not choose 5 or 15. Try again.")
      
answer = askUser()

  
def askUserShape():
  notAnswered = True
  while notAnswered:
    question = int(input("Choose a shape from 5-10 (5=Pentagon, 6=Hexagon, 7=Septagon, 8=Octagon, 9=Nonagon, 10=Decagon): "))
    if question==5:
      return 5
    elif question==6:
      return 6
    elif question==7:
      return 7
    elif question==8:
      return 8
    elif question==9:
      return 9
    elif question==10:
      return 10
    else: 
      print("You did not choose between 5 and 10. Try again.")
      
shapeAnswer = askUserShape()


def changePos(offset):
  degrees = 45
  myPen.up()
  myPen.right(degrees)
  myPen.forward(offset)
  myPen.left(degrees)
  myPen.forward(offset)


def drawHexa(num, sides, length):
  circleDegrees = 360
  for i in range(num):
    myPen.down()
    for i in range(sides):
      myPen.left(circleDegrees/sides)      
      myPen.forward(length) 
    changePos(answer)
    length = length + 10


def main():
  turtle.screensize(1000, 1000)
  answer
  shapeAnswer
  drawHexa(8, shapeAnswer, 25)
  window.exitonclick()
  
main()

