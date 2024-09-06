# loops, Conner Oquinn, v0.0

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
    for 1 in range(10): # range is 0 - 0
        print(1)
        