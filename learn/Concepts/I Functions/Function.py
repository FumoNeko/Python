# Sometimes you will hear someone call these "methods"
# Method is just a fancy way of saying "function"

# A Function is a block of code that you can call upon later.
# Functions are useful when you anticipate that you will have to use a "function" in your code many times.
# In other words, you write the code once then you don't have to write it again. Not to be confused with looping or iterating.

# Whitespace is significant in Python. A function ends when there is no longer an indentation.
def my_function():
    print("Hello from a function")
my_function() # => "Hello from a function"

def multiply(a, b):
    c = a * b
    return c # return the result you want out of a function
variable = multiply(2,2)
print(variable)
