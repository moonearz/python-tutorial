"""
exercise: 
a) modify the bisection algorithm for cube roots to work with negative numbers and numbers < 1
"""

#SOLUTION
#Use a boolean to remember if cube was negative, then we can just work with positive numbers using abs()
#If -1 < cube < 1, the magnitude of the cube root will be larger than the cube, so the initial high value should be one, and the low cube
#Invert the guess at the end if cube was negative to begin with

cube = -0.75
isNegative = (cube < 0)
cube = abs(cube)
epsilon = 0.01
num_guesses = 0
if cube > 1:
    low = 0
    high = cube
else:
    low = cube
    high = 1
guess = (high + low) / 2.0
while(abs(guess**3 - cube) > epsilon):
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0
    num_guesses += 1
if(isNegative):
    guess = -guess
print('num guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)



"""
b) use for or while loops to draw the following patterns using only single character output functions (e.g print("#")):
Note-- you can use end = "" as a parameter in the print function to avoid printing a new line

1. ########
    ######
     ####
      ##

2.    ##
     ####
    ######
   ########
   ########
    ######
     ####
      ##

3. #            #
    ##        ##
     ###    ### 
      ######## 
      ########
     ###    ###
    ##        ##
   #            # 

"""

#SOLUTIONS

""" 
#prob1
for i in range(4):
    for j in range(i):
        print(" ", end = "")
    for j in range(8, 2 * i, -1):
        print("#", end = "")
    for j in range(i):
        print(" ", end = "")
    print() 
"""

""" 
#prob2
#split into top half, bottom half
for i in range(1, 5):
    for j in range(4 - i):
        print(" ", end = "")
    for j in range(i):
        print("#", end = "")
        print("#", end = "")
    for j in range(4 - i):
        print(" ", end = "")
    print()

for i in range(4):
    for j in range(i):
        print(" ", end = "")
    for j in range(4 - i):
        print("#", end = "")
        print("#", end = "")
    for j in range(i):
        print(" ", end = "")
    print() 
"""

""" 
#prob3
#top half
for i in range(4):
    for j in range(i):
        print(" ", end = "")
    for j in range(i + 1):
        print("#", end = "")
    for j in range(3 - i):
        for k in range(4):
            print(" ", end = "")
    for j in range(i + 1):
        print("#", end = "")
    print()
#bottom half
for i in range(4):
    for j in range(3 - i):
        print(" ", end = "")
    for j in range(4 - i):
        print("#", end = "")
    for j in range(i):
        for k in range(4):
            print(" ", end = "")
    for j in range(4 - i):
        print("#", end = "")
    print() 
"""