ppl, step = list(map(int,input().split()))

while True:
    a = []
    p = 0
    t = 0
    for i in range (1,ppl+1):
        a.append(i)
    while True:
        t +=1
        remove = (step-1)+p
        p+=step*(t)
        if p>len(a):
            p = len(a)%step
            t = 0
        a.pop(remove)
        print(a)
