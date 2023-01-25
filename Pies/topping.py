pie=True

while pie:
    topping=input("\nPlease enter desired topping or stop to end.")

    if topping.title()=='Stop':
        pie=False

    else:
        print('\n',topping.title()+" added to your pizza.")
    
    
    
