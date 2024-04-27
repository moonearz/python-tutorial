"""
TOPICS:
structuring programs and hiding details via abstraction and decomposition
functions
specifications
keywords-- return and print
scope
"""

"""
ABSTRACTION-- we don't need to know how something works to use it
example -> electric pallet jack
DECOMPOSITION-- different devices work together to acheive a larger end goal
example -> one giant uboat versus several movable ones
"""

#import random
#print(random.randint(0, 10))
#even without knowing how random works, I can use it for additional features
#for example, generate a random even number between 0-10
#print(2 * random.randint(0,5))

"""
decomposition in programming = functions/modules, eventually classes
features of modules:
    self-contained
    break up code
    resuable
    keep code organized
    keep code coherent
"""

"""
abstraction in programming = code as a black box
achieve via function specifications, also known as docstrings
"""

"""
FUNCTIONS:
functions on their own are not run in a program unless they are CALLED or INVOKED -> otherwise they may as well be comments
functions have:
1. a name
2. paramaters (0 or more)
3. a docstring (recommended for readability)
4. a body
5. a return statement

as a programmer, you think about programs in two different ways:
    1. writing your own functions, understanding how the underlying components work
    2. using functions as a black box, especially useful in module-based languages like python
"""

def is_even(i):
    """
    Input: positive integer i
    Returns True if i is even, False otherwise
    """
    print("is_even was called")
    return i % 2 == 0

#is_even(3)
#print(is_even(3))
#result = is_even(4)
#print(result)

"""
components of this function:
def keyword tells python you're defining a function
name of function follows def
parameters of function are in parentheses
docstring comment first thing after def
body of function prints to the console
return statement returns boolean of whether input is even
once you return, nothing else happens (example print after return)
if no return statement, python returns None for you
"""

"""
SCOPE: function calls create new environments separate from the environment of the main program
"passing" variables -> only the returned value gets sent back to the main environment
pythontutor.com is a great resource for understanding function scopes
"""

def f(x):
    x = x + 1
    print('in f(x): x =', x)
    return x

#MAIN PROGRAM CODE -- initializes x, calls f(x), assigns return value to z
#x = 3
#z = f(x)
#print(x)
#print(z)

def is_even_no_return(i):
    """
    Input: positive integer i
    Does not return anything
    """
    print("no return")
    i % 2 == 0
    #return None -> python does this for you

#print(is_even(3))
#print(is_even_no_return(3))

""" 
#functions can be reused many times
for i in range(20):
    if is_even(i):
        print(i, "is even")
    else:
        print(i, "is odd") 
"""

"""
function paramaters can be of any type, even other functions:
"""

def func_a():
    print("inside func_a")

def func_b(y):
    print("inside func_b")
    return y

def func_c(z):
    print("inside func_c")
    return z()

#print(func_a())
#print(5 + func_b(2))
#print(func_c(func_a))

"""
functions scopes are their own worlds, which means they can reuse variables names, even though it can be confusing
functions can also access variables from the exterior scope
inside a function you cannot modify a variable defined outside-- can using global variables
global variables are not a good idea generally-- code gets very messy
"""

def fs(y):
    x = 1
    x += 1
    print(x)

x = 5
#fs(x)
#print(x)

def gs(y):
    #uses x from outside g
    print(x)
    print(x + 1)

#x = 5
#gs(x)
#print(x)

def hs(y):
    x += 1

#x = 5
#hs(x)
#print(x)

"""
harder scope example-- follow along in python tutor
"""

def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('g: x =', x)
    h()
    return x

#x = 3
#z = g(x)
#print(z)

"""
major advantage of functions-- only have to debug once!
exercises: 
a) predict outputs of programs (see exercise file)
b) use bisection search to write a function that finds a word in a dictionary
The exercise file has supplementary code to test your search function on a real dictionary
"""

"""
Super common data storage in python: lists and tuples
lists are like strings except instead of storing characters they can store any object type
tuples are lists of a fixed size, say 2
"""

#list = [1, 2, 3]
#print(list)
#tuple = ["x", "y"]
#print(tuple)
#print(tuple[0])
#list.append(4)
#print(list)

#for number in list:
    #print(number + 1)