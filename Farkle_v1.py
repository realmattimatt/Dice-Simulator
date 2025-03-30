import random
import time
import os
from collections import Counter


# Define Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.dice = []
        self.score = 0

    def roll_dice(self, num_dice=6):
        self.dice = [random.randint(1, 6) for _ in range(num_dice)]
     
    @staticmethod   
    def calculate_score(dice):
        counts = Counter(dice)
        values = list(counts.values())
        
        score = 0
        
    # Rule: 1 - 6 straight    
        if sorted(dice) == [1, 2, 3, 4, 5, 6]:
            score += 3000
        
    # Rule: 6 of a kind
        if 6 in values:
            score += 3000
    
    # Rule: Two triplets (e.g. 2,2,2, 5,5,5)
        if sorted(values) == [3, 3]:
            score += 2500
        
    # Rule: Five of a kind
        if 5 in values:
            score += 2000

    # Rule: Three pairs (e.g. 1,1,3,3,6,6)
        if sorted(values) == [2, 2, 2]:
            score += 1500
        
    # Rule: 4 of any number and a pair
        if sorted(values) == [2 , 4]:
            score += 1500
        
    # Rule: Four of a kind
        if 4 in values:
            score += 1000
            
    # Rule: Three of a kind
        for num, count in counts.items():
            if count >= 3:
                if num == 1:
                    score += 1000
                else:
                    score += num * 100
                counts[num] -= 3
    # Rule: Single or double one's and five's
        # Rule: Single 1s and 5s (outside of triplets)
        score += counts[1] * 100
        score += counts[5] * 50

        return score


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
            player.score = Player.calculate_score(player.dice)
            print(f"\n{player.name}'s score this round: {player.score}")
            input("\nPress Enter to continue to the next player...")


        roll = input("\nRoll again? (Yes / No): ")


    print("\nFinal Dice Results:")
    for player in players:
        print(f"{player.name}: {player.dice}")

    print("\nThanks for playing!")

roll_dice()