# Dragon Realm, <STUDENT_NAME>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart

import random
import time

def displayIntro():

    print('You are in a land that harbors dragons and all manner of fantasy creatures. In front of you,')
    print('you see three caves. In one cave deep in the forest, a friendly dragon lies within showing hospitality,')
    print('and will share his treasure and boon with you. The other dragon which harbors in another cave within the mountains,')
    print('is bloodlusted and hungry, and will brutally devour you with no further notice.')
    print('but in another cave deep underground along the coast their lies a small skeleton army within')

    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2' and cave != '3':
        print('Which cave will you go into? (1 or 2 or 3)')
        cave = input()
    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    chosenCave = random.randint(1, 3)

    if chosenCave == str(forestCave):
        print('Gives you his treasure!')
    elif chosenCave == str(mountainCave):
        print('devours you quickly in one bite!')
    else:
        print('you awake the small skeleton army!')
  
    
    
  



playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input() 