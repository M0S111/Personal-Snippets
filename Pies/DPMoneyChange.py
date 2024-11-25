def DPChange(amount):

    mincoins = [0]*(amount+1) #create an array of len(amount+1) to compensate for range func

    denoms = [1,3,4] #array of coin denominations to be iterated thru

    for m in range(1,len(mincoins)): #for each index of array indicating money amount

        mincoins[m] = 1000000000 #set m to v.large number
        
        for i in denoms: #for each coin denom for each amount
            if m >= i: #check if denom is less than or equal to amount
                numcoins = mincoins[(m-i)]+1 #if it is the number of coins needed is difference of amount & denom +1
                if numcoins < mincoins[m]: #if coins needed are less than minimum coins needed
                    mincoins[m] = numcoins #set minimum needed amount to coins needed

    return mincoins[-1]


print(DPChange(34))
