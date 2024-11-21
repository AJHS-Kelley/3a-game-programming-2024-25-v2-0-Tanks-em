# functions practice, conner oquinn, v0.0

import random

def helloWorldMulti(): # function signature
    """this function will output hello, world! ina a language the user choose.""" # docstring \
    # print a list of languages to the screen, at least three but no more than five.
    # allow the user to select (input) a choice for the language.
    # print "hello, world!" to the screen in that language.
    print("""
        Welcome to the Hello, World! Translator
        The following languages are available.
        [E]nglish
        [S]panish
        [J]apanese
        """)
    languageChoice = input("what language do you want?\n please type the first letter of the language you want,\n").upper()
    if languageChoice == "S":
        print("Hola, Mundo!")
    elif languageChoice == "E":
        print("Hello, World!")
    else:
        print("Konichiwa, Sekai!")

#helloWorldMulti() # function call

# function to determine even / odd numbers
arguement1 = random.randint(-1000, 1000)

def isEven(arguement1: int) -> bool: #requires one arguement and returns a boolean value
    """determines if an integer value is even or odd."""
    if arguement1 % 2 == 0:
        return True
    else:
        return False
    
print(isEven(arguement1))

# function with multiple aruguements
def canRideRollerCoaster(age: int, height: int) -> bool:
    if age > 10 and height > 4:
        print("you can ride.\n")
        return True
    else:
        print("you cannot ride.\n")
        return False
    
canRideRollerCoaster(4, 10) # arguements msut be passed in the same order as the function signature indicates.