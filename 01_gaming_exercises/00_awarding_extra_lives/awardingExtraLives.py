# awarding extra lives, Conner Oquinn, v0.0

lives = 3

# allow the user to input the score as an integer
# if score is 10000 or less
    # lose a life
# if score is > 10000 but less than 100001
    # give 1 extra life
# if score is > 100000
    # give 2 extra lives

# output the score and number of lives to the screen

score = 0
life = 0
if score <= 10000:
    print("loseALife.\n")

elif score < 100001:
    print("oneExtraLife.\n")

else:
    print("twoExtraLives.\n")

print(f"Your score is {score}! You gained {life} Lives")