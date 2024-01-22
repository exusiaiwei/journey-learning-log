import random

player_score = 0

while True:
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter rock, paper, or scissors.")
    else:
        options = ["rock", "paper", "scissors"]
        opponent_choice = random.choice(options)

        print("Opponent's choice:", opponent_choice)

        if player_choice == opponent_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and opponent_choice == "scissors") or \
                (player_choice == "paper" and opponent_choice == "rock") or \
                (player_choice == "scissors" and opponent_choice == "paper"):
            print("You won!")
            player_score += 1
        else:
            print("You lost!")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break

print("Your score:", player_score)
