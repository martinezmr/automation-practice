# def apply_twice(func, arg):
#     return func(func(arg))

# def add_five(x):
#     return x + 5

# print(apply_twice(add_five, 10))

# # multiplies everything three times = 16
# def test(func, arg):
#     return func(func(arg))
# def mult(x):
#     return x*x
# print(test(mult,2))


def my_func(f, arg):
    return f(arg)
    
print(my_func(lambda x: 2*x*x, 5))


#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))


print('\nlamba\n')

price = 50
perc = 10

res = (lambda x,y:x/y)(price,perc)

print(res)






