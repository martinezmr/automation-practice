# uses if / else statements as a conditional expression
# called ternary because it takes three arguments 

a = 7
b = 1 if a >= 5 else 42
print(b)

status  = 1
msg = "Logout" if status == 1 else "Login"
print(msg)

balance = int(input())
to_cash = int(input())
money_left = balance-to_cash if to_cash<=balance and to_cash >= 500 else "Error"
print(money_left)