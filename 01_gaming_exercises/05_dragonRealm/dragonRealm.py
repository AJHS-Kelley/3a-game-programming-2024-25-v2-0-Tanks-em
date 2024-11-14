# Dragon Realm, <STUDENT_NAME>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart

import random
import time

hasTorch = False

def displayIntro():

    print('You are in a land that harbors dragons and all manner of fantasy creatures. In front of you,')
    print('you see three caves. In one cave deep in the forest, a friendly dragon lies within showing hospitality,')
    print('and will share his treasure and boon with you. The other dragon which harbors in another cave within the mountains,')
    print('is bloodlusted and hungry, and will brutally devour you with no further notice.')
    print('but in another cave deep underground along the coast their lies a small skeleton army within')

    print()

def chooseCave():
    caveNumber = None
    while caveNumber != '1' and caveNumber != '2' and caveNumber != '3':
        print('Which cave will you go into? (1 or 2 or 3)')
        caveNumber = input()
    return caveNumber

def checkCave(chosenCave):

    print('You approach the cave...')

    if caveNumber == 1:
        chosenCave = "forestCave"
    elif caveNumber == 2:
        chosenCave = "mountainCave"
    elif caveNumber == 3:
        chosenCave = "undergroundCave"

    
    

    if chosenCave == "forestCave":
        print('you enter the cave to be greeted by a very kind dragon that gives you treasure')
    elif chosenCave == "mountainCave":
        print('you enter a cave with a bloodlustful dragon that hasnt eaten in days')
        print('while the dragon is cornering you you pick up a torch on the ground and light it with two rocks')
        hasTorch = True
        return hasTorch
    elif chosenCave == "undergroundCave":
        print('you awaken a skeleton army as you enter the cave')
  
    
    
  



playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input() 