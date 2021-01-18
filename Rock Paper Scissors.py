import random

choice = input("Pick your choice: ")

print("My choice is",choice)

choices = ["rock","paper","scissors"]
computerChoice = choices[random.randint(0, len(choices))]

print("Computer choice is", computerChoice)

if choice == "rock":
    if computerChoice == "rock":
        print("It's a Tie!!!!")
    elif computerChoice == "paper":
        print("You Lose!!! Boooooo!!!")
    elif computerChoice == "scissors":
        print("YAYY!!!! You Win!!!!")

if choice == "paper":
    if computerChoice == "rock":
        print("YAYY!!!! You Win!!!!")
    elif computerChoice == "paper":
        print("It's a Tie!!!!")
    elif computerChoice == "scissors":
        print("You Lose!!! Boooooo!!!")

if choice == "scissors":
    if computerChoice == "rock":
        print("You Lose!!! Boooooo!!!")
    elif computerChoice == "paper":
        print("YAYY!!!! You Win!!!!")
    elif computerChoice == "scissors":
        print("It's a Tie!!!!")