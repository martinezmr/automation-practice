#while statments
i = 5
while True:
    if i % 0o11 == 0:
        break
    print(i)
    i += 1

#with input
secret_number = 3
guess = int(input("Guess a number: "))
while guess != secret_number:
    guess = int(input("Wrong, guess again: "))
else:
    print("Congrats pussy")
