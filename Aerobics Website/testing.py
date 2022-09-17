'''mytuple=("a", "b", "c")
mylist = ["a", "b", "c"]
for item in mylist:
    mytuple.append(item)
    print(mytuple)'''
'''
t = list(mytuple)
print(t)
for item in t:
    t.remove(item)
    print(t)
mytuple = tuple(t)
print(mytuple)'''
'''
thistuple = ("apple", "banana", "cherry")
tup = ("c", "cherry" "banana")

a = ["a", "d", "c", "f"]
b = ["f", "c", "b", "a"]
all = []

for item in a:
    if item not in b:
        print(item)
        all.append(item)
        print(all)'''


'''for item in thistuple:
    thistuple = list(thistuple)
    tup = list(tup)
    if item in tup:
        print(item)
        thistuple.remove(item)

un = tuple(thistuple)
print(un)'''



'''
for item in y:
    y.remove(item)
    print(y)
thistuple = tuple(y)
print(thistuple)'''


scores = ["a", "b", "c", "d"]
placings = []
counter = 0
for item in scores:
    counter+=1
    print(counter)
    placings.append(counter)
    print(placings)
