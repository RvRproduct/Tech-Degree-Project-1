"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
Roberto Valentino Reynoso
7/22/2020
--------------------------------
"""

import random

end_number = 10
choice_number = 0
number_tries = 0
current_score = 9999
high_score = 9999


def random_answer(length_choice):
    return random.randint(1, length_choice)
    # write your code inside this function.


def choose_length():
    
    choose_length = ""
    
    while choose_length.lower() not in("no", "yes"):
        
        choose_length = input("would you like to change the length of the game? (Yes/No): ")
        
        if choose_length.lower() == "yes":
            
            try:
                choose_number = int(input("Create the length (1 - ?) choose end number: "))
            except ValueError:
                print("That it is not a valid value it must be a whole number.")
                
                choose_length = ""
                
                continue
            
            return choose_number
            
        elif choose_length.lower() == "no":
            
            print("We will go ahead and set it to the default setting")
            
            choose_number = 10
            
            return choose_number
            
        
def play_again():
    
    play_again = ""
    
    while play_again.lower() not in("yes", "no"):
        
        play_again = input("Would you like to start over and play again? (Yes/No): ")
        
        if play_again.lower() == "yes":
            
            return play_again
        
        elif play_again.lower() == "no":
            
            return play_again
            
def play_again_same():
    
    play_again = ""
    
    while play_again.lower() not in("yes", "no"):
        
        play_again = input("Would you like to play with the same length? (Yes/No): ")
        
        if play_again.lower() == "yes":
            
            return play_again
        
        elif play_again.lower() == "no":
            
            return play_again            

print("""               Welcome to the Number Guessing Game
-------------------------------------------------------------------
Goal: You must guess the right number from a range of numbers given
Info: * Number must be a whole number
      * If length isn't chosen it will be set at a default range of
      (1 - 10) the number range will always start at 1 but the ending
      number can be changed to increase the challenge. HighScore is
      shown after the first attempt, since one needs to be placed first!
      """)

while True:
    
    number_tries = 0
    end_number = choose_length()
    answer_number = random_answer(end_number)
    
    while True:
        
        number_tries += 1
        
        
        try:
            choice_number = int(input("Enter Guess: "))
        
        except ValueError:
            print("You must enter a whole number!")
            number_tries -= 1
            
            continue
        
        if choice_number == answer_number:
            print("You have guessed the right number!")
            current_score = number_tries
            print("Number of attempts: {}".format(number_tries))
            number_tries = 0
            
            if high_score > current_score:
                
                high_score = current_score
                
            another_round = play_again_same()
        
            if another_round.lower() == "yes":
                
                answer_number = random_answer(end_number)
                
                print("CURRENT HIGHSCORE (least amount of tries) Range from (1 - {}): {}".format(end_number, high_score))
            
                continue
            
            elif another_round.lower() == "no":
                
                high_score = 9999
            
            
                break
            
        elif choice_number > answer_number:
            if choice_number > end_number:
                print("Please enter a number within the range of (1-{}) Try again".format(end_number))
                number_tries -= 1
                continue
            print("Lower! Try again.")
            continue
            
        elif choice_number < answer_number:
            if choice_number < 1:
                print("Please enter a number within the range of (1-{}) Try again.".format(end_number))
                number_tries -= 1
                continue
            print("Higher! Try again.")
            continue
            
    another_round = play_again()
    
    if another_round.lower() == "yes":
        
        continue
        
    elif another_round.lower() == "no":
        
        break

print("\nThank you for playing!!! Bye bye.")