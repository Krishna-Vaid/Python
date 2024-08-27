import random

options = ("rock", "paper", "scissors")
playing = True

# Initialize counters for wins
player_wins = 0
computer_wins = 0

while playing:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
        player_wins += 1  # Increment player win counter
    else:
        print("You lose!")
        computer_wins += 1  # Increment computer win counter

    print(f"Player Wins: {player_wins} | Computer Wins: {computer_wins}")  # Display the score

    play_again = input("Play again? (yes/no): ").lower()
    if play_again == "yes":
        playing = True
    else:
        playing = False

print("Game Over")
print(f"Final Score - Player Wins: {player_wins} | Computer Wins: {computer_wins}")  # Display final score
