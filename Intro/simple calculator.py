from types import TracebackType
from unicodedata import digit


def add():
    while True:
        try:
            a = float(input("What is the first number you would like to use?"))
            break
        except:
            print("Please enter a number")

    while True:
        try:
            b = float(input("What is the second number you would like to use?"))
            break
        except:
            print("Please enter a number")
        
    answer = a+b
    return answer

def subtract():
    while True:
        try:
            a = float(input("What is the first number you would like to use?"))
            break
        except:
            print("Please enter a number")

    while True:
        try:
            b = float(input(f"How much would you like to subtract {a} by?"))
            break
        except:
            print("Please enter a number")
    answer = a-b
    return answer

def divide():
    while True:
        try:
            a = float(input("What is the first number you would like to use?"))
            break
        except:
            print("Please enter a number")

    while True:
        try:
            b = float(input(f"How much would you like to divide {a} by?"))
            break
        except:
            print("Please enter a number")
        print("Please enter a number")
    answer = a/b
    return answer

def multiply():
    while True:
        try:
            a = float(input("What is the first number you would like to use?"))
            break
        except:
            print("Please enter a number")

    while True:
        try:
            b = float(input(f"How much would you like to multiply {a} by?"))
            break
        except:
            print("Please enter a number")
        print("Please enter a number")
    answer = a*b
    return answer

def subtract (a, b):
    answer = a-b
tryagain = "y"
while True:
    #choose what function to use
    shortcuts = ["a", "s", "d", "m"]
    symbol = " "
    while symbol not in shortcuts:
        symbol = input("What function would you like to use? \na = add \ns = subtract \nd = divide \nm = multiply\nc = find the circumfrence of a circle\nr = find the area of a circle \n")
        if symbol.lower() in shortcuts: 
            break


    if symbol.lower() == "a":
        print((f"Answer = {add()}"))
    elif symbol.lower() == "s":
        print((f"Answer = {subtract()}"))
    elif symbol.lower() == "d":
        print((f"Answer = {divide()}"))
    elif symbol.lower() == "m":
        print((f"Answer = {multiply()}"))


    
    while True:

        tryagain = input("Would you like to try again? y/n")


        
            
        if tryagain.lower() == "y":
            print()
            break
        elif tryagain.lower() == "n":
            print("bye")
            
        elif tryagain.lower() != "y":
            print("Please enter a valid option")
        break

    break

            

