# Data Types and Operators, Conner Oquinn, v0.0

# Fundamental Data Types 
# String - str - Sequence of letters, numbers, spaces, or other characters.
# Strings in Python are inside ' ' or " "
# doesn't matter if i use ' ' or " " just be consistent.

# Boolean - boob - True or False values.

# Float - float - any number valure with a decimal, +/-, including 0.0

# Integers - int - any whole number including 0, +/-

# Data types are stored in variables.
# A variable is basically a bucket with a name to put data into.
# VARIABLE NAMES SHOULD TELL YOU WHAT DATA IS BEING STORED IN IT.
# Variables cannot start with a number
# camelCaseVaribaleNames
#snake_case_variable_names

# DECLARING VARIABLES AND ASSIGNING VALUES

highScore = 7865 # int data types

carSpeed = 12.333359 # float data type, miles per hour

hasAxe = True # Boolean data type
isPurple = False # Boolean data type

playerName = "Conner Oquinn" # string data type
mobType = "Skullion" # string data type

# assign new values
playerName = "Boyle Smite"
carSpeed = 232

# data types can change, be careful
hasAxe = 5.0

# printing data types
newInt = 3
newFloat= 4.0
newString = "ohio rizz"
newBool = False

print(type(newInt))
print(type(newFloat))
print(type(newString))
print(type(newBool))

# print variables to console / screen
print(playerName)
print(isPurple)
print(highScore)
print(carSpeed)

# printing varianles and expressionsto console / screen
print(highScore + 5000)
print(3 * 12)
print(highScore)


# printing variables inside of strings
print(f"Hello {playerName}. Your high score is {highScore}.\n")

# ARITHMETIC OPERATORS
myInt = 2
myFloat = 2.2
myNum = 0

# addition
myInt = 2 + 8
myFloat = 2.2 + 3.22

muInt = myInt + 5

myNum = myInt + myFloat
# when you add an int and a float together, the answer becomes a float

# subtraction
myNum = myInt - myFloat
myInt = myFloat - 1.25

# multiplication
myNum = myInt * myFloat

# division
myNumber = myInt / myFloat # first is numerator, second is denominator

# modulus (Modulo) % -- returns remainder after dividing
numStudents = 6
numSlicesPizza = 36

leftOvers = numSlicesPizza % numStudents
print(leftOvers)

# exponents
numSquared = 5 ** 2 # 5 is the base, 2 is the exponent

# floor division // -- divides, throws out the decimaal
myNum = myInt // myFloat

# addition assignment operator - mostly used for counters
myNum = 5
myNum = myNum + 1 # old method
myNum += 1 # new method

# comparison operators
# Is-Equal-To == are the two values equal to each other?
# returns true or false based on evaluations.
x = 6
print(x == 5)

# not - equal - to != are two values not equal?
# returns true or false based on evaluations. 
print(x != 12)

# greater than / greater than or equal to
print(5 > 3) # greater than
print(12 >= 2) # greater than or equal to

# less than and less than or equal to
print(5 < 3) # less than
print(12 <= 2) # less than or equal to

# logical operators
# and -- all conditions must be true for entire statement to be true
age = 16
height = 72.9
eyeColor = "grey"
# in order to ride the teacups, you must be atleast 18 years or older and at least 60" tall
print(age >= 18 and height >= 60)
print(age >= 18 and height >= 60 and eyeColor == "blue")
# always check for the most likely to be false condition first!!!!!
#print(defeatedBoss == true and level > 5 and hasBlueKey == true)

# or -- at least onecondition must be true for entire statement to be true
print(age >= 18 or height >= 60)
print(age >= 18 or height >= 60 or eyeColor == "blue")
# always check most likely true condition first
#print(defeatedBoss == true or level > 5 or hasBlueKey == true)

# not -- returns the opposite value of the statement
a = 5
print( a == 5)
print(not (not (a == 5)))

# combining logical operators
#print(a == 5 and hasKey == True or isCloud == True)
#TRUE and 

# identity operators
g = 1.0
h = 1.0
i = g
print(g is h)
print(i is h)
print(i is not 1.0)
print(i is not g)

# membership operators
fruits = ["apple", "banana", "tomato"]

