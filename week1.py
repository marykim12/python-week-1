import random
def play_rounds():
    choices = ("rock","paper","scissors")
    player_choice = input("Enter choice: ").lower()
    print(f"player:{player_choice}")

    if player_choice not in choices:
        print("not valid")
        return 0,0
    computer = random.choice(choices)
    print(f"computer:{computer}")


    if player_choice == computer:
        return 0,0
    elif (player_choice == "rock" and computer == "scissors") or \
         (player_choice == "paper" and computer == "rock") or \
         (player_choice == "scissors" and computer == "paper"):
        return 1,0
    else:
        return 0,1

def play_game():
    player_score = 0
    computer_score = 0

    for _ in range(3):
        players_points, computer_points = play_rounds()
        player_score += players_points
        computer_score += computer_points

    print(f"player: {player_score}")
    print(f"computer: {computer_score}")

    if player_score > computer_score:
        print ("player wins")
    elif computer_score > player_score:
        print("computer wins")
    else:
        print("its a tie!")


if __name__ == "__main__":
    play_game()
