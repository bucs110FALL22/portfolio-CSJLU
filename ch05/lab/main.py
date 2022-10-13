import pygame
pygame.init()

count = 0
upper_limit = 20
iters = {}
coords = {}
white = (255, 255, 255)
black = (0, 0, 0)
scale = 9
max_so_far = 0
font = pygame.font.Font(None, 25)
display = pygame.display.set_mode((500, 500))
graph_display = pygame.Surface((500, 200))
graph_display.fill(white)
display.fill(white)
new_display = pygame.transform.flip(display, False, True)
display.blit(new_display, (0, 0))


for start in range(2, upper_limit + 1):
  n = start
  while (n != 1):
    count += 1
    if (n % 2 == 0):
      n = n // 2
    else:
      n = n*3 + 1
  iters[start]=count
  coords[start*scale]=count*scale
  coordinates = list(coords.items())
  if (len(coordinates) >= 2):
    pygame.draw.lines(graph_display, black, False, coordinates)
    new_graph_display = pygame.transform.flip(graph_display, False, True)
    display.blit(new_graph_display, (0, 0))
  if (count > max_so_far):
      max_so_far = count
      text = "Your max so far is " + str(max_so_far)
      msg = font.render(text, True, black)
      display.blit(msg, (0, 0))
      pygame.display.flip()
  count = 0
  pygame.time.wait(500)
print(iters)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()




