'''words = ["these", "are", "words"]
words.append("really")
print(words)
print(words[1])
print(words.pop()) #leaving pop empty will remove the last word in the list
print(words)

a = words.pop(0)
print (a)
print(len(words))'''
 #####

'''a = "this is words"
print(a[0])
a = "B" +a[1:] #: is the rest of a str
print(a)

words = ["these", "are", "words"]
words.append("really")
print(words)
words[1] = "bob"
words.insert(0, "really") #add words to a specific place in the list - list.insert(index, item)
print(words)'''

a = "this is words"
a = a[:4]+" are " +a[8:]
print(a)