"""Rock, papaer, scissors vs. computer"""

from random import randint

t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0, 2)]
player = False

while player == False:
    player = input("Rock, Paper or Scissors")
    print("\n")
    if player == computer:
        print("TIE!!")
    elif player == "Rock":
        if computer == "Paper":
            print("You Lose!!", computer, "covers", player)
        else:
            print("You Win!!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You Lose!!", computer, "cut", player)
        else:
            print("You Win!!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You Lose!!", computer, "smashes", player)
        else:
            print("You Win!!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling and capitalization.")

player = False
computer = t[randint(0, 2)]