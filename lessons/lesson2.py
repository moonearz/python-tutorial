#TOPICS:
#string objects
#branching and iteration, control flow

"""
Learning Outcomes-- at the end of this lesson you will be able to:

Define what strings and booleans are in Python
Manipulate strings and booleans using their associated operators
Predict the output of simple programs that use conditional statements
Write basic programs that take user input and can make decisions based on that input
"""

"""
Strings: a super important data type in python (and most languages)
letters, special characters, spaces, digits
enclose in quotes "" or single quotes ''
concatenate (add) strings
other operations (see python documentation)
"""

""" 
hi = "hello there"
name = "abby"
greet = hi + name
greeting = hi + " " + name
print(greet)
print(greeting)
print((greeting + " ") * 3)
"""

"""
Input/output -> adding user interaction to the mix
output keyword: print    (this prints to console/terminal)
input keyword: input     (paired with an output statement)
binds user value after they hit enter
input always reads a string, must cast if looking for something else
"""


""" 
text = input("Type something! ")
print(5 * text)
print(type(text)) 
"""


"""
#using casting
num = int(input("Type a number: "))
print(5 * num)
print(type(num)) 
"""

"""
comparing objects (int, float, string):
>
>=
<
<=
==
!=
output type: boolean -> True/False
"""

"""
condition = 5 > 3
print(condition)
print(type(condition))
print(5 <= 2)
"""

"""
basic logical operators on bools:
not a
a and b
a or b
"""

""" 
sleep_time = 10
enough_sleep = 8
got_enough_sleep = (sleep_time >= enough_sleep)
print(got_enough_sleep)
print(not got_enough_sleep)

eats = 1800
enough_eat = 2000
ate_enough = (eats >= enough_eat)
print(got_enough_sleep and ate_enough)
print(got_enough_sleep or ate_enough)
"""

"""
back to conditionals -> recall if, else
new: elif
indentation matters
= vs. ==
= overwrites in memory
"""

""" 
x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y:
    print("x and y are equal")
    if y != 0:
        print("therefore, x/y is", x/y)
elif x < y:
    print("x is smaller")
else:
    print("y is smaller")
print("all done!")
"""

"""
#iterating through numbers using for and while loops
n = 0
while n < 5:
    print(n)
    n = n + 1

for n in range(5):
    print(n)

#for loops are simpler if you know how many/which iterations you need
"""

"""
range -> extremely useful function for loops
default values: start = 0 step = 1, loop until stop - 1
"""


""" 
sum = 0
for i in range(7,10):
    sum += i
print(sum)

sum = 0
for i in range(5, 11, 2):
    sum += i
print(sum)
"""

""" 
#a simple algorithm for computing squares -> n^2 = 1 + 3 + ... + 2n - 1
for i in range(1,21):
    square = 0
    for j in range(1, 2 * i, 2):
        square += j
    print(i, "^2 is: ", square, sep = "") 
"""

"""
break statements:
immediately exits whatever loop it is in, skipping remaining expressions in code block
only exits innermost loop
"""


""" 
#try to predict the output of this program:
sum = 0
for i in range(5, 11, 2):
    sum += i
    if sum == 5:
        break
        sum += 1
print(sum)
"""

"""
exercise: grade calculator
write a program that prompts the user to enter in their grades on assignments one at a time until they enter "compute"
assume the user will give you a valid input
compute and print a float of their grade average
after their average, print their letter grade using the following scale:
>=93 -> A
90-93 -> A-
87-89 -> B+
83-86 -> B
80-82 -> B-
77-79 -> C+
73-76 -> C
70-72 -> C-
66-69 -> D+
60-65 -> D
<59 -> F

suggestion-- break up the problem into small pieces
"""