import random

from numpy import where
words = ["comment", "hangman", "awesome"]
word = random.choice(words)
print(word)
hidden = "_" * len(word)
print(hidden)
used = []
d = 0
lives = 10
for i in range(10):

    guess = input("Guess a letter: ")
    if guess in word:
        while guess in word:
            print("yay!")
            for n in range(len(word)-1):
                if word[n] == guess:
                    if hidden[n] == "_":
                        d +=1
                        if n == 0:
                            hidden = (f"{guess}{hidden[n+d::]}")
                            print(hidden)
                            print(word)
                        else:
                            hidden = (f"{hidden[:n]}{guess}{hidden[n-1::]}")
                            print(hidden)
                            print(word)
            print(f"You have {lives} lives left")
            guess = input("Guess a letter: ")
            
            #a[:4]+" are " +a[8:]
    else:
        lives -=1
        print("no")
        print(f"You have {lives} lives left")

