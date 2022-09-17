a = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "k", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def split(word):
    return [char for char in word]

string = input()

s = split(string)

length = len(string)

total = 0

for i in range (length):
    index = a.index(s[i])
    prev = a.index(s[i-1])
    smaller = min(index, prev)
    print (smaller)
    #tfw = 
    print(s[i])
    if i ==0:
        if s[i] == "A":
            total+=1
        if s[i] == "B":
            total+=2
    else:
        if s[i] == s[i-1]:
            total+=1
        elif s[i] != s[i-1]:
            total+=2

print(total)



