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

###
class Student:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(self.name+" says hi")

obj = Student("John")
obj.greet()
####
class Dog:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def bark(self):
    print("Woof!")

fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()
####
class Dog:
    legs = 4
    def __init__(self, name, color):
        self.name = name
        self.color = color

fido = Dog("Fido", "brown")
print(fido.legs)
print(Dog.legs)
####