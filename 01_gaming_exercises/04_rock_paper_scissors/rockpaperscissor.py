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
if playerChoice != "rock" and playerChoice != "scissors" and playerChoice != "paper":
    playerChoice = input("please enter rock, paper, or scissors and press enter.\n").lower()
    if playerChoice != "rock" and playerChoice != "scissors" and playerChoice != "paper":
        print("you are not following directions please try again.\n")
        exit()
        print(f"you have chosen{playerChoice}.\n")
    else:
        print(f"you have chosen{playerChoice}.\n")
#print current score for player and cpu
cpuChoice = random.randint(0, 2) #randomly select 0, 1 or 2.
if cpuChoice == 0:
    cpuChoice = "rock"
elif cpuChoice == 1:
    cpuChoice = "paper"
elif cpuChoice == 2:
    cpuChoice = "scissors"
else:
    print("Unable to determine cpu choice\n. please try again")
    exit()
print(f"CPU choice: {cpuChoice}")
#let player select rock, paper, scissors

#let cpu select rock, paper, scissors randomly
#compare player choice to cpu choice
if playerChoice == "rock" and cpuChoice == "paper":
    #cpu wins
    print(f"cpu chose {cpuChoice} and you chose {playerChoice}\n.")
    print("the cpu wins a point\n")
    cpuScore += 1
elif playerChoice == "paper" and cpuChoice == "scissors":
    #player wins
    print(f"cpu chose {cpuChoice} and you chose {playerChoice}\n.")
    print("you win a point\n")
    playerScore += 1
elif playerChoice == "rock" and cpuChoice == "rock":
    #draw
    print(f"cpu chose {cpuChoice} and you chose {playerChoice}\n.")
    print("its a draw!\n")
elif #player choose scissors, cpu choose rock:
    #cpu wins
    print(f"cpu chose {cpuChoice} and you chose {playerChoice}\n.")
    print("the cpu wins a point\n")
    cpuScore += 1
elif #player choose scissors, cpu choose paper:
    #player wins
    print(f"cpu chose {cpuChoice} and you chose {playerChoice}\n.")
    print("you win a point\n")
    playerScore += 1
elif #player choose scissors, cpu choose scissors:
    #draw
    print(f"cpu chose {cpuChoice} and you chose {playerChoice}\n.")
    print("its a draw!\n")
elif #player choose paper, cpu choose rock:
    #player wins
    print(f"cpu chose {cpuChoice} and you chose {playerChoice}\n.")
    print("you win a point\n")
    playerScore += 1
elif #player choose paper, cpu choose paper:
    #draw
    print(f"cpu chose {cpuChoice} and you chose {playerChoice}\n.")
    print("its a draw!\n")
elif #player choose paper, cpu choose scissors: 
    #cpu wins
    print(f"cpu chose {cpuChoice} and you chose {playerChoice}\n.")
    print("cpu wins a point\n")
    cpuScore += 1
else:
    print("unable to determine a winner. please restart.\n")
    exit()

 print(f"your final score: {playerScore}\nCpu final score: {cpuScore}\n")
 if playerScore > cpuScore:
    print(f"congratulations {playerName}, a winner is you\n")
elif cpuScore > playerScore:
    print(f"the cpu wins you are a dissapointment to all\n")
else:
    print("unable to determine winner.\n please restart\n")
    exit()
