# User Input Practice, Conner Oquinn, v0.0

# input() is the built in function to get information from the keyboard
# basic example
variableName = input("please type a variable name and press enter.\n")
print(variableName)

# input() saves ALL INPUT TO STRING DATA TYPES NY DEFAULT!!!
# input() saves ALL INPUT TO STRING DATA TYPES NY DEFAULT!!!
# input() saves ALL INPUT TO STRING DATA TYPES NY DEFAULT!!!
# input() saves ALL INPUT TO STRING DATA TYPES NY DEFAULT!!!

# incorrect causes a concatenation error.
#myNumber = input("Please type an integer number and press enter.\n")
#print(myNumber + 5)

# correct --- use a wrapper
myNumber = int(input("Please type an integer number and press enter.\n"))
print(myNumber + 5)

# wrapper functions
# int() will convert the data to an integer if possible
newNumber = input("Please type a value and press enter.\n")
print(float(newNumber)) #will convert the data to a float 
print(str(newNumber)) #will convert the data to a string
print(int(newNumber)) #will conert the data to a integer

# float() will convert the data to a float if possible
newNumber = input("Please type a value and press enter.\n")
# print(int(newNumber)) --- cannot convert float to integer
print(float(newNumber)) # can convert string to float
print(str(newNumber)) # can convert float to string

# str() will convert the data to a string if possible
newNumber = 5
print(newNumber + newNumber) # should print 10
print(str(newNumber + newNumber)) # should print 55
