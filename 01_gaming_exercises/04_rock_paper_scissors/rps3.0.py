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
def playerName() -> str: # function signature -- name of function, (arguments if any)
    """gets the name from the player and reutrns it."""
    # the line above is a docstring, it gives brief example of what the function does.
    playerName = input("type your name and press enter.\n")
    print(f"hello{playerName}!\n")
    isCorrect = input("Is that correct? Type yes or no and press enter.\n").lower()

    if isCorrect == "yes":
        print(f"ok{playerName}, lets play rock, paper, scissors!\n")
    else:
        playerName = input("type your name and press enter.\n")
    return playerName

# calling the function
playerName = playerName()

# the rules using multi lined strings
def rules() -> None:
    """this function prints the rules for rock, paper, scissors."""
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
    # does another part of this program need to access this information
    # if yes you must have a return statement
    # if no a return statement is not required

def playerChoice() -> str: 
    """Allows the player to choose rock, paper, scissors"""
    playerChoice = input("please enter rock, paper, or scissors and press enter.\n").lower()
    if playerChoice != "rock" and playerChoice != "scissors" and playerChoice != "paper":
    # YOU NEED TO FIX THE INDENTING ON ALMOST EVERY LINE AFTER THIS. 
        playerChoice = input("please enter rock, paper, or scissors and press enter.\n").lower()
    if playerChoice != "rock" and playerChoice != "scissors" and playerChoice != "paper":
        print("you are not following directions please try again.\n")
        exit()        
    else:
        print(f"you have chosen{playerChoice}.\n")
    return playerChoice

def cpuChoice() -> str:
    """Allows the CPU to choose rock, paper, scissors"""
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
    return cpuChoice
# main game loop

while playerScore < 5 and cpuScore <5:

    print(f"{playerName} you have {playerScore} points.\n The cpu has {cpuScore} points.\n")
    
#print current score for player and cpu
    
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
elif print(f"cpu chose {cpuChoice} and you chose {playerChoice}\n."):
    print("the cpu wins a point\n")
    cpuScore += 1
elif print(f"cpu chose {cpuChoice} and you chose {playerChoice}\n."):
    print("you win a point\n")
    playerScore += 1
elif print(f"cpu chose {cpuChoice} and you chose {playerChoice}\n."):
    print("its a draw!\n")
elif print(f"cpu chose {cpuChoice} and you chose {playerChoice}\n."):
    print("you win a point\n")
    playerScore += 1
elif print(f"cpu chose {cpuChoice} and you chose {playerChoice}\n."):
    print("its a draw!\n")
elif print(f"cpu chose {cpuChoice} and you chose {playerChoice}\n."):
    print("cpu wins a point\n")
    cpuScore += 1
else:
    print("unable to determine a winner. please restart.\n")
    exit()

# STOP INDENTING HERE.  

print(f"your final score: {playerScore}\nCpu final score: {cpuScore}\n")
if playerScore > cpuScore:
    print(f"congratulations {playerName}, a winner is you\n")
elif cpuScore > playerScore:
    print(f"the cpu wins you are a dissapointment to all\n")
else:
    print("unable to determine winner.\n please restart\n")
    exit()
