num, min, max = int(input().split())
good = 0
days = int(input().split())
for i in range (num-1):
    if min<=days<=[i]:
        good +=1
