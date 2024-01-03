import random

print("\nThis is a game where you play against the computer. "
      "\nEach turn, you have two choices: 'red' or 'yellow'. "
      "\nThe computer randomly chooses 'red' or 'yellow' each turn as well. "
      "\n\nIf you both choose 'red', you gain 2 points. "
      "\nIf you both choose 'yellow', you gain 1 point. "
      "\nIf you choose 'red' and the computer chooses 'yellow', you lose 2 points. "
      "\nIf you choose 'yellow' and the computer chooses 'red', you lose 1 point. "
      "\n\nThe aim of the game is to get to 5 points in as few turns as possible. "
      "\n\nType 'r' to choose 'red' and 'y' to choose 'yellow'. Good luck!")
print()

PLAYER_POINTS = 0
TURNS = 0
CPU_COLOUR_options = ["r", "y"]
CPU_COLOUR = ""
OUTCOME = ""

while PLAYER_POINTS < 5:

    TURNS += 1
    PLAYER_COLOUR = ""

    while PLAYER_COLOUR not in ("r", "y"):
        PLAYER_COLOUR = input("Choose a colour: ")
        PLAYER_COLOUR = PLAYER_COLOUR.lower()
        print()

    CPU_COLOUR = random.choice(CPU_COLOUR_options)

    if PLAYER_COLOUR == "r":

        if CPU_COLOUR == "r":
            PLAYER_POINTS += 2
            OUTCOME = f"You gain 2 points! Total points = {PLAYER_POINTS}"

        else:
            PLAYER_POINTS -= 2
            OUTCOME = f"You lose 2 points. Total points = {PLAYER_POINTS}"

    else:

        if CPU_COLOUR == "r":
            PLAYER_POINTS -= 1
            OUTCOME = f"You lose 1 point. Total points = {PLAYER_POINTS}"

        else:
            PLAYER_POINTS += 1
            OUTCOME = f"You gain 1 point! Total points = {PLAYER_POINTS}"

    print(f"You chose: {PLAYER_COLOUR}")
    print(f"Computer chose: {CPU_COLOUR}")
    print()
    print(OUTCOME)
    print()

print(f"Well done! You reached 5 points in {TURNS} turns.")
print()
