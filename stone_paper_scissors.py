name = input("Enter your name:")
print(f"Welcome {name}, to Stone, paper, scissor game")

import random

user_score=0
comp_score=0

choices = ["stone","paper","scissor"]

rounds = int(input("How many rounds do you want to play: "))

for i in range(1,rounds+1):
    user = input("Enter your choice: ")
    comp = random.choice(choices)

    print("You choose = ",user)
    print("Computer choose = ",comp)

    if user == comp:
        print("Its is Tie")
    elif (user == "stone" and comp == "scissor") or (user == "paper" and comp == "stone") or (user == "scissor" and comp == "paper"):
        print("You win")
        user_score += 1
    else:
        print("Computer win")
        comp_score += 1


print("Now, its time to display final results ")

print(f"Your score: {user_score}")
print(f"Computer score : {comp_score}")

if user_score > comp_score:
    print("Congragulations, You win")
elif user_score < comp_score:
    print("Computer wins, better luck next time")
else:
    print("Match draw")    