#from tabnanny import check
from multiprocessing import resource_tracker
from anagrams import anagrams
import time
#import datetime
import random

lengths = [ 5, 6, 7, 8]
_word_list = []
_word_length = ""
_words_left = ""
_anagram_list = []
_guess_list = []
_first_word = ""
_game_over = False
_time_limit = 30
_start_time = ""
_elapsed_time = ""
_score = 0

#method to prompt for word lengths
def config_prompt():
    global _word_length

    try:
        _word_length  = int(input("Please enter a word length [5, 6, 7, 8]:"))

    except ValueError:
        print('Integers only please. Try again.')
        config_prompt()

    check_length(_word_length)

#method to check selected word length is valid    
def check_length(wl):
    global _word_length
    for length in lengths:
        if int(length) == int(_word_length):
            return _word_length
    try:
        _word_length = int(input("That is not a correct word length. Please try again [5, 6, 7, 8]:"))
        check_length(_word_length)

    except:
        print('Integers only please. Try again.')
        config_prompt()

#method to get the word list of chosen word length
def get_words(wl):
    global _word_list
    _word_list = anagrams[int(wl)]
    return _word_list

#method to drive game play
def play_game(alist):
    global _word_length
    global _words_left
    global _first_word
    global _game_over
    global _time_limit
    global _start_time
    global _anagram_list
    global _elapsed_time

    _anagram_list = alist

    _words_left = len(_anagram_list)
    #time_limit = 30
    #start_time = time.time()
    #loop to guess anagrams

    while not _game_over:
        _elapsed_time = time.time() - _start_time
        print("time elapsed is " , _elapsed_time) 
        #print(words_left)
        
        #get new list if current list is solved
        if _words_left == 0:
            print("You got all the anagrams for ", _first_word)
            get_words(_word_length)
            _anagram_list = random.choice(_word_list)
            print(" this list is ", _anagram_list)
            _first_word = random.choice(_anagram_list)
            _anagram_list.remove(_first_word)
            _word_list.remove(_anagram_list)
            play_game(_anagram_list)

  
        if _elapsed_time > _time_limit:
            _game_over = True
            end_game()
            
        print("The word is: " ,_first_word)
        print("There are ", _words_left, " unguessed anagrams")
        print("You have", _time_limit - int(_elapsed_time), " seconds left")
        guess = input("Make a guess: ")
        if _elapsed_time > _time_limit:
                print("Time is up!")
                print("Sorry, you didn't get that last on in on time.")
                end_game()
        check_guess(guess, _anagram_list)


#method to check if guess is correct
def check_guess(g, alist):
    global _anagram_list
    global _score
    global _words_left
    #global _elapsed_time
    global _time_limit

    _anagram_list= alist
    print(_anagram_list)

    for guess in _guess_list:
        if g.lower() == guess:
            print("You already got ", guess, ". Please try again")
            return

    for word in _anagram_list:

        if g.lower() == word:
            print(g, " is an anagram")
            _anagram_list.remove(word)
            _guess_list.append(g)
            print(_anagram_list)
            _words_left = len(_anagram_list)
            _score += 1
            return

    print("wrong you fucking dumbass")
    print(g, " is not a valid anagram, please try again")


#method to end game when time expires gives option to play again or quite
def end_game():
    global _game_over
    global _anagram_list
    
    print("Time is up, Game Over")
    print("you got ", _score, " anagrams for", _word_length,"-letter words!")
    _anagram_list = []
    play_again = input("Press enter to play again or any other key to quit: ")
    if play_again == "":
        print("you pressed enter ")
        _game_over = False
        main()
    else:
        print("ok bye dickhead")
        exit()

    
#Main method
def main():
    global _anagram_list
    global _first_word
    global _word_list
    global _word_length
    global _start_time
    global _elapsed_time
    global _score

    config_prompt()
    get_words(_word_length)
    print (_word_list)
    print(len(_word_list))
    _anagram_list = random.choice(_word_list)
    print(" this list is ", _anagram_list)
    _word_list.remove(_anagram_list)
    print(_word_list)
    _first_word = random.choice(_anagram_list)
    _anagram_list.remove(_first_word)
    _guess_list.append(_first_word)
    print("the guess list is ", _guess_list)
    _start_time = time.time()
    _elapsed_time = 0
    _score = 0
    play_game(_anagram_list)

    

main()




        
    
    
    