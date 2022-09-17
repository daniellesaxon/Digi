#60 percent ANSWER

f = int(input())
c = input()
x = 0
z = 0

if f >2 and c[0] == c[1] == c[2]:
    if f%2 == 0:
        x = f/2
    else:
        x = (f/2)-0.5
else:
    for i in range(f-1):
        if c[i] == c[i+1]:
            x +=1
print(int(x))