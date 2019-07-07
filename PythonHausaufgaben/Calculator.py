print(" Welcome to your Calculator")


x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))

operation = input("Choose an operator. Your can choose + - or *")

if operation == "+":
    print(x + y)

elif operation == "-":
    print(x - y)

elif operation == "*":
    print(x * y)

else:
    print("This was not correct! Try it again.")


