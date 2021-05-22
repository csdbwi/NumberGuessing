import random

guess = int(input("Guess a number between 1 to 10: "))
number = random.randint(1,10)


if guess == number:
    print("Correct!")
elif guess < number:
    print("Your guess is too low.")
elif guess > number:
    print("Your guess is too high")

