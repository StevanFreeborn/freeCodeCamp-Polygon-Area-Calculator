class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2 * self.width) + (2 * self.height)

  def get_diagonal(self):
    return ((self.width ** 2) + (self.height ** 2)) ** 0.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."

    picture = ""
    
    for i in range(self.height):
      inner_range = range(self.width)
      for j in inner_range:
        if j == inner_range[-1]:
          picture += "*\n"
        else:
          picture += "*"

    return picture
  
  def get_amount_inside(self, other_shape):
    return int(self.get_area() / other_shape.get_area())

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
  def __init__(self, side_length):
    super().__init__(side_length, side_length)

  def set_width(self, width):
    self.height = width
    self.width = width

  def set_height(self, height):
    self.height = height
    self.width = width
  
  def set_side(self, side_length):
    self.height = side_length
    self.width = side_length
    
  def __str__(self):
    return f'Square(side={self.width})'
