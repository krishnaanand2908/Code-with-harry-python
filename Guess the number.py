number = 18
guess = 1
print("You have a total of 9 guesses!") 
while(guess <= 9):
    guessed = int(input("Guess the number:\n"))
    if guessed > 18:
        print("Your number is greater than the number to be guessed!\n")
        continue
    elif guessed < 18:
        print("Your number is smaller than the number to be guessed!\n")
        continue
    else:
        print("Congratulations! You guessed the number!")
        print("You took", guess, "number of guesses to solve!")
        break
    print(9 - guess, "number of guesses left")   