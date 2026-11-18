import random  # Load Python's built-in random module so the computer can pick at random


# Function that makes the computer's move
def get_computer_choice():
    # random.choice picks one item from the list at random and returns it
    return random.choice(["rock", "paper", "scissors"])


# Function that decides who won a round; takes both players' choices as input
def determine_winner(player, computer):
    # If both picked the same thing, nobody wins
    if player == computer:
        return "tie"
    # Dictionary mapping each choice to the choice it beats
    # e.g. "rock" beats "scissors"
    wins_against = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    # Look up what the player's choice beats; if that's the computer's choice, player wins
    if wins_against[player] == computer:
        return "player"
    # Not a tie and the player didn't win, so the computer won
    return "computer"


# Main function that runs the whole game
def play():
    print("Rock, Paper, Scissors!")  # Show the game title
    print("Type 'quit' to exit.\n")   # Tell the user how to stop (\n adds a blank line)

    # Start both scores at zero
    player_score = 0
    computer_score = 0

    # Loop forever until we hit a "break" (when the user types quit)
    while True:
        # Ask for input; .strip() removes extra spaces, .lower() makes it lowercase
        # so "  ROCK " becomes "rock"
        player = input("Your choice (rock/paper/scissors): ").strip().lower()

        # If the user wants to stop, show the final score and exit the loop
        if player == "quit":
            print(f"\nFinal Score — You: {player_score} | Computer: {computer_score}")
            break  # Leaves the while loop, ending the game

        # If the input isn't one of the valid options, warn the user
        if player not in ("rock", "paper", "scissors"):
            print("Invalid choice. Try again.\n")
            continue  # Skip the rest of this loop and ask again

        # Get the computer's random choice and show it
        computer = get_computer_choice()
        print(f"Computer chose: {computer}")

        # Figure out who won this round: "tie", "player", or "computer"
        result = determine_winner(player, computer)

        # Print the result and update the score
        if result == "tie":
            print("It's a tie!\n")
        elif result == "player":
            print("You win!\n")
            player_score += 1     # Add 1 to the player's score
        else:
            print("Computer wins!\n")
            computer_score += 1   # Add 1 to the computer's score

        # Show the running score after each round
        print(f"Score — You: {player_score} | Computer: {computer_score}\n")


# This is True only when the file is run directly (e.g. `python Rock.py`),
# not when it's imported into another file
if __name__ == "__main__":
    play()  # Start the game
