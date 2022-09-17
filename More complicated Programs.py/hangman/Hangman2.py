import sqlite3
'''
conn = sqlite3.connect('words.db')
cursor = conn.cursor()
cursor.execute('SELECT word FROM words;')
words = cursor.fetchall()
conn.close()
print(results)

DATABASE = "words.db"
'''

while True:
    tryagain = "NO"
    words = ["me", "ten", "good", "hello", "fruits"]
    conn = sqlite3.connect('words.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Word;')
    words = cursor.fetchall()
    conn.close()
    print(words)
    lives = 10
    hidden = "_" * len(words)
    while lives > 0:
        if hidden == word:
            print(hidden)
            break
        print(hidden)
        choice = input("Guess a letter: ").lower().strip(" ")
        flag = False
        for i in range(len(word)):
            if choice == word[i]:
                hidden = hidden[:i] + choice + hidden[i+1:]
                flag = True
        if flag:
            print("Correct!")
        else:
            print("No, that letter is't in the word :(")
    
    while tryagain == "NO":
        tryagain = input("Would you like to try again? y/n")
        if tryagain.lower() == "yes" or "y":
            print()
            

        if tryagain.lower() != 'y' or 'n' or 'yes' or 'no':
            print("Please enter y or n")
            tryagain = "NO"
    
            
        elif tryagain.lower() == "no" or "n":
            tryagain = "nope"
            print("Goodbye :(")
    

