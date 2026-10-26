import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    wins_against = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    if wins_against[player] == computer:
        return "player"
    return "computer"

def play():
    print("Rock, Paper, Scissors!")
    print("Type 'quit' to exit.\n")

    player_score = 0
    computer_score = 0

    while True:
        player = input("Your choice (rock/paper/scissors): ").strip().lower()

        if player == "quit":
            print(f"\nFinal Score — You: {player_score} | Computer: {computer_score}")
            break

        if player not in ("rock", "paper", "scissors"):
            print("Invalid choice. Try again.\n")
            continue

        computer = get_computer_choice()
        print(f"Computer chose: {computer}")

        result = determine_winner(player, computer)

        if result == "tie":
            print("It's a tie!\n")
        elif result == "player":
            print("You win!\n")
            player_score += 1
        else:
            print("Computer wins!\n")
            computer_score += 1

        print(f"Score — You: {player_score} | Computer: {computer_score}\n")

if __name__ == "__main__":
    play()
