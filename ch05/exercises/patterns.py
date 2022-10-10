def star_pyramid():
  print("How many rows do you want")
  rows = int(input(""))
  for i in range(1, rows + 1):
    print("*" * i)
    
star_pyramid()


def rstar_pyramid():
  print("How many rows do you want")
  rows = int(input(""))
  for i in range(1, rows + 1):
    print("*" * rows)
    rows -= 1

rstar_pyramid()