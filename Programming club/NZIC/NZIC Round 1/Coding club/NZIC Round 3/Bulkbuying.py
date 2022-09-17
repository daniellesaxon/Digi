numofduck = int(input())
costof2 = int(input())
costof3 = int(input())

if costof2/2 == costof3/3:
    if numofduck%2 == 0:
        price = (numofduck/2)*costof2 
        print(int(float(price)))
    elif numofduck%3 == 0:
        price = (numofduck/3)*costof3
        print(int(float(price)))
    elif numofduck%2 == 1:
        price = costof3
        remain = numofduck-3
        price += (remain/2)*costof2
        print(int(float(price)))
if costof3/3<costof2/2:

    if numofduck%3==0:
        numofbuys = numofduck/3
        
        price = int(numofbuys*costof3)
        print(int(float(price)))
    else:

        r = numofduck%3

        if r == 1:

            price = costof2
            amountofducks = numofduck-2
            if amountofducks%3 !=0:
                price += costof2
                amountofducks = amountofducks-2
            price += (amountofducks/3)*costof3
        elif r == 2:

            num = numofduck-2
            price = (num/3)*costof3
            price += costof2
        print(int(float(price)))

if costof2/2<costof3/3:
    if numofduck%2==0:
        numofbuys = numofduck/2
        price = int(numofbuys*costof2)
        print(price)
    else:

        r = numofduck%2

        if r == 1:

            price = costof3
            amountofducks = numofduck-3
            price += (amountofducks/2)*costof2

        print(int(float(price)))






