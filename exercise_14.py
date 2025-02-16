# create a rock paper scissors game with the user playing against the computer

# import the random module to generate random choices for the computer
import random

# show an introductory message for the game
print("Welcome to the Rock, Paper, Scissors challenge -- can you beat the Computer?\n")

# set user and computer's score to zero before starting the game
user_score = 0
computer_score = 0

# create a function to get the user's choice
def user_choice():
    """
    This function prompts the user to enter a choice (R, P, or S).
    It also ensures the input is valid
    :return: str
    """

    # use a dictionary to list all possible choices, matching Rock, Paper, Scissors to R, P or S
    possible_choices = {
        "R": "Rock",
        "P": "Paper",
        "S": "Scissors"
    }

    # prompts the user for input -- use .upper to convert input to uppercase for consistency
    user_input = input("Enter R for Rock, P for Paper, or S for Scissors: ").upper()

    # the while loop ensures the user enters a valid choice (preventing a key error)
    while user_input not in possible_choices:
        print("Invalid choice; please enter R, P, or S.")
        user_input = input("Enter R for Rock, P for Paper, or S for Scissors: ").upper()

    # this returns the full name of the user's choice
    return possible_choices[user_input]


# create a function to generate the computer's choice
def computer_choice():
    """
    This function randomly selects a choice for the computer (Rock, Paper, or Scissors)
    :return: str
    """

    # use a dictionary to list all possible choices, matching Rock, Paper, Scissors to 0, 1 or 2 (could also have used a list)
    possible_choices = {
        0: "Rock",
        1: "Paper",
        2: "Scissors"
    }

    # generate a random number between 0 and 2 to select a choice of Rock, Paper, or Scissors
    computer_number = random.randint(0, 2)

    # returns the full name of the computer's choice
    return possible_choices[computer_number]

# create a function to play a single round of the game
def play_round():
    """
    This function plays a single round of Rock, Paper, Scissors between a user and the computer
    It gets both the user and the computer's choice, compares the choices to determine a winner, updating the scores accordingly and printing the result for each round
    :return: str
    """

    # instruction to use the global variable inside this function
    # the keyword "global" tells this function to take the global variable (from outside the scope: user_score = 0 and player_score = 0)
    # user and computer scores can now be updated based on the below instructions
    global user_score, computer_score

    # call the user_choice and computer_choice functions within the play_round function -- so that this happens for each round
    # had this outside of play_round before and it wasn't being considered when I ran the for loop to run 3 rounds of the game :(
    user = user_choice()
    computer = computer_choice()

    # show the choices made by both the user and the computer
    print(f"You chose: {user}")
    print(f"The computer chose: {computer}")

    # use conditional logic to determine the winner of each round
    # draw if the user and computer pick the same thing
    if user == computer:
        print("This round is a draw\n")

    # these are the conditions which mean the user wins
    elif (
            (user == "Rock" and computer == "Scissors") or
            (user == "Paper" and computer == "Rock") or
            (user == "Scissors" and computer == "Paper")
    ):
        print("You win this round!\n")

        # if the user wins, their score increases by 1 (from zero)
        user_score += 1

    # if none of the above conditions are met, then the computer wins
    else:
        print("You lose this round!\n")

        # if the user loses, the computer's score increases by 1 (from zero)
        computer_score += 1


# use a for loop to play 3 rounds of the game
for item in range(3):
    play_round()


# Show the final score after 3 rounds of the game have been played
print(f"The final score is:\nYou: {user_score}, Computer: {computer_score}")

# use conditional statements to decide the overall winner of the game (best 2 out of 3 rounds)
if user_score > computer_score:
    print("Congratulations, you win the game! 🤩")
elif user_score == computer_score:
    print("It's a tie! Try again to beat the Computer 💪🏼")
else:
    print("Computer won the game. Better luck next time! 😔")
