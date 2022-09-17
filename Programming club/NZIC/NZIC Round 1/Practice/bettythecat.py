p = int(input())
v = []
t = 0
num = input().split()
#v.append(num)
for i in range (p-1):
    a = num[i]
    if a == 0:
        v.append("2")
        t = 0
        print (f"\n{v}")
    if t > 2:
        v.append("2")
        t = 0
        print (f"\n{v}")
    else:
        v.append("1")
        t = t+1
        print (" ".join(v))

#print(v)
s=0
for ab in range(len(v)):
    noo = v[ab]
    if noo == "1":
        s = s+1
    if noo == "2":
        s=s

print (s)
