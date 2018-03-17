#Users pick options
#computer picks
#compare and notify

import random
user = input("dear user => rock, paper , or scissors")
print("user choice" +" "+ user)

options = ["Rock", "Paper" , "Scissors"]
computer = random.choice(options)
print("Computer " + computer)


#still trying to fix this so you can only pick 1 of 3
if user != options:
  print("you typed bullshit")

elif user == computer:
  print("TIED BITCHES")

elif user == 'Rock':
  if computer == 'Paper':
    print("Rock may rip paper but paper covers rock so i guess you lose")

elif user == "Paper":
  if computer == "Scissors":
    print("YOU GOT CUT")

elif user == "Scissors":
  if computer == "Rock":
    print("ROCK SMASH")

else:
  print("you one or typed something random")