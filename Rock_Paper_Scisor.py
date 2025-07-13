from datetime import datetime
import random

computer_dict = {-1: "Rock", 0: "Paper", 1: "Scissors"}
player_dict = {"R": -1, "P": 0, "S": 1}

wins = 0
losses = 0


def Play_Main():
    global wins, losses

    print("'R' : Rock\n'S' : Scissors\n'P' : Paper")

    computer_choice = random.choice([-1, 0, 1])

    while True:
        players_choice = input("\nEnter Your Choice: ").upper()
        if players_choice in player_dict:
            break
        else:
            print("Enter a valid choice (R, P, or S)")

    playerNum = player_dict[players_choice]

    print(f"You chose: {computer_dict[playerNum]}")
    print(f"Computer chose: {computer_dict[computer_choice]}")

    if playerNum == computer_choice:
        print("It's a Draw")
    elif (computer_choice - playerNum == -1) or (computer_choice - playerNum == 2):
        print("You Win")
        wins += 1
    else:
        print("You Lose")
        losses += 1


def save_score(wins, losses, filename="scores.txt"):
    today = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")
    new_entry = f"{today} {current_time} - Wins: {wins}, Losses: {losses}\n"

    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    highest_today = 0
    for line in lines:
        if line.startswith(today):
            try:
                win_count = int(line.split("Wins:")[1].split(",")[0].strip())
                highest_today = max(highest_today, win_count)
            except:
                continue

    if wins > highest_today:
        new_entry += f"NEW HIGH SCORE for {today}: {wins} wins!\n"

    with open(filename, "a") as file:
        file.write(new_entry)

    print("Score saved successfully.")


while True:
    Play_Main()
    play_again = input("\nDo you want to play again? (Y/N): ").lower()
    print()
    if play_again != "y":
        print("Thanks for playing!")
        print(f"Total Wins: {wins}")
        print(f"Total Losses: {losses}")
        save_score(wins, losses)
        break
