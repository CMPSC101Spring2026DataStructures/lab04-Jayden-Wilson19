
# Basic Rock Paper Scissors Game
# Name: Jayden Wilson
# Date: 2/27/26 (new due date)

import random

"""
main.py
---------
Rock Paper Scissors game for CS101 Fall 2025 Lab 02.
This script allows a user to play a 3-round game of Rock, Paper, Scissors against the computer.
It uses the 'rich' library for colorful output.
"""

import random
from rich.console import Console
from rich.text import Text


console = Console()
"""
main.py (Starter Template)
-------------------------
Rock Paper Scissors game for CS101 Fall 2025 Lab 02.

Complete the TO-DOs to finish the game!
"""

import random
from rich.console import Console

console = Console()

choices = ['rock', 'paper', 'scissors']
num_to_choice = {'1': 'rock', '2': 'paper', '3': 'scissors'}


def get_user_choice():
	"""
    Code to get the user's choice of rock, paper, or scissors.

	It prompts the user until a valid input is received.
    """
	input_prompt = "Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors):"
	
	while True:
		user_input = input(input_prompt).strip()
		if user_input in num_to_choice:
			return num_to_choice[user_input]
		else:
			console.print("[bold red]Invalid input. Please enter 1, 2, or 3.[/bold red]")


def get_computer_choice():
	"""
	Code that will randomly return 'rock', 'paper', or 'scissors' for the computer's choice.
	
    """
	input_prompt = "Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors):"
	"""Randomly return 'rock', 'paper', or 'scissors'."""
	return random.choice(choices)

# TODO: Implement this function to determine the winner of a round.
def determine_winner(user_choice, computer_choice):
	"""Return 'user', 'computer', or 'tie' based on the choices."""
	pass

# TODO: Implement this function to print the round result with color.
def print_round_result(user_choice, computer_choice, winner):
	"""Print the choices and the winner of the round using rich colors."""
	pass

# TODO: Implement the main game loop.
def main():
	"""Main function to run the game for 3 rounds and print the final result."""
	user_score = 0
	computer_score = 0
	rounds = 3
	for round_num in range(1, rounds + 1):
		# TODO: Get user and computer choices
		# TODO: Determine winner
		# TODO: Print round result
		# TODO: Update scores
		pass
	# TODO: Print final scores and announce the overall winner
	pass

if __name__ == "__main__":
	main()
	if user_score > computer_score:

		console.print("[bold green]Congratulations, you win the game![/bold green]")
