# *args allows you to pass an arbitrary number of arguments to that function
# the arguments are then accessible as the tuple args in the body of the function

def function(named_arg, *args):
    print(named_arg)
    print(args)

function(1,2,3,4,5)

#change the function
def adder(x, *args):
    print(x+sum(args))

adder(2, 3)
adder(2, 3, 4)
adder(1, 2, 3, 4, 5)

# using default values, i.e. food = spam
# if the argument does not pass, the default value is used
def function(x, y, food="spam"):
    print(food)

function(1, 2)
function(3, 4, "egg")

# kwargs = key word arguments
# returns a diciontary with keys for argument names like a : 7, b : 8
def my_func(x, y=7, *args, **kwargs):
    print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)