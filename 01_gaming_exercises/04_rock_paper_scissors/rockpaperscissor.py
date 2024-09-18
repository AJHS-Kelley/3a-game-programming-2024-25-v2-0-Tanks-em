# rock, paper, scissors by conner oquinn, v0.0

# module imports
import random

# data structures -- PLAYER
playerScore = 0
playerName = "Test Player"
playerChoice = None

# data structures -- CPU
cpuScore = 0
cpuChoice = None

# player name input
playerName = input("type your name and press enter.\n")
print(f"hello{playerName}!\n")
isCorrect = input("Is that correct? Type yes or no and press enter.\n").lower()


if isCorrect == "yes":
    print(f"ok{playerName}, lets play rock, paper, scissors!\n")
else:
    playerName = input("type your name and press enter.\n")