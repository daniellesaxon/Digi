

s = input()
g, b, r, bl,br, m = 0, 0, 0, 0, 0, 0
c = []

def x(v, Word, c):
    if v%2 !=0:
        print(f"A {Word} shoe has no partner.")
        print(c)
    else:
        c.append("a")
        print(c)

for i in range (len(s)):

    if s[i] == "G":
        g +=1
    elif s[i] == "B":
        if i+1 == len(s):
            b+=1
        elif s[i+1] == "l":
            bl+=1
        elif s[i+1] == "r":
            br+=1
        else:
            b+=1
    elif s[i] == "R":
        r+=1
    elif s[i] == "M":
        m+=1

x(g, "Green", c)
x(b, "Black", c)
x(r, "Red", c)
x(bl, "Blue", c)
x(br, "Brown", c)
x(m, "Mustard", c)

if c[0] == "a":
    print("All paired up!")