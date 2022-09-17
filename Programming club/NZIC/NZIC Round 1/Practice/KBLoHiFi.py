numofppl = int(input())
biddings = []
for i in range (numofppl):
    biddingprice = int(input())
    biddings.append(biddingprice)

print (biddings)
prices = []
for i in range (7):
    price = int(input())
    prices.append(price)

bought = []
choosing = []
for i in biddings:
    for s in prices:
        a = i-s
        if a<0:
            a=a
        else:
            choosing.append(a)
            choosing.sort()

        lastvalue = len(choosing)
        bought.append(choosing[lastvalue])
        

biddings.sort()
print (biddings)

            


