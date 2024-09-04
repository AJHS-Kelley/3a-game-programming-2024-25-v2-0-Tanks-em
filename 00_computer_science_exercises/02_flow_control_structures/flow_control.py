# flow control structures, Conner Oquinn, v0.0
# making computer programs make descisions

temperature = 89.54
color = "Cyan"
height = 6
likesPineappleOnPizza = True

# single sescision point - if statement
# if conditional expression -- this will use a comparison operator 99% of the time
# run this code if the conditional expression is true

if temperature > 80:
    print("it is hot as sun outside.\n")

if height > 7:
    print("they are too tall.\n")

# cheat code for if statements that use booleans
if likesPineappleOnPizza:
    print("yummy.\n")

# what if something we want happens different?
if color == "Red": #common error for student is using = instead of ==
    print("Your shirt is the correct uniform color.\n")
else:
    print("Your shirt is not the correct uniform color.\n")

if height == "8":
    print("You are perfect height.\n")
else:
    print("You are not the perfect height.\n")

# amusement park height checker example
# must be > min. height and < max. height to ride.
    
# when writing if-elif-else blocks check for the highest value first when using > or >=
if height >= 3:
    print("You're tall enough to ride the teacups!.\n")
elif height >= 3:
    print("You're too tall to ride the teacups.\n")
else: # "oh, no, somethings wrong!"
    print("Error, height not detected. Do not ride.\n")

# when writing if-elif-else blocks check for the lowest value first when using < or <=
if height <= 3:
    print("You're not tall enough to ride the teacups!.\n")
elif height <= 3:
    print("You're too tall to ride the teacups.\n")
else: # "oh, no, somethings wrong!"
    print("Error, height not detected. Do not ride.\n")

# create and if-elif-else block that checks for temperature
if temperature >= 100:
    print("it's too hot outside.\n")
elif temperature >= 50:
    print("Recess is allowed today.\n")
elif temperature > 0:
    print("Recess will be in gym today.\n")
else:
    print("Error detecting temperature.\n")
