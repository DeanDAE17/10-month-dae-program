# Load Python's built-in random module so the computer can pick at random
import random

# Function that makes the computer's move
def get_computer_choice():
    # random.choice picks one item from the list at random and returns it
    return random.choice(["rock", "paper", "scissors"])

# Function that decides who won a round; takes both players' choices as input
def determine_winner(player, computer):
    # If both picked the same thing, nobody wins
    if player == computer:
        return "tie"
    # Dictionary mapping each choice to the choice it beats (e.g. "rock" beats "scissors")
    wins_against = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    # Look up what the player's choice beats; if that's the computer's choice, player wins
    if wins_against[player] == computer:
        return "player"
    # Not a tie and the player didn't win, so the computer won
    return "computer"

# Main function that runs the whole game
def play():
    # Show the game title and how to stop (\n adds a blank line)
    print("Rock, Paper, Scissors!")
    print("Type 'quit' to exit.\n")

    # Start both scores at zero
    player_score = 0
    computer_score = 0

    # Loop forever until we hit a "break" (when the user types quit)
    while True:
        # Ask for input; .strip() removes extra spaces, .lower() makes it lowercase
        player = input("Your choice (rock/paper/scissors): ").strip().lower()

        # If the user wants to stop, show the final score and leave the loop
        if player == "quit":
            print(f"\nFinal Score — You: {player_score} | Computer: {computer_score}")
            break

        # If the input isn't a valid option, warn the user and ask again
        if player not in ("rock", "paper", "scissors"):
            print("Invalid choice. Try again.\n")
            continue

        # Get the computer's random choice and show it
        computer = get_computer_choice()
        print(f"Computer chose: {computer}")

        # Figure out who won this round: "tie", "player", or "computer"
        result = determine_winner(player, computer)

        # Print the result and add 1 to the winner's score
        if result == "tie":
            print("It's a tie!\n")
        elif result == "player":
            print("You win!\n")
            player_score += 1
        else:
            print("Computer wins!\n")
            computer_score += 1

        # Show the running score after each round
        print(f"Score — You: {player_score} | Computer: {computer_score}\n")

# True only when the file is run directly (e.g. `python Rock.py`), then start the game
if __name__ == "__main__":
    play()
