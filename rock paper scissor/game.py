import random
item_list = ["rock" ,"paper" ,"scissor"]
user_choice= input("Enter your move = rock, paper, scissor : ")
comp_choice= random.choice(item_list)

print(f"User choice = {user_choice}, computer_choice = {comp_choice}")

if user_choice == comp_choice :
    print("Both chooses same : MATCH TIE!")

elif user_choice == "rock":
    if comp_choice == "paper":
     print("Paper covers rock : COMPUTER WINS!")
    else:
        print("Rock smashes scissors : YOU WIN!")

elif user_choice == "paper":
    if comp_choice == "scissor":
        print("scissor cuts paper : COMPUTER WINS!")
    else:
        print("Paper covers rock : YOU WIN!")
        
elif user_choice == "scissor":
    if comp_choice == "rock":
        print("rock smashes scissors : COMPUTER WINS!")
    else:
        print("scissor cuts paper : YOU WIN!")
