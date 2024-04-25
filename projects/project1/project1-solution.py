#WORDLE GAME
import random

#READ FILE
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

#GET FIVE LETTER WORDS
five_letter_words = []
def has_5_letters(word):
    """
    Input: string word
    Returns True if word contains 5 characters, false otherwise
    """
    return len(word) == 5

for word in words:
    if has_5_letters(word):
        five_letter_words.append(word)

#array indexes range from 0 to len(five_letter_words) - 1
random_int = random.randint(0, len(five_letter_words) - 1)
target = five_letter_words[random_int]
#print("psst... the word is", target)

#FUNCTIONS
def print_correctness(correctness):
    """
    Input: list of characters
    Prints each character of the list to the console with a space in between, then prints a new line
    Does not return a value
    """
    for char in correctness:
        print(char + " ", end = "")
    print()

#CORRECTNESS FUNCTIONS
def reset_correctness(correctness):
    """
    Input: correctness list
    Sets all values in correctness to ""
    Does not return a value
    """
    for index in range(len(correctness)):
        correctness[index] = ""

def are_equal(string1, string2):
    """
    Input: two strings of equal length
    Returns True if the strings are the same, False otherwise (without using ==)
    """
    for index in range(len(string1)):
        if string1[index] != string2[index]:
            return False
    return True

def set_greens(target, guess, correctness):
    """
    Input: two strings of equal length, the correctness array
    Sets the correctness array at index i to "G" if the strings at index i are the same for all indices i in the strings
    Does not return a value
    """
    for index in range(len(target)):
        if target[index] == guess[index]:
            correctness[index] = "G"
    
def string_difference(target, guess):
    """
    Input: two strings of equal length (5, in this case)
    Returns the same strings except that if they have the same character at the same index it is replaced with _
    i.e. string_difference("crane", "crate") returns ["___n_", "___t_"]
    """
    new_t = ""
    new_g = ""
    for index in range(len(target)):
        if target[index] == guess[index]:
            new_t += "_"
            new_g += "_"
        else:
            new_t += target[index]
            new_g += guess[index]
    return [new_t, new_g]

def set_yellows_difference(new_t, new_g, correctness):
    """
    Input: the difference of two strings of equal length (no characters in common at any index i) and the correctness array
    Sets the correctness array at index i of new_g to "Y" if new_g[i] is in new_t (uniquely)
    Does not return a value
    """
    for index1 in range(len(new_g)):
        if not new_g[index1] == "_":
            for index2 in range(len(new_t)):
                if new_g[index1] == new_t[index2]:
                    correctness[index1] = "Y"
                    new_t = new_t[0:index2] + "_" + new_t[index2 + 1:]

def set_yellows(target, guess, correctness):
    """
    Input: original target and guess strings, the correctness array
    Sets the yellows in the correctness array by combining the two previous functions
    Does not return a value
    """
    difference = string_difference(target, guess)
    set_yellows_difference(difference[0], difference[1], correctness)

def set_grays(correctness):
    """
    Input: the correctness array
    Sets all empty values in correctness to "X"
    Does not return a value
    """
    for index in range(len(correctness)):
        if correctness[index] == "":
            correctness[index] = "X"

#INITIALIZE GAME VALUES
guess_number = 1
correctness = ["", "", "", "", ""]

#MAIN GAME LOOP
print("Welcome to WORDLE!")
print('Key: "G" = green, "Y" = yellow, "X" = gray')
while(guess_number < 7):
    print_correctness(correctness)
    print("- - - - -")
    guess = input(("Enter a guess: "))
    if are_equal(target, guess):
        print("Congratulations! You guessed right. The word was", target)
        break
    print()
    guess_number += 1
    reset_correctness(correctness)
    set_greens(target, guess, correctness)
    set_yellows(target, guess, correctness)
    set_grays(correctness)

if(guess_number > 6):
    print("Oh no! You ran out of guesses. The word was", target)