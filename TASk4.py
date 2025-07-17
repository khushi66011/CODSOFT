#----------------------------------
#Task4 :  Rock-Paper-Scissors Game
#----------------------------------
#Project Description:-
# 1. Prompt to user to choice: 0 for rock, 1 for paper, 2 for scissors
# 2. computer generates random choice
# 3. Game Logic: Rock > Scissors > Paper > Rock
# 4. Result: win, Lose or draw.
# 5. Score tracking
# 6. Reply option (yes/no)


import random
# return the name of choices
def get_choice_name(choice):
    return ["Rock", "Paper", "Scissors"][choice]
# determine the result of the game: win,lose or draw
def Winner(user, computer):
    if user == computer:
        return "draw" # if both choices are same, It's draw
    elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
        return "win"
    else:
        return "lose"
    
#Initialize scores to 0
user_score = 0
computer_score = 0

#start  the game
while True:
    print("\n=== Rock-Paper-Scissors Game ===")
    print("Type 0 for Rock, 1 for Paper, 2 for Scissors")

# take input from user
    try:
        user_choice = int(input("Your choice: "))
        if user_choice not in [0, 1, 2]:
            print("Invalid input. Please enter 0, 1, or 2.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

# Computer makes random choice from 0 to 2
    computer_choice = random.randint(0, 2)

# display chhoices
    print(f"You choose: {get_choice_name(user_choice)}")
    print(f"Computer choose: {get_choice_name(computer_choice)}")

# show winner
    result = Winner(user_choice, computer_choice)

# update score
    if result == "draw":
        print("It's a draw!")
    elif result == "win":
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

# show score
    print("your score:", user_score) 
    print("computer score:", computer_score) 

# Ask user to play again?
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if (play_again == "no" or play_again !="yes") :
        print("Thanks for playing!")
        break
