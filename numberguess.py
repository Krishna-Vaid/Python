#Number guessing game between 0 to 10
import random

random_num = random.randint(0, 11)
guess = 0

while True:
    guess += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number ")
        continue

    if user_guess == random_num:
        print("You got it!")
        break
    elif user_guess > random_num:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guess, "guesses")