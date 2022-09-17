words = ["this", "great", "a", "list"]

'''
#this prints the rest of the list from the specified place
print(words[1:2])
#every second item 
print([words[::2]])
#from the start of the list until the secified place
print(words[:2])'''

'''
for i in range(3):
    print(words[i])

for word in words:
    print(word)'''

for i in range (4):
    if len(words[i])>=4:
        print(words[i])
    elif i ==1:
        print("this is the second word")
    else:
        print("too small, don't care")