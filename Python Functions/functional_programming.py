#taking functions in other functions as arguments and returning results
def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))

#example
def test(func, arg):
  return func(func(arg))

def mult(x):
  return x * x

print(test(mult, 2))

#pure function > have no side effects, and return a value that depends only on their arguments
def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)

#impure function
some_list = []

def impure(arg):
  some_list.append(arg)

#lambda functions
def my_func(f, arg):
  return f(arg)

my_func(lambda x: 2*x*x, 5)

#named function comparison with lambda below
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))

#lambda being used as normal functions
double = lambda x: x * 2
print(double(7))