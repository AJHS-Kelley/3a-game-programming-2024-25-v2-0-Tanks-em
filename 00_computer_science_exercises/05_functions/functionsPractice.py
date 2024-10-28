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
    languageChoice = input("what language do you want?\n please type the first letter of the language you want,\n").lower()
    if languageChoice == "spanish":
        print("Hola, Mundo!")
    elif languageChoice == "english":
        print("Hello, World!")
    else:
        print("Konichiwa, Sekai!")

helloWorldMulti()

