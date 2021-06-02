import random

user = int(input("Guess a number between 1 to 10: "))
number = random.randint(1,10)

if user == number:
    print("Correct!")
else:
    print("Incorrect!")