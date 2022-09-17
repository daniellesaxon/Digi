b = int(input())
w = []
price = []
for i in range (b):
    a = int(input())
    w.append(a)
p = int(input())
for i in range (p):
    a = int(input())
    price.append(a)

c = 1
w.sort()
price.sort()


'''
while True:
    item = w[b-c]
    print (w)
    if w == item:
        print (item)'''
