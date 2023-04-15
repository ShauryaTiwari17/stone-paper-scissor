import random

user_Action = input("Enter your choice(stone,paper,scissor)\n")
possible_Actions = ["stone","paper","scissor"]
computer_Actions = random.choice(possible_Actions)
print(f"\nyou chose{user_Action}, computer choses {computer_Actions}.\n")

if user_Action == computer_Actions:
    print(f"Both players are selected {user_Action}.its a tie!")
elif user_Action == "stone":
    if computer_Actions == "scissor":
        print("You win ! stone smashes the scissor")
    else:
        print("You lose! paper covers the stone ")
elif user_Action == "paper":
    if computer_Actions == "stone":
        print("You win! paper covers the stone")
    else:
        print("You lose! scissor cuts  the paper")
elif user_Action == "scissor":
    if computer_Actions == "paper":
        print("You win! scissor cuts the paper")
    else:
        print("You lose! stone smashes  the .k       .scissor")                