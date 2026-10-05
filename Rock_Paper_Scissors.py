"""
Welcome the user to the game. Ask them how many rounds they would like to play. Ensure that
the number they enter is an odd number so there cannot be any ties.
For the game play, ask the user for their choice and then generate a random choice for the
computer. (NOTE: Make sure that the user’s choice is valid.) If there is a tie, the game does not
count, and we push to the next one. Keep track of the number of wins and losses for both the
player and the computer. When the game play is over, determine the overall winner and print the
results.
Build and use at least two custom functions:
• get_player_choice: This function should prompt the player, convert the response to
lowercase, validate the choice, and return the result.
• determine_winner: This function should compare the two choices and return "win",
"loss", or "tie".
"""
import random


result = "Tie"
user_wins = 0
computer_wins = 0
winner = ""

def get_player_choice(result, user_wins, computer_wins) : 
    while(result == "Tie") :
        #Handles computer generated play
        random_choice = random.randint(1, 3)
        #Turns randomly generated number into rock, paper, or scissors
        if(random_choice == 1) :
            random_choice = "rock"
        elif(random_choice == 2) :
            random_choice = "paper"
        elif(random_choice == 3) :
            random_choice = "scissors"

        #Handles user play
        user_choice = input("\nEnter rock, paper, or scissors: ")
        while (user_choice.lower() not in ("rock", "paper", "scissors")):
            user_choice = input(user_choice + " is not a valid option. Please try again: ")
        

        #Checks if user wins game, if not, follows other path.
        if determine_winner(random_choice, user_choice) == "Win" :
            print("You chose " + user_choice.lower())
            print("The computer chose " + random_choice.lower())
            print("You win!")
            winner = "User"
            result = "Win"
            return winner
        elif determine_winner(random_choice, user_choice) == "Lose" :
            print("You chose " + user_choice.lower())
            print("The computer chose " + random_choice.lower())
            print("You lose!")
            winner = "Computer"
            result = "Lose"
            return winner
        else:
            print("You chose " + user_choice.lower())
            print("The computer chose " + random_choice.lower())
            print("It's a tie! Try again.")
            result = "Tie"

#Function to check to see if player or computer won or tie
def determine_winner(random_choice, user_choice) :
    if (user_choice.lower() == "rock") :
        if (random_choice == "paper") :
            return "Lose"
        elif(random_choice == "scissors") :
            return "Win"
        else : 
            return "Tie"
    elif (user_choice.lower() == "paper") :
        if(random_choice == "scissors") :
            return "Lose"
        elif (random_choice == "rock"):
            return "Win"
        else :
            return "Tie"
    elif (user_choice.lower() == "scissors") :
        if (random_choice == "rock") :
            return "Lose"
        elif (random_choice == "paper") :
            return "Win"
        else :
            return "Tie"
    

rounds = int(input("Welcome to Rock Paper Scissors! How many rounds would you like to play? "))
while(rounds % 2 == 0) :
    rounds = int(input("Sorry, we don't like ties here, so please enter an odd number. "))

for i in range(0, rounds) :
    print(f"\nGame {i + 1}")
    winner = get_player_choice(result, user_wins, computer_wins)
    if(winner == "User") :
        user_wins += 1
    elif(winner == "Computer") :
        computer_wins += 1
    winner = ""

print("\n---------------\n")
print(f"Score - You: {user_wins} | Computer: {computer_wins}")
if(user_wins > computer_wins) :
    print("You win!!")
elif(computer_wins > user_wins) :
    print("You lose!!")
print("Thanks for playing!")