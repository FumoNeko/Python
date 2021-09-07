# A class is basically a container for functions and variables
# Classes can do things like inheritence
# Classes are used for organization and localization

# methods are objects within classes

# An example class with default constructor
class exampleClass:
    def __init__(self): # this is a constructor
        self.str = "hello world"
# Constructors are used to assign variables (initialize)
# Constructors are just functions that run first to assign variables.
    def printText(self):
        print(self.str)
# In this class, we defined an initialization function and a print function.

obj = exampleClass() # we can refer to classes by calling them like functions

obj.printText() # the printText() function in the exampleClass() class is now a method.
