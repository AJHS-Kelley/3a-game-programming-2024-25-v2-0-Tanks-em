# loops, Conner Oquinn, v0.0
import random # import the random module for us to use
# generally put all your import statements at the top

# two types of loops
#for --- used when you know how many loops you'll need
#while --- used when you do not know how many loops you'll need

# for loop is like go fish, you search each card for what the player asked
# while loop is like musical chairs, you move around until the music stops

# each trip through the entire loop is called an iteration
# "iterate through the list" means use for a loop

# for loop example -- iterating a list
fruits = ["apple", "banana", "orange", "tomato"]
for eachFruit in fruits:
    print(eachFruit)

# continue keyword --- skins the current iteration and then finishes the loop
fruits = ["apple", "banana", "orange", "tomato"]
for eachFruit in fruits:
    if eachFruit == "banana":
        continue
    print(eachFruit)

# break keyword --- immediately exits the loop
fruits = ["apple", "banana", "orange", "tomato"]
for eachFruit in fruits:
    if eachFruit == "banana":
        break
    print(eachFruit)

# for loops using range(). range(x) is exclusive it starts at 0 and ends at x - 1
    for i in range(10): # range is 0 - 0
        print(i)
    
# might not always want to start at zero
for i in range(10, 100): #
    print(i)

# not want to count by 1
for i in range(10, 100, 5): # 10 = start - 1 = stop, 5 = # to count by
    print(i)

# sometimes you're not done writing the loops
    for x in range(10):
        pass # tells python this loops isn't finished, don't freak out

# while loops -- musical chairs
playerScore = 0
while playerScore < 100 # run as long as this is true
print(f"Starting: {playerScore}")
playerScore += random.radiant(1,3)
print(f"After: {playerScore}")

