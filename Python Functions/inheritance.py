class Animal: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal):
    def purr(self):
        print("Purr...")
        
class Dog(Animal):
    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()
###
class Wolf: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")

class Dog(Wolf):
    def bark(self):
        print("Woof")

# inheritance on inheritance
class A:
    def method(self):
        print("A method")
    
class B(A):
    def another_method(self):
        print("B method")
    
class C(B):
    def third_method(self):
        print("C method")
    
c = C()
c.method()
c.another_method()
c.third_method()

husky = Dog("Max", "grey")
husky.bark()

###
class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()

###
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def __add__(self, otherbalance):
        return BankAccount(self.balance + otherbalance.balance)
        

a = BankAccount(1024)
b = BankAccount(42)

result = a + b
print(result.balance)