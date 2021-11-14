import random

player_wins = 0
computer_wins = 0
winner = ""

def computer_turn():
    options = ["rock","paper","scissors"]
    return options[random.randint(0,2)]


while player_wins < 3 and computer_wins < 3:
    while True:
        player_choice = input("Rock, paper or scissors? ").lower()
        if player_choice not in ["rock","paper","scissors"]:
            print("Choose from rock, paper or scissors only!")
            continue
        else:
            break
    computer_choice = computer_turn()
    print(f"The computer chose: {computer_choice}")
    if computer_choice == player_choice:
        print("It was a draw!")
    elif (computer_choice == "rock" and player_choice == "scissors") \
            or (computer_choice == "scissors" and player_choice == "paper")\
            or (computer_choice == "paper" and player_choice == "rock"):
        print("Computer wins!")
        computer_wins += 1
    else:
        print("You win!")
        player_wins += 1
    print(f"You need {3 - player_wins} wins to beat the computer.")
    print(f"The computer needs {3 - computer_wins} wins to beat you.")
    print("*"*35)
else:
    if computer_wins == 3:
        print("Oh dear, the computer has won!")
    elif player_wins == 3:
        print("Congratulations, you win!")
print("Game over!")

