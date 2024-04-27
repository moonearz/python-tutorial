"""
TOPICS:
string manipulation
alogrithmic thinking:
    guess-and-check
    approximation
    bisection
"""

"""
thinking of strings as sequences of characters
example: "abby" = [a, b, b, y]
can compare with ==, <, > (comparison is alphabetical order)
len() retrieves the length of the string in parentheses
"""


""" 
print("Abby" == "abby")
print("abby" > "munir")
print(len("abby"))
"""

"""
use square brackets for indexing, getting the value at a certain index/position
indexing always starts at 0, we say strings/arrays are 0-indexed
can go backwards, last element always starts at -1
"""

"""
s = "dude"
print(s[0])
print(s[1])
print(s[2])
print(s[3])
#print(s[4])
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
"""

"""
longer indexing-- use slices using [start:stop:step]
two number -> [start:stop], step = 1 by default
numbers optional, can leave colons -> s[::] is the same as s[0:len(s):1]
"""


""" 
s = "ohmylord"
print(s[3:6])
print(s[3:6:2])
print(s[::])
print(s[::-1])
print(s[4:1:-2])
"""

"""
strings cannot be modified once they are created, call this property immutability, say string are immutable
we can use assignment to overwrite values to new strings, however
"""


""" 
s = "hello"
#s[0] = 'y'
print(s)
s = 'y' + s[1:len(s)]
print(s) 
"""

"""
recall for loops iterate over a set of values
we used range() to iterate over a set of numbers
examples: 
    for i in range(4) iterates over 0,1,2,3
    for i in range(4,6) iterates over 4,5
loops can actually iterate over any set of values, not just integers
"""


""" 
#these two loops do the same thing, but one is easier to read, more intuitive
s = "the quick brown fox jumps over the lazy dog"
for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print("there is an i or a u")
print()
for char in s:
    if char == 'i' or char == 'u':
        print("there is an i or a u")
"""


""" 
#cheer for a word
an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("Enter a word and I will cheer for you!: ")
times = int(input("Enter my enthusiasm level (1-10): "))

for char in word:
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a " + char + "! " + char)
print("What does that spell?")
for i in range(times):
    print(word + "!!!")
"""

"""
We will look at different ways of approaching the problem of finding cube roots
First approach: guess-and-check
Guess a value
Check if the value is correct
Repeat until solution is found or all options are exhausted
"""


""" 
cube = 512
#cube root will be less than cube for positive integers
for guess in range(cube + 1):
    if guess**3 == cube:
        print("cube root of", cube, "is:", guess) 
"""


""" 
#adaptation to include negative cube roots
cube = -512
for guess in range(abs(cube) + 1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
        print("cube root of", cube, "is:", guess) 
 """

"""
Second approach: approximate solutions
not perfect but good enough
start with a guess and increment by a small value
keep guessing if abs(guess*3 - cube) > epsilon -> epsilon small
decreasing increment size leads to slower program
increasing epsilon leads to less accurate answer
"""


""" 
cube = 512
epsilon = 0.01
guess = 0.0
increment = 0.001
num_guesses = 0
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print("num_guesses =", num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print("failed on cube root of", cube)
else:
    print(guess, "is close to the cube root of", cube) 
"""

"""
Third approach: bisection
idea: cut search space in half after each iteration
illustration -> guessing game
compare to guess-and-check, checking 1,2,3,...
"""

""" 
print("Write down a number between 1 and 100!")
print("I will guess your number within 7 guesses")
min = 1
max = 101
space = range(min, max)
guess = int((min + max) / 2)
num_guesses = 0
userInput = ""
while(userInput != "y" and len(space) > 1):
    userInput = input("Is your number " + str(guess) + "? (y/n) ")
    num_guesses += 1
    if userInput == "n":
        userInput = input("Is your number greater than or less than " + str(guess) + "? (g/l) ")
        if userInput == "g":
            min = guess + 1
            space = range(min, max)
            guess = int((min + max) / 2)
        else:
            max = guess
            space = range(min, max)
            guess = int((min + max) / 2)
if userInput == "y":
    print("Yay! Your number was " + str(guess) + " and I got it in " + str(num_guesses) + " tries.")
else:
    print("I'm confident. My final guess is that your number is " + str(guess)) 
"""

"""
bisection search applied to cube root
max is cube, min is zero
guess in the middle
adaptations --  negative cubes, small cubes?
"""


""" 
cube = 200145
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low) / 2.0
while(abs(guess**3 - cube) > epsilon):
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0
    num_guesses += 1
print('num guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)
"""

"""
exercise: 
a) modify the bisection algorithm for cube roots to work with negative numbers and numbers < 1
b) see exercise3.py
"""