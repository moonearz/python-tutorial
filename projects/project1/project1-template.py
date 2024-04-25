"""
In this project you will use the given template to create a simplified version of the wordle game available here:
https://www.nytimes.com/games/wordle/index.html
It is assumed the user will know how to play the game.
We will use the abbreviations G for green, Y for yellow, X for gray to avoid using graphics modules (this can be changed later)
"""

"""
Generating 5 letter words:
You are given a large list of words (of many lengths), called words, and an empty list called five_letter_words. 
1. Write a function that returns True if a string contains 5 characters and False otherwise
2. Loop through the words in words and use the .append() function to add 5 letter words to five_letter_words

list.append(parameter) adds parameter to the end of the list
"""
#imports you will need
import random

f = open("words.txt", "r")
text = f.read()
f.close()
words = []
temp_word = ""
for char in text:
    if char == ' ':
        words.append(temp_word)
        temp_word = ""
    else:
        temp_word += char   

five_letter_words = []
#YOUR CODE GOES HERE
#YOUR CODE GOES HERE
#YOUR CODE GOES HERE

"""
Choosing a 5 letter word:
Use the randomint function from the random library to choose a random word from your list of five letter words
Assign the chosen word to a variable called target
"""

#YOUR CODE GOES HERE
#YOUR CODE GOES HERE
#YOUR CODE GOES HERE

"""
Game start:
Print a welcome message and key to the console:
Welcome to WORDLE!
Key: "G" = green, "Y" = yellow, "X" = gray

Create a variable called guess_number and set its value to 1
Start a while loop that runs while guess_number is less than or equal to 6

We will use a list called correctness to store which letters in the user's guess are correct
Initialize the correctness list with 5 empty strings

Write a function that prints each character in the correctness array to the console (with a space in between) followed by a new line

Use the function you just created + print/input statements to make the following appear in the console:

_ _ _ _ _

Enter a guess: 

The user's entry should be saved under the variable name guess
Assume their entry will be a five character string
"""

#YOUR CODE GOES HERE
#YOUR CODE GOES HERE
#YOUR CODE GOES HERE

"""
Comparing a guess to the target word:
(Reset Correctness)
1. Write a function that sets every character of correctness to the empty string ""

(Equality of strings)
2. Write a function that takes an input of two string and returns True if the string are the same, and False otherwise (or use == for strings)

(Green letters)
3. Write a function that takes an input of two strings (and the correctness list) and compares them one character at a time. The function
should keep track of which index it is comparing. If the strings are equal at an index, it should set correctness of that index to "G" for green.

(Yellow letters)
4. Write a function that takes an input of two strings and returns their difference as two five character strings (a tuple) in the following way:
If input1[i] = input2[i], output1[i] = output2[i] = "_". Otherwise, output1[i] = input1[i] and output2[i] = input2[j]
5. Write a function that takes an input of two strings, temp_target and temp_guess, and the correctness list. The function should iterate through temp_guess in order and check if the 
characters in temp_guess are in temp_target, skipping lo-dashes. If character i of guess is in target, set correctness[i] to "Y" for yellow. Then, remove the corresponding letter
from temp_target to avoid double counting yellow tiles.
6. Combine 4 and 5 to make a function that sets the yellow characters in correctness

(Gray letters)
7. Write a function that sets any empty characters in correctness to "X"

In your game loop, check if the guessed word is the same as the target word. If it is, print "Congratulations! You guessed right. The word was " + target to the console and break out of the while loop
If not, do all of the following (inside your while loop):
Add one to the guess counter
Reset the correctness counter
Set the greens in the correctness list
Set the yellows in the correctness list
Set all the grays in the correctness list

Note that functions must be defined before (above) where they are invoked, so you may need to move your game loop to the bottom
"""

#YOUR CODE GOES HERE
#YOUR CODE GOES HERE
#YOUR CODE GOES HERE

"""
End of game:
After the while loop ends, print the following if the number of guesses is at least 6:
"Oh no! You're out of guesses. The words was " + target 
"""

#YOUR CODE GOES HERE

"""
And that's it! Give the game a try
"""