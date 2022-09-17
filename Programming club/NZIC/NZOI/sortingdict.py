a = {
    "c": 2,
    "b": 5,
    "a":1
}

list_a  = list(a.items())
list_a.sort()
print(list_a)

for key, value in list_a:

    print(key)
    print(a[key])
'''list_a.sort()
d = dict(list_a)
print(d)'''
