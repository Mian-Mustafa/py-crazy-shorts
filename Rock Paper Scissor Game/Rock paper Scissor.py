import random


choices = ["rock","paper","scissors"]
user = input("Choose rock ,paper , scissor :  ").lower()
comp = random.choice(choices)

print("computer Choose :",comp)
if user == comp:
    print("Draw")
elif (user == "rock" and comp == "scissors") or \
     (user == "scissors" and comp == "paper") or \
     (user == "paper" and comp == "rock"):
            print("you Win 🥇")
else:
    print("You Loose! 😢")