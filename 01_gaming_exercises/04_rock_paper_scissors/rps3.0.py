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
    Welcome, {playerName} to the rock, paper, scissors robot!
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

    
def pickWinner(playerChoice: str, cpuChoice: str) -> str:
    """Determines the winner using player and CPU choices."""
    if playerChoice == "rock" and cpuChoice == "paper":
    #cpu wins
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        return "cpu wins"
    elif playerChoice == "rock" and cpuChoice == "scissors":
        #player wins
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("you win a point,\n")
        return "player wins"
    elif playerChoice == "rock" and cpuChoice == "rock":
        #draw
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("you win a point,\n")
        return "draw"
    elif playerChoice == "scissors" and cpuChoice == "rock":
        #cpu wins
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("you win a point,\n")
        return "cpu wins"
    elif playerChoice == "scissors" and cpuChoice == "paper":
        #player wins
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("you win a point,\n")
        return "player wins"
    elif playerChoice == "scissors" and cpuChoice == "scissors":
        #draw
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("you win a point,\n")
        return "draw"
    elif playerChoice == "paper" and cpuChoice == "rock":
        #player wins
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("you win a point,\n")
        return "player wins"
    elif playerChoice == "paper" and cpuChoice == "paper":
        #draw
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("you win a point,\n")
        return "draw"
    elif playerChoice == "paper" and cpuChoice == "scissors":
        #cpu wins
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("you win a point,\n")
        return "cpu wins"
    else:
        print("unable to dtermine a winner. please restart.\n")
        exit()

def score(winner: str) -> int:
    """this function uses the winner to update the score for the cpu, num. draws, and player score"""
    if winner == "player wins":
        score = 1
    elif winner == "cpu wins":
        score = 1
    else: # this is a draw
        score = 0
    return score

def matchWinner(playerScore: int, cpuScore: int) -> bool:
    """This function determines if a player has won the game or not by scoring 5 points."""
    if playerScore >= 5:
        print("Congratulations! You are the winner.\n")
        return True
    elif cpuScore >= 5:
        print("Sadly, you have been defeated by the CPU.\n")
        return True   
    else: # No winner yet.
        return False

def playGame(playerScore: int, cpuScore: int) -> None:
    """This function will use all other functions to play Rock, Paper, Scissors. """
    while True:
        cpuPick = cpuChoice()
        playerPick = playerChoice()
        roundWinner = pickWinner(playerPick, cpuPick)
        if roundWinner == "player wins":
            playerScore += score(roundWinner)
        if roundWinner == "CPU Wins":
            cpuScore += score(roundWinner)

        print(f"Player Score: {playerScore}\n")
        print(f"CPU Score: {cpuScore}\n")

        if matchWinner(playerScore, cpuScore) == True:
            break

playGame(playerScore, cpuScore)

