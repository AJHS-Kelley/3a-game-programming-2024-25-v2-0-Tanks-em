# awarding extra lives, Conner Oquinn, v0.0

lives = 3

# allow the user to input the score as an integer
score = # Look line 18 from the user_input.py file for an example.  
# if score is 10000 or less
    # lose a life
# if score is > 10000 but less than 100001
    # give 1 extra life
# if score is > 100000
    # give 2 extra lives

# output the score and number of lives to the screen


if score <= 10000:
    print("loseALife.\n")
    # change the number of lives. 
elif score < 100001:
    print("oneExtraLife.\n")
    # change the number of lives. 
else:
    print("twoExtraLives.\n")
    # change the number of lives. 
print(f"Your score is {score}! You gained {life} Lives")