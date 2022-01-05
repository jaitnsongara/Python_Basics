# Learn in Public | Variables 
# Author: Jatin Songara
# Variable is Container for Asgined Values or it provides the name to he Values

#========================================================================

name = "Jatin Songara"
# -------------- Int -------------------------------------------------------

age = 21

# -------------- float -----------------------------------------------------

height = 155.9
print(height)

# --------------------------------------------------------------------------

print(name)# <----name will be printed on console
#----- {------String------} String is a Value Assign to the variable "name"

# --------------------------------------------------------------|
#      Question is how many Variables are here in Python        |  
#                                                               |
#                 > int                                         |
#                 > flot                                        |
#                 > str                                         |
#                 > Bool                                        |
#                                                               |
# --------------------------------------------------------------|

# Contactination is by + and this use to combines two same datatypes
# we can use the typecasting or we can use formating the text
# ------- there are two ways we can do this--------------------
#---- Fromating and useing the varibale with string------------

print(f"{name} This the way to print the variable and sting\n")
#------------Concatination
print("this is used to concatination" + " " +str(age))

# --------------------- Bool -----------------------------------------------

human = True
# {-var-} <-asgine --Bool False
print(human)
# Now we are printing the Var = human

# Find out the type of the Variable we use type funcation

print(type(human))

#-^--Printing the type of human

# --------------------------------------------------------------------------

# -----------Two line of code can do this "Multiple Assignments" -----------

name, age, human = "jatin", 21, True
print(f"{name}, {age} ,{human} ")

