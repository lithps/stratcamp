# import random module
import random

# player 1 name
player1 = input("Player 1, enter your name: ")
player2 = input("Player 2, enter your name: ")

# generate 2 random numbers between 1 and 6 for player 1
player1_roll1 = random.randint(1, 6)
player1_roll2 = random.randint(1, 6)
# sum the 2 rolls
player1_sum = player1_roll1 + player1_roll2

# generate 2 random numbers betwen 1 and 6 for player 2
player2_roll1 = random.randint(1,6)
player2_roll2 = random.randint(1,6)
# sum the 2 rolls
player2_sum = player2_roll1 + player2_roll2

# if statement to determine the winner
def winner():
    if player1_sum > player2_sum:
        print(f"{player1} wins!")
    else:
        print(f"{player2} wins!")

print(f"{player1}'s score: {player1_sum}")
print(f"{player2}'s score: {player2_sum}")
winner()

