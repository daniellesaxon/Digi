#pick a currency and make sure it is valid
valid = ["usd", "USD", "zwl", "ZWL", "AUD", "aud", "vnd", "VND"]
def pick_a_currency():
    while True:
        currency = input("What currency would you like to convert to? Zimbabwean dollar (ZWL), US dollar (USD), Vietnamese Dong (VND), or Australian Dollar (AUD). ")
        if currency in valid:
            return currency
        else:
            print("Pick a valid currency")

def yes_or_no(parameter, input1):

    parameter = input(input1)
    while parameter.lower() not in YES_NO:
            parameter = input(f"{input1}Please pick either yes (y) or no (n): ")
    if parameter.lower() in YES_NO:
        return parameter.lower()     

while True:
    while True:
        #currency is the string that is returned
        currency = pick_a_currency()

    #Ask user to input a number (the amount of money in NZD)
        while True:
            try:
                nzd = float(input("What amount would you like to convert? (enter an amount in NZD)"))
                if nzd <= 0:
                    print("That isnt a valid option, try again")
                else:
                    break
            except:
                print ("That isnt a valid option, try again")

        #make the calulations depending on what the user choose
        if currency == "zwl" or currency == "ZWL":
            print(f"Converting ${nzd}NZD to ZWL...")
            print(nzd*16.05)
            break
        if currency == "usd" or currency == "USD":
            print(f"Converting ${nzd}NZD to USD...")
            print(nzd*0.74)
            break
        if currency == "aud" or currency == "AUD":
            print(f"Converting ${nzd}NZD to AUD...")
            print(nzd*0.94)
            break
        if currency == "vnd" or currency == "VND":
            print(f"Converting ${nzd}NZD to VND...")
            print(nzd*16985.55)
            break
#        #elif currency<0:
#            #print ("That is not a possible option, pick a valid currency (ZWL, USD, VND, AUD)")
#        else:
#            print ("That is not a possible option, pick a valid currency (ZWL, USD, VND, AUD)")
    play_again = "n"
    while play_again != "y":
        play_again = input("Would you like to try again? (Y or N)")

        if play_again.lower() == "n":
            print("Goodbye :(")
            break
        elif play_again.lower() != "y":
            print("That isnt a valid option")
            
        else:
            print()
            break
    
        

 


