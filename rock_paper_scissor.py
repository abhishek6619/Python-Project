# import random

# ROCK = "r"
# SCISSORS = "s"
# PAPER = "p"
# emojis = {ROCK: "🪨", SCISSORS: "✂️", PAPER: "📃"}
# choices = tuple(emojis.keys())


# def get_user_choice():
#     while True:
#         user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
#         if user_choice in choices:
#             return user_choice
#         else:
#             print("Invalid choice!")


# def display_choices(user_choice, computer_choice):
#     print(f"You chose {emojis[user_choice]}")
#     print(f"Computer chose {emojis[computer_choice]}")


# def determine_winner(user_choice, computer_choice):
#     if user_choice == computer_choice:
#         print("Tie!")
#     elif (
#         (user_choice == ROCK and computer_choice == SCISSORS)
#         or (user_choice == SCISSORS and computer_choice == PAPER)
#         or (user_choice == PAPER and computer_choice == ROCK)
#     ):
#         print("You win")
#     else:
#         print("You lose")


# def play_game():
#     while True:
#         user_choice = get_user_choice()

#         computer_choice = random.choice(choices)

#         display_choices(user_choice, computer_choice)

#         determine_winner(user_choice, computer_choice)

#         should_continue = input("Continue? (y/n): ").lower()
#         if should_continue == "n":
#             break


# play_game()

import random


def get_user_choice():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    while user_choice not in choices:
        print("Invalid choice. Try again.")
        user_choice = input("Enter rock, paper, or scissors: ").lower()
    return user_choice


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)


if __name__ == "__main__":
    play_game()
