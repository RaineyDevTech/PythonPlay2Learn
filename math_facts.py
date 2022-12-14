import random
import time

operations = ["+", "-", "x", "/"]
_game_over = False
time_limit = 30
_score = 0

#method to drive game play
def play_game(op, mn):

    global game_over
    global _score

    print("your operator is ", op)
    print("your max number is ", mn)
    start_time = time.time()

    while not _game_over:
        elapsed_time = time.time() - start_time
        #print(elapsed_time) 

        a = random.randint(2, mn)
        b = random.randint(2,mn)
        

        if elapsed_time > time_limit:
            game_over = True
            end_game()

        if op == "+":
            try:
                answer = int(input(F'{a} + {b} = '))

            except:
                print("answer must be an integer")
                print("You have ", time_limit - int(elapsed_time), " seconds left")
                continue

            #answer = input(a , " + ", b, " = ")
            print("You have ", time_limit - int(elapsed_time), " seconds left")
            if answer == a+b:
                print(answer, " is correct!")
                _score += 1
                print("Score : ", _score)
                continue
            else:
                print(answer, " is not correct. Try again!")
                continue


        if op == "-":
            try:
                answer = int(input(F'{a} - {b} = '))
            except:
                print("answer must be an integer!")
                print("You have ", time_limit - int(elapsed_time), " seconds left")
                continue
            #answer = input(a , " + ", b, " = ")
            print("You have ", time_limit - int(elapsed_time), " seconds left")
            if answer == a-b:
                print(answer, " is correct!")
                _score += 1
                print("Score : ", _score)
                continue
            else:
                print(answer, " is not correct. Try again!")
                continue

        
        if op == "x":

            try:
                answer = int(input(F'{a} x {b} = '))
            except:
                print("answer must be an integer!")
                print("You have ", time_limit - int(elapsed_time), " seconds left")
                continue
            
            print("You have ", time_limit - int(elapsed_time), " seconds left")
            if answer == a*b:
                print(answer, " is correct!")
                _score += 1
                print("Score : ", _score)
                continue
            else:
                print(answer, " is not correct. Try again!")
                continue


        if op == "/":
            try:
                print("Round answers to two decimal places")
                #print(float(round(a/b,2)))
                answer = float(input(F'{a} / {b} = '))
            except:
                print("answer must be a float!")
                print("You have ", time_limit - int(elapsed_time), " seconds left")
                continue
            
            print("You have ", time_limit - int(elapsed_time), " seconds left")
            #print("answer is ", a/b)
            if answer == float(round(a/b,2)):
                if time_limit - int(elapsed_time) < 1:
                    print("Sorry you didn't get that one in time")
                    end_game()
                print(answer, " is correct!")
                _score += 1
                print("Score : ", _score)
                continue
            else:
                print(answer, " is not correct. Try again!")
                continue

        
            
 #method to set game configuration      
def config_prompt():
    #print(operations)
    operator = input("Please enter an operation [+, -, x, /]: ")
    #print("you chose ", operator)
    for operation in operations:
        if operator == operation:
            try:
                max_number = int(input("Please enter a max number between 1 and 100:" ))

            except ValueError:
                print('Integers only please. Try again.')
                config_prompt()

            if max_number > 1 and max_number <100:
                play_game(operator, max_number) 

            else:
                print("The Max number must be greater than 1 and less than 100!")
                print("Please try again!")
                config_prompt()

    print("Please choose a valid operator")
    config_prompt()

def end_game():
    global game_over
    global _score
    print("Time is up, Game Over!")
    print("You answered ", _score, " problems!")
    play_again = input("Press enter to play again or any other key to quit: ")
    if play_again == "":
        print("you pressed enter ")
        game_over = False
        _score = 0
        config_prompt()
    else:
        print("Bye, Thanks for playing!")
        exit()
    

config_prompt()
