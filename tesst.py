n=50
no_of_guesses_left=9
no_of_guesses_took=0
i=9
print("Guess the number")
while(i==9):
  if no_of_guesses_took==9:
      print("GAME OVER!!!")
      break
  x=int(input())
  if x==n:
    print("winner winner chicken dinner")
    print("no of guesses took",no_of_guesses_took+1)
    print("no of guesses left",no_of_guesses_left-1)
    break
  elif x>n:
    print("you entered greater number!! GUESS AGAIN")
  else:
    print("you entered smaller number!! GUESS AGAIN")

  no_of_guesses_left-=1
  no_of_guesses_took+=1
  print("no of guesses took",no_of_guesses_took)
  print("no of guesses left",no_of_guesses_left)
