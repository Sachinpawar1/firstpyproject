import random

user_wins = 0
computer_wins = 0
options = ["rock", "scissors", "paper"]

while True:
    user_input = input("Type Rock or Paper or Scissors to play and Type Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock : 0, paper: 1, scissors 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick+ ".")

    if user_input == "rock" and computer_pick == "Scissors":
        print("you won")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("you won")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("you won")
        user_wins += 1

    elif user_input == computer_pick:
        print("You and computer are tied")

    else:
        print("You lost!")
        computer_wins += 1

print(f'you won {user_wins}, computer wins {computer_wins}')
print("See you again!")
