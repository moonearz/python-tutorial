#TOPICS:
#what is computation
#python basics
#mathematical operations
#python variables and types
#intro iteration and branching

"""
What is a computer?
What is a computer program?
How does a computer read a computer program?
"""

print("Hello World!")


"""
computer programs must follow specific rules in order to compile:
syntax 
#cat dog boy -> bad syntax
#cat hugs boy ->ok syntax

#"ho"331 -> bad syntax
#3.1 * 5 -> ok syntax

(static) semantics
#I are hungry -> bad semantics, ok syntax
#3 + "hi" -> static semantic error

Once you don't have errors, meaning is determined
English: Flying planes can be dangerous -> multiple meanings
Not so with computers! But sometimes meaning is not what was intended -> major programming challenge
"""

"""
What is the point of a computer program?
Declarative vs. imperative knowledge

Finding the square root of x

recipe:
1. make a guess g
2. improve the guess by averaging g and x/g
3. repeat until the guess is close enough

Note that 1-3 are simple steps
There is an order/flow that specifies when each step is executed
The recipe says when to stop (sort of)
These elements are what make an algorithm

target: 2
initial guess: 1
"""

""" 
x = 2
g = 1

x_div_g = x / g
g = (g + x_div_g) / 2
print("g is now " + str(g) + "!")

x_div_g = x / g
g = (g + x_div_g) / 2
print("g is now " + str(g) + "!")

x_div_g = x / g
g = (g + x_div_g) / 2
print("g is now " + str(g) + "!") 
"""

"""
Notice the section above repeats a lot of code. We can streamline this process using a process called iteration
"""


""" 
#simple iteration:
for i in range(5):
    print(i)
"""


""" 
x = 2
g = 1
for i in range(3):
    x_div_g = x / g
    g = (g + x_div_g) / 2
    print("g is now " + str(g) + "!")
"""


"""
Instead of specifying exactly how many iterations to run, we can also use a conditional -> expression that is true or false
""" 


""" 
counter = 0
if(counter == 1):
    print("counter is 1!")
else:
    print("counter is not 1!")
if(counter == 0):
    print("counter is zero!")
"""

""" 
counter = 0
#conditional -- is counter less than 10?
while(counter < 10):
    print("hi abby")
    print(counter)
    counter += 1 
"""


""" 
x = 2
g = 1
while(abs(g * g - x) > 0.000001):
    x_div_g = x / g
    g = (g + x_div_g) / 2
    print("g is now " + str(g) + "!")
"""


"""
basic types of data:
int -> integers 1,2,3, etc...
float -> real number e.g. 3.45
bool -> True or False
None -> Special type has only one value, None
use the type() function to find the type of an object
you can also cast items of one type to another
"""

#type(3)
#type("hi abby")
#type(True)
#type(None)
#type(3.1415)
#print(int(3.1415))
#print(float(3))

"""
use operators to transform/combine objects
for example we can use +, -, *, / for integers
other operators: i**j is i to the power j, i % j is remainder when i is divided by j
"""

#print(20 % 3)
#print(6**3)
#print(3+5)


""" 
#modulus operator % is super useful for alternating!
for i in range(10):
    if i % 2 == 0:
        print(i, "is even!")
    else:
        print(i, "is odd!")
"""


""" 
for i in range(12):
    if i % 3 == 2:
        print("goose!")
    else:
        print("duck")
"""

"""
Exercise: write a program to print a message to the terminal 5 times, then a different message 5 times
e.g.
message1
message1
message1
message1
message1
message2
message2
message2
message2
message2

extra credit -- make the messages alternate
message1
message2
message1
message2...

extra extra credit -- make the messages follow the pattern ab ba ab ba ab
message1
message2
message2
message1
message1...
"""