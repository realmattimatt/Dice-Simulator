import random
import time
import os

# Define Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.dice = []
        self.score = 0

    def roll_dice(self, num_dice=6):
        self.dice = [random.randint(1, 6) for _ in range(num_dice)]

# Dice graphics
dice_drawing = {
        1: (
            "┌─────────┐",
            "│         │",
            "│    ○    │",
            "│         │",
            "└─────────┘",
        ),
        2: (
            "┌─────────┐",
            "│  ○      │",
            "│         │",
            "│      ○  │",
            "└─────────┘",
        ),
        3: (
            "┌─────────┐",
            "│  ○      │",
            "│    ○    │",
            "│      ○  │",
            "└─────────┘",
        ),
        4: (
            "┌─────────┐",
            "│  ○   ○  │",
            "│         │",
            "│  ○   ○  │",
            "└─────────┘",
        ),
        5: (
            "┌─────────┐",
            "│  ○   ○  │",
            "│    ○    │",
            "│  ○   ○  │",
            "└─────────┘",
        ),    
        6: (
            "┌─────────┐",
            "│  ○   ○  │",
            "│  ○   ○  │",
            "│  ○   ○  │",
            "└─────────┘",
        )
    }


# Game loop
def roll_dice():
    players = []
    num_players = int(input("How many players? "))
    for i in range(num_players):
        name = input(f"Enter name for Player {i+1}: ")
        players.append(Player(name))
    roll = input("Roll the dice? (Yes or No): ")
    while roll.strip().lower() in ("yes", "y"):
        for player in players:
            # Animate
            for _ in range(5):
                temps = [random.randint(1, 6) for _ in range(6)]
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{player.name} is rolling...")
                for line in zip(*(dice_drawing[t] for t in temps)):
                    print("   ".join(line))
                time.sleep(0.2)

            # Final roll
            player.roll_dice()
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{player.name} rolled: {player.dice}\n")
            for line in zip(*(dice_drawing[d] for d in player.dice)):
                print("   ".join(line))
            input("\nPress Enter to continue to the next player...")

        roll = input("\nRoll again? (Yes / No): ")


    print("\nFinal Dice Results:")
    for player in players:
        print(f"{player.name}: {player.dice}")

    print("\nThanks for playing!")

roll_dice()
