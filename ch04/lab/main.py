import pygame
import random 
import math

pygame.init()

x = 200
y = 200
half_x= x/2
half_y = y/2
screen = (x, y)
center = (half_x, half_y)
radius = half_x 

#colors 
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 225)

msg = "Who do you think will win?"
print(msg)
surface = pygame.display.set_mode(size=screen)
surface.fill(white)
hit_box_width = x / 3
hit_box_height = y / 3 

blue_rect = pygame.Rect(25, 65, hit_box_width, hit_box_height)
red_rect = pygame.Rect(100, 65, hit_box_width, hit_box_height)
blue_button = pygame.draw.rect(surface, blue, blue_rect)
red_button = pygame.draw.rect(surface, red, red_rect)
pygame.display.flip

no_click = True
will_win = ""

while no_click:
  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_click_pos = event.pos
      if red_button.collidepoint(mouse_click_pos):
        no_click = False
        surface.fill(white)
        pygame.display.flip
        will_win = "Red"
      elif blue_button.collidepoint(mouse_click_pos):
        no_click = False
        surface.fill(white)
        pygame.display.flip
        will_win = "Blue"


#draws the dart board
pygame.draw.circle(surface, black, center, radius)
pygame.draw.line(surface, white, (0, 100), (200, 100))
pygame.draw.line(surface, white, (100, 0), (100, 200))
pygame.display.flip()




red_count = 0
blue_count = 0
round_count = 10
turn = "Red"

def throw():
  pygame.time.wait(1000)
  rand_x = random.randrange(0, x+1)
  rand_y = random.randrange(0, y+1)
  random_center = (rand_x, rand_y)
  distance_from_center = math.hypot(rand_x-half_x, rand_y-half_y)
  is_in_circle = distance_from_center <= x/2
  if is_in_circle:
    pygame.draw.circle(surface, green, random_center, 4)
    pygame.display.flip()
    return True
  else:
    pygame.draw.circle(surface, red, random_center, 4)
    pygame.display.flip()
    return False

for i in range(2 * round_count):
  hit = throw()
  if (turn=="Red" and hit):
    print("Red hits, +1")  
    red_count += 1
  elif (turn=="Blue" and hit):
    print("Blue hits, +1")
    blue_count += 1
  else:
    if (turn=="Red"):
      print("Red missed")
    else:
      print("Blue missed")

  if (turn=="Red"):
    turn = "Blue"
  else:
    turn = "Red"

if red_count > blue_count:
  print("Red wins, " + str(red_count))
  final_answer_red = "Red"
  if will_win==final_answer_red:
    print("You guessed right!")
  else:
    print("You guessed wrong!")
elif blue_count > red_count: 
  print("Blue wins, " + str(blue_count))
  final_answer_blue = "Blue"
  if will_win==final_answer_blue:
    print("You guessed right!")
  else:
    print("You guessed wrong!")
else:
  print("You tied!")
  print("The score was" ,str(red_count))
  print("You guessed wrong!")


