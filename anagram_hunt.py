from tabnanny import check
from anagrams import anagrams
import time
import datetime
import random


lengths = [ 5, 6, 7, 8]
word_list = []
word_length = ""
words_left = ""
anagram_list = []
guess_list = []
first_word = ""
game_over = False

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


def play_game(anagram_list):
    global word_length
    global words_left
    global first_word
    global game_over

    words_left = len(anagram_list)
    

    time_limit = 30
    start_time = time.time()
    #print(start_time)

    while not game_over:
        elapsed_time = time.time() - start_time
        print(elapsed_time)
        #print(words_left)
        

        if words_left == 0:
            #get_words(word_length)
            print("this list is solved")
            get_words(word_length)
            anagram_list = random.choice(word_list)
            print(" this list is ", anagram_list)
            first_word = random.choice(anagram_list)
            anagram_list.remove(first_word)
            word_list.remove(anagram_list)
            play_game(anagram_list)

            
        print("The word is: " ,first_word)
        print("There are ", words_left, " unguessed anagrams")
        print("You have", time_limit - int(elapsed_time), " seconds left")
        guess = input("Make a guess: ")
        check_guess(guess)

        if elapsed_time > 30:
            game_over = True
            end_game()

        


def check_guess(g):
    global anagram_list
    global words_left
    for word in anagram_list:

        if g == word:
            print(g, " is an anagram")
            anagram_list.remove(word)
            print(anagram_list)
            words_left = len(anagram_list)
            print(words_left)
            return

    print("wrong you fucking dumbass")


def end_game():
    global game_over
    
    print("Time is up, Game Over")
    

def main():
    global anagram_list
    global first_word
    global word_list
    global word_length

    config_prompt()

    #check_length(word_length)
    #print("in main method word length is " ,word_length)

    get_words(word_length)
    print (word_list)
    print(len(word_list))

    anagram_list = random.choice(word_list)
    print(" this list is ", anagram_list)
    word_list.remove(anagram_list)
    print(word_list)

    first_word = random.choice(anagram_list)
    anagram_list.remove(first_word)
    play_game(anagram_list)

    

main()




        
    
    
    