

def split(shoes):
    return [char for char in shoes]
     
# Driver code
shoes = str(input())
l = (split(shoes))
t = 0
for i in range (len(l)):
    p = l[i]
    
    if p == "R":
        t = t+ 1
    else:
        t=t


if t == 2:
    print("Dorothy is in the classroom.")
elif t == 1:
    print("Hop along Dorothy and find that other shoe.")
elif t==0:
    print("Maybe Dorothy is in Kansas.")

