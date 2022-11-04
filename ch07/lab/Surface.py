from Rectangle import Rectangle


class Surface:
  def __init__(self, myimage, x, y, height, width):
    self.rect = Rectangle(x, y, height, width)
    self.image = str(myimage)

  def getRect(self):
    '''
    Create rectangle object with specific values

    myimage(str): the image of the rectangle
    x(int): the x coordinate of the rectangles upper left position
    y(int): the y coordinate of the rectangles upper left position
    height(int): the height of the rectangle
    width(int): the width of the rectangle
    
    return(str): rectangle object with x, y, height, and width
    '''
    return self.rect
