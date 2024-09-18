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

# .lower() can turn all letters lowercase
# .upper() can turn all letters uppercase

if isCorrect == "yes":
    print(f"ok{playerName}, lets play rock, paper, scissors!\n")
else:
    playerName = input("type your name and press enter.\n")
# the rules using multi lined strings
print("""
Welcome to the rock, paper, scissors robot!
its times to play rock, paper, scissors!
you will play against the cpu. the first player to score five points wins. 
you will select from rock, paper, and scissors.
the cpu will select rock, paper, and scissors at random.

1)rock beats scissors
2)scissors beats paper
3)paper beats rock
""")

# multi line strings
"""
anything in between the sets of double quotes is just ignored.
if you need to write large comments its easier to use multi lined quotes rather than single quotes
"""

# main game loop
while playerScore < 5 and cpuScore <5:
print(f"{playerName} you have {playerScore} points.\n The cpu has {cpuScore} points.\n")
playerChoice = input("please enter rock, paper, or scissors and press enter.\n").lower()
if playerChoice != "rock" or playerChoice != "scissors" or playerChoice != "paper":
    playerChoice = input("please enter rock, paper, or scissors and press enter.\n").lower()
    if playerChoice != "rock" or playerChoice != "scissors" or playerChoice != "paper":
        print("you are not following directions please try again.\n")
        exit()
        print(f"you have chosen{playerChoice}.\n")
    else:
        print(f"you have chosen{playerChoice}.\n")
#print current score for player and cpu
#let player select rock, paper, scissors
#let cpu select rock, paper, scissors randomly
#compare player choice to cpu choice
#print results to the screen 
#award point to winner and output results
