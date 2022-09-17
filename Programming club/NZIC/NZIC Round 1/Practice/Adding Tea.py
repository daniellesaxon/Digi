'''
while True:

    teas = input.split()
    print (teas[0])
    if teas == "D": 
        break
print (teas)
'''
'''
teas = {
    "G":0,
    "C":0,
    "E":0,
    "P":0,
    "L":0,
    "S":0,
}
while True:
    t = input().split()


    print (t[0])

    break

for item in teas[1]:
    print (item)

print (teas)
'''



colors = {
    "blue" : "5",
    "red" : "6",
    "yellow" : "8",
}

def get_first_key(dictionary):
    for key in dictionary:
        return key
    raise IndexError

first_key = get_first_key(colors)
first_val = colors[first_key]
print (first_val)
print (first_key)

def get_nth_key(dictionary, n=0):
    n = n-1
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range") 

n = get_nth_key(colors, n = 2)

print (n)