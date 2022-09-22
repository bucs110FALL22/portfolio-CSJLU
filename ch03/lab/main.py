import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
x = random.randrange(1, 101)
michelangelo.forward(x)
leonardo.forward(x)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

x2 = random.randrange(0, 11)
x3 = random.randrange(0, 11)
for i in range(10):
  michelangelo.forward(x2)
  leonardo.forward(x3)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

  
# PART B - complete part B here
pygame.init()

window = pygame.display.set_mode((500, 800))
color = (0, 0, 0)
shapecolor = (255, 255, 255)
window.fill(color)
pygame.display.flip()
offset = 100

class etriangle:
  num_sides = 3
  side_length = 35
  coords = []
  
for i in range(3):
  theta = (2.0 * math.pi * i / etriangle.num_sides)
  x = etriangle.side_length * math.cos(theta) + offset
  y = etriangle.side_length * math.sin(theta) + offset 
  etriangle.coords.append((x, y))

pygame.draw.polygon(window, shapecolor, etriangle.coords)
pygame.display.flip()
pygame.time.wait(500)
window.fill(color)
pygame.display.flip()

class square:
  num_sides = 4
  side_length = 35
  coords = []

for i in range(4):
  theta = (2.0 * math.pi * i / square.num_sides)
  x = square.side_length * math.cos(theta) + offset
  y = square.side_length * math.sin(theta) + offset 
  square.coords.append((x, y))

pygame.draw.polygon(window, shapecolor, square.coords)
pygame.display.flip()
pygame.time.wait(500)
window.fill(color)
pygame.display.flip()

class hexagon:
  num_sides = 6
  side_length = 35
  coords = []

for i in range(6):
  theta = (2.0 * math.pi * i / hexagon.num_sides)
  x = hexagon.side_length * math.cos(theta) + offset
  y = hexagon.side_length * math.sin(theta) + offset 
  hexagon.coords.append((x, y))

pygame.draw.polygon(window, shapecolor, hexagon.coords)
pygame.display.flip()
pygame.time.wait(500)
window.fill(color)
pygame.display.flip()

class nonagon:
  num_sides = 9
  side_length = 35
  coords = []

for i in range(9):
  theta = (2.0 * math.pi * i / nonagon.num_sides)
  x = nonagon.side_length * math.cos(theta) + offset
  y = nonagon.side_length * math.sin(theta) + offset 
  nonagon.coords.append((x, y))

pygame.draw.polygon(window, shapecolor, nonagon.coords)
pygame.display.flip()
pygame.time.wait(500)
window.fill(color)
pygame.display.flip()

class circle:
  num_sides = 360
  side_length = 35
  coords = []

for i in range(360):
  theta = (2.0 * math.pi * i / circle.num_sides)
  x = circle.side_length * math.cos(theta) + offset
  y = circle.side_length * math.sin(theta) + offset 
  circle.coords.append((x, y))

pygame.draw.polygon(window, shapecolor, circle.coords)
pygame.display.flip()
pygame.time.wait(500)
window.fill(color)
pygame.display.flip()

#test (don't mind this comment)









