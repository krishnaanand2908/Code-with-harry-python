while (True):
    num1 = float(input("Please enter a number here:\n"))
    if num1 > 100:
        print("You are very smart!")  
        break
    
    elif num1 == 100:
        print("Very close! TRY AGAIN:\n")
        
    else:
        print("An error occured, please try again:\n")
        continue
