#class name is cat
#attributes are color and legs
#__init__ is used when an instance(object) of the class is created using the class name as a function
class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

print(felix.color)
print(rover.color)
print(stumpy.color)