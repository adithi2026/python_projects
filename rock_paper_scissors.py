import random

choices = ["r", "p", "s"]
emojis = {"r": "✊", "p": "✋", "s": "✌️"}

while True:
    user_choice = input("Rock, Paper, Scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print("ivalid choice!")
        continue
    computer_choice = random.choice(choices)
    print(f'you chose {emojis[user_choice]}')
    print(f'computer chose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print("tie!")
    elif (
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "p" and computer_choice == "r") or
        (user_choice == "s" and computer_choice == "p")
    ):
        print("you win!")
    else:
        print("you lose!")
    play_again = input("play again? (y/n): ").lower()
    if play_again == 'n':
        break



