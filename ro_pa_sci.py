#Rock ,Paper , Scissors

import random

options = ("rock" , "paper" ,"scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
     player = input("Enter your choice(rock 🪨 , paper📃 , scisssors✂️): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("TIE 😵")
    elif player == "rock" and computer == "scissors":
        print("You WIN 😎")
    elif player == "scissor" and computer == "paper":
        print("You WIN 😎")
    elif player == "paper" and computer == "rock":
        print("You WIN 😎")
    else:
        print("You LOSE 😶")

    play_again = input("Play Again 😏 (y/n): ").lower()

    if play_again == "n":
        running = False

print("Thanks For Playing 😊")