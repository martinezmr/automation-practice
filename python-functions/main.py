def function():
    print("This is a module function")

if __name__=="__main__":
    print("This is a script")


# the if statement will print if the function IS NOT imported
# the else statement will print if the function IS imported

if __name__ == "__main__":
    print("Hi")
else:
    print("Welcome")