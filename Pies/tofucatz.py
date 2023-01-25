spam = ['apples','bananas','tofu','cats','cherries','melons']

n=len(spam)

print(n)

while n>0:
    print(spam[n-1]+",")
    n-=1

    
    if n==3:
        print(spam[-2]+"")
        
    if n==5:
        print("and",spam[-1])
    



##print(spam[-5]+",",spam[-4]+",",spam[-3]+",",spam[-2],"and",spam[-1])
