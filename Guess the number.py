number = 30
guess = 1
print("You have to guess a number between 1 to 100.\nYou have a total of 9 guesses!") 
while(guess <= 9):
    guessed = int(input("Guess the number:\n"))
    if guessed > 30:
        print("Your number is greater than the number to be guessed!\n")
        print(9 - guess, "number of guesses left")  
        guess = guess + 1 
        continue
    elif guessed < 30:
        print("Your number is smaller than the number to be guessed!\n")
        print(9 - guess, "number of guesses left")   
        guess = guess + 1
        continue
    else:
        print("Congratulations! You guessed the number!")
        print("You took", guess, "number of guesses to solve!")
        guess = guess + 1
        break
    
if guess > 9:
    print("GAME OVER")
    
    