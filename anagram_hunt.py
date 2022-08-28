from tabnanny import check
from anagrams import anagrams
import time
import datetime
import random
from timer import countdown



lengths = [ 5, 6, 7, 8]
word_list = []
word_length = ""
words_left = ""
anagram_list = []

def start_game():
    pass
    #countdown()

def config_prompt():
    global word_length

    try:
        word_length  = int(input("Please enter a word length [5, 6, 7, 8]:"))

    except ValueError:
        print('Integers only please. Try again.')
        config_prompt()

    check_length(word_length)

    


def check_length(wl):
    global word_length
    for length in lengths:
        if int(length) == int(word_length):
            start_game()
            return word_length
    try:
        word_length = int(input("That is not a correct word length. Please try again [5, 6, 7, 8]:"))
        check_length(word_length)

    except:
        print('Integers only please. Try again.')
        config_prompt()



def get_words(wl):
    global word_list
    word_list = anagrams[int(wl)]
    return word_list


def play_game(anlist):

    first_word = random.choice(anlist)
    words_left = len(anlist) - 1
    print("The word is: " ,first_word)
    print("There are ", words_left, " unguessed anagrams")
    print("You have 60 seconds left")
    guess = input("Make a guess: ")
    check_guess(guess)


def check_guess(g):
    global anagram_list
    for word in anagram_list:

        if g == word:
            print(g, " is an anagram")
            anagram_list.remove(word)
            print(anagram_list)
            return anagram_list

    print("wrong you fucking dumbass")





    
def main():
    global anagram_list

    config_prompt()

    #check_length(word_length)
    #print("in main method word length is " ,word_length)

    get_words(word_length)
    print (word_list)
    print(len(word_list))

    anagram_list = random.choice(word_list)
    print(" this list is ", anagram_list)

    play_game(anagram_list)

    






main()




        
    
    
    