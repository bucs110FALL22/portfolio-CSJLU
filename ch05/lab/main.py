import pygame

count = 0
upper_limit = 20
iters = {}
max_so_far = count
black = (0, 0, 0)

for start in range(2, upper_limit + 1):
  n = start
  while (n != 1):
    count += 1
    if (n % 2 == 0):
      n = n // 2
    else:
      n = n*3 + 1
  iters[start]=count
  count = 0
print(iters)

display = pygame.display.set_mode()
coordinates = iters.items()
pygame.draw.lines(display, black, False, coordinates)
new_display = pygame.transform.flip(display, False, True)
display.blit(new_display, 0, 0)
font = pygame.font.Font(None, 12)
max_msg = "Your current max iteration is, " + max_so_far
msg = font.render()
