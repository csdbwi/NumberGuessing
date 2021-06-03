import random

user = int(input("Guess a number between 1 to 5: "))
number = random.randint(1,5)

if user == number:
    print("Correct!")
else:
    print("Incorrect!")