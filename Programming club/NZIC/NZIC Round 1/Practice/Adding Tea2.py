def get_nth_key(dictionary, n=0):
    n = n-1
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range") 

teas = {
    "G":0,
    "C":0,
    "E":0,
    "P":0,
    "L":0,
    "S":0,
}
print (teas)
while True:
    t = input().split()
    
    print (t)
    for i in range (6):
        if t[0].capitalize() == get_nth_key(teas, i):
            l = t[0].capitalize
            print ("yes")
            teas[l]=t[1]
        else:
            print ('no')


