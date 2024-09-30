# rock, paper, scissors by conner oquinn, v0.0

# module imports
import random, time

# data structures -- PLAYER
playerScore = 0
playerChoice = None
numDraws = 0
# data structures -- CPU
cpuScore = 0
cpuChoice = None


# main game loop
loopCount = 0
loopsReq = input("how many loops do you want?\nEnter and integer no commas and press enter\n.")
# req is the universal abreviation for request is computer science
rpsTimeStart = time.time() # returns the number of seconds since Jan. 01, 1970 @ 12:00 am
while loopCount < loopsReq:
     



    while playerScore < 5 and cpuScore <5:

#let cpu select rock paper or scissors
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
#let player select rock, paper, scissors
    playerChoice = random.randint(0, 2) #randomly select 0, 1 or 2.
    if playerChoice == 0:
        playerChoice = "rock"
    elif playerChoice == 1:
        playerChoice = "paper"
    elif playerChoice == 2:
        playerChoice = "scissors"
    else:
        print("Unable to determine cpu choice\n. please try again")
        exit()
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
loopCount += 1
# STOP INDENTING HERE.  

print(f"your final score: {playerScore}\nCpu final score: {cpuScore}\n")
if playerScore > cpuScore:
    print(f"congratulations. a winner is you\n")
elif cpuScore > playerScore:
    print(f"the cpu wins you are a dissapointment to all\n")
else:
    print("unable to determine winner.\n please restart\n")
    exit()

rpsTimeStop = time.time()
rpsTime = rpsTimeStop - rpsTimeStart
print(f"number of loops: {loopCount}\n")
print(f"Execution Time {rpsTime:.}")