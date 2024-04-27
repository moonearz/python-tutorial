"""
exercise 4
a) predit the output (in the console) of the following programs
Use python tutor if you're stuck!
"""
#functions
def foo():
    print("foo")

def bar(x):
    y = 20
    print("y =,", y)
    return "None"

def fee(y):
    print("gimme your beans")
    return y()

def fum(z):
    if z == "None":
        print("hmm...")
    elif z == None:
        print("grr...")
    else:
        return -1
    return 5 

#program 1
#print(fee(foo))

#program 2
#word = bar(3)
#fum(word)

#program 3
""" 
y = 3
word = bar(y)
fye = foo()
if y > 15:
    print(fum(word))
else:
    print(fum(fye))
"""

"""
b) Write a function that takes as input a list (of words, in alphabetical) and a string and uses bisection search
 to determine if the word is in the "dictionary". If the word is in the dictionary, the function should return its
 index and print how many guesses it had to make. If the word is not in the dicitionary the function should print
 that it did not find the word and return -1.
"""

#supplementary code for dictionary testing
f = open("words.txt", "r")
text = f.read()
f.close()
big_dict = []
temp_word = ""
for char in text:
    if char == ' ':
        big_dict.append(temp_word)
        temp_word = ""
    else:
        temp_word += char  
big_dict.sort()

#SOLUTION
def word_search(dictionary, word):
    min = 0
    max = len(dictionary) - 1
    space = range(min, max)
    guess = int((max + min) / 2)
    num_guesses = 1
    while(len(space) > 1):
        if(dictionary[guess] == word):
            print(word, "is in the dictionary at index", guess)
            print("num_guesses =", num_guesses)
            return guess
        elif(dictionary[guess] > word):
            max = guess
        else:
            min = guess
        #note that this code runs in both the elif and else cases
        space = range(min, max)
        guess = int((max + min) / 2)
        num_guesses += 1

    #in case the word is the last guess
    if(dictionary[guess] == word):
        print(word, "is in the dictionary at index", guess)
        print("num_guesses =", num_guesses)
        return guess
    else:
        print(word, "is not in the dictionary.")
        print("num_guesses =", num_guesses)
        return -1

#word_search(big_dict, "zombie")
#print(big_dict[55855])