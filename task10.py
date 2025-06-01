#Task 10  Done
#      ***Mini Game: Rock, Paper, Scissorm(Single Round)***

print("***Mini Game: Rock, Paper, Scissorm(Single Round)***")

import random

user_choice = input("choose rock, paper, scissor: ")
options = ['rock','paper','scissor']
computer_choice = random.choice(options)
print(f"Computer chose:{computer_choice}")

if user_choice == computer_choice:
    print("Its a Tie")
elif (user_choice == 'rock' and computer_choice == 'scissor')or \
    (user_choice == 'paper' and computer_choice == 'rock')or \
    (user_choice == 'scissor' and computer_choice == 'paper'):
    print("You Win!")
else:
    print("You Lose!") 
