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
        self.round_scores = []

    def roll_dice(self, num_dice=6):
        self.dice = [random.randint(1, 6) for _ in range(num_dice)]
     
    @staticmethod   
    def calculate_score(dice):
        counts = Counter(dice)
        values = list(counts.values())
        
        
    # Rule: 1 - 6 straight    
        if sorted(dice) == [1, 2, 3, 4, 5, 6]:
            return 3000
        
    # Rule: 6 of a kind
        if 6 in values:
            return 3000
    
    # Rule: Two triplets (e.g. 2,2,2, 5,5,5)
        if sorted(values) == [3, 3]:
            return 2500

    # Rule: Three pairs (e.g. 1,1,3,3,6,6)
        if sorted(values) == [2, 2, 2]:
            return 1500
        
    # Rule: 4 of any number and a pair
        if sorted(values) == [2 , 4]:
            return 1500
        
        score = 0
    
    # Rule: Five of a kind
        for num, count in list(counts.items()):
            if count == 5:
                score += 2000
                counts[num] -= 5  # Important to avoid double-scoring
     
    # Rule: Four of a kind
        for num, count in list(counts.items()):
            if count >= 4:
                score += 1000
                counts[num] -= 4
            
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
            print(f"\n{player.name} rolled: {player.dice}\n")
            for line in zip(*(dice_drawing[d] for d in player.dice)):
                print("   ".join(line))

            round_score = Player.calculate_score(player.dice)
            player.score += round_score
            player.round_scores.append(round_score)
            print(f"\n{player.name}'s score this round: {round_score}")
            print(f"{player.name}'s total score: {player.score}")

            input("\nPress Enter to continue to the next player...")

            
        roll = input("\nRoll again? (Yes / No): ")

    # Final scoreboard
    print("\nFinal Scores by Round:")
    max_rounds = max(len(p.round_scores) for p in players)
    header = "Round\t" + "\t".join(player.name for player in players)
    print(header)
    print("-" * len(header.expandtabs()))
        
    # Print each round side by side
    for round_num in range(max_rounds):
        row = f"{round_num + 1}\t"
        for player in players:
             # Get score for this round or blank if no score
            if round_num < len(player.round_scores):
                row += f"{player.round_scores[round_num]}\t"
            else:
                row += " \t"
        print(row)
    
    
    print("-" * len(header.expandtabs()))
    totals = "Total\t" + "\t".join(str(p.score) for p in players)
    print(totals)
    # for player in players:
    #     print(f"\n{player.name}: Total = {player.score} points")
    #     for i, score in enumerate(player.round_scores, 1):
    #         print(f"  Round {i}: {score}")

    print("\nThanks for playing!")
    
roll_dice()