import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num,highest_num)
guesses = 0
is_running = True

print("Python Num Guessing Game")
print(f"Select a Num between 1 and 100")

while is_running:
    guess = input("Enter ur Guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That is Invalid Guess or Out of Range")
            print(f"Select a Num between 1 and 100")
        elif guess < answer:
            print("Too low")
        elif guess > answer:
            print("Too High")
        else:
            print(f"Correct! The answer was {answer}")
            print(f"Number of Guesses: {guesses}")
            is_running = False 
    else:
        print("Invalid Guess")
        print(f"Select a Num between 1 and 100")