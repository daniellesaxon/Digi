s = input()
g, b, r, bl, br, m, c = 0, 0, 0, 0, 0, 0, 0

def x(l, m):
    if l%2 !=0:
        print(f"A {m} shoe has no partner.")
        c+=1
        return c

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
    
x(g, "Green")
x(b, "Black")
x(r, "Red")
x(bl, "Blue")
x(br, "Brown")
x(m, "Mustard")

if c == 0:
    print("All paired up!")