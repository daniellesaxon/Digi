'''this code was created by Danielle Saxon on the 30/03/2021
this code will create a random passowrd for the user using paramerters of the users choosing'''

import random

#function to determine whether the answer is yes or no, and if not, get a y/n answer
def yes_or_no(name_of_type):

    parameter = input(f"Would you like {name_of_type} y/n: ")
    while parameter.lower() not in YES_NO:
            parameter = input(f"Would you like {name_of_type} Please pick either yes (y) or no (n): ")
    if parameter.lower() in YES_NO:
        return parameter.lower()    

#one function to choose all characters
def pick_characters(type_of_character, list, amount_in_list):
    for _ in range (length):
        if type_of_character in YES:
            password.append(list[random.randint(0, amount_in_list)])

#possible leters, numbers, and symbols to choose from
LETTERS_OPTIONS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
NUMBERS_OPTIONS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS_OPTIONS = ['!', '#', '&', '%', '/', '-', '_', '*', '@', '(', ')', '$']
#options for the questions 
YES_NO = ["y", "n", "yes", "no"]
YES = ["y", "yes"]
NO = ["n", "no"]
#this needs to be there for the while loop
playagain = "y"

#at the end when the user asks to generate another password, if they choose no the code will not go back to here
while playagain in YES:
    #every time a new password is created, these lists will all be empty
    password = []
    final_password = []
    number_of_types = 0

    #ask user what length they would like and only accept y or n
    while True:
        try:
            length = int(input("How long would you like your password to be (max 15, min 3)?: "))
            if length < 3:
                print("That isn't a valid option. Try again")
            elif length > 15:
                print("That isn't a valid option. Try again")
            else:
                break
        except:
            print("That isn't a valid length. Try again")
    while True:
        has_letters = yes_or_no("letters in your password?")
        has_numbers = yes_or_no("numbers in your password?")
        has_symbols = yes_or_no("symbols in your password?")


        
    #if the user picks no for all three ask them to choose
    #use functions to pick everything 
        if has_letters in YES or has_numbers in YES or has_symbols in YES:
            pick_characters(has_letters, LETTERS_OPTIONS, 25)
            pick_characters(has_numbers, NUMBERS_OPTIONS, 9)
            pick_characters(has_symbols, SYMBOLS_OPTIONS, 11)
            break    
        else:
            print("Please pick yes for at least one parameter")     

    #ensure that the required characters are in the password so that there is a 100% chanvec that the type of charcters you choose will be in the password

    if has_letters in YES:
        number_of_types =  number_of_types+1
        final_password.append(LETTERS_OPTIONS[random.randint(0, 25)])
    if has_numbers in YES:
        number_of_types =  number_of_types+1
        final_password.append(NUMBERS_OPTIONS[random.randint(0, 9)])
    if has_symbols in YES:
        number_of_types =  number_of_types+1
        final_password.append(SYMBOLS_OPTIONS[random.randint(0, 11)])

    #shuffle the password so it isnt *letters, numbers, symbols*
    (random.shuffle(password))

    #add the password to a new list, only choosing the amount of characters the user specified in the list
    for x in range (0, length-number_of_types):
        final_password.append(password[x])
    (random.shuffle(final_password))
    print("Your password is:",''.join(final_password))
    playagain = yes_or_no("to generate another password?")

    #determine whether to generate another password
    if playagain in NO:
        print("Goodbye :(")
    else:
        print()  