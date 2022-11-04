class Rectangle:
  def __init__(self, x, y, height, width):
    if x<0:
      x=0
    if y<0:
      y=0
    if height<0:
      height = 0
    if width<0:
      width = 0
    self.x = x
    self.y = y
    self.height = height
    self.width = width
    
    
  def __str__(self):
    '''
    Organize specific values of the rectangle 
    
    x(int): the x coordinate of the rectangles upper left position
    y(int): the y coordinate of the rectangles upper left position
    height(int): the height of the rectangle
    width(int): the width of the rectangle

    return(int): x, y, width, and height of the rectangle in a specific format
    '''
    return f"({self.x} : {self.y})width:{self.width}, height:{self.height}"
