secret = 34

guess = int(input("Guess the secret number (between 1 and 40): "))

if guess == secret:
    print("Congratulations! You're right!")

else:
    print ("I am sorry! This is not correct!")
