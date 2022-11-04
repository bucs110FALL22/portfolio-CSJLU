from Rectangle import Rectangle


class Surface:
  def __init__(self, myimage, x, y, height, width):
    self.rect = Rectangle(x, y, height, width)
    self.image = str(myimage)
    '''
    Creates a surface with five different variables
    
    myimage(str): the image of the surface (file name)
    x(int): the x coordinate of the surface
    y(int): the y coordinate of the surface
    height(int): the height of the surface
    width(int): the width of the surface
    '''
  
  def getRect(self):
    '''
    Create rectangle object with surface variables
    
    return(str): rectangle object with x, y, height, and width
    '''
    return self.rect
