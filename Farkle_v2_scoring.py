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
     
class Scorer:
    @staticmethod
    def calculate_score(dice):
        counts = Counter(dice)
        values = list(counts.values())

        if sorted(dice) == [1, 2, 3, 4, 5, 6]:
            return 3000
        if 6 in values:
            return 3000
        if sorted(values) == [3, 3]:
            return 2500
        if sorted(values) == [2, 2, 2]:
            return 1500
        if sorted(values) == [2, 4]:
            return 1500

        score = 0

        for num, count in list(counts.items()):
            if count == 5:
                score += 2000
                counts[num] -= 5

        for num, count in list(counts.items()):
            if count >= 4:
                score += 1000
                counts[num] -= 4

        for num, count in counts.items():
            if count >= 3:
                score += 1000 if num == 1 else num * 100
                counts[num] -= 3

        score += counts[1] * 100
        score += counts[5] * 50

        return score

    @staticmethod
    def score_breakdown(dice):
        breakdown = []
        counts = Counter(dice)

        # Special cases
        if sorted(dice) == [1, 2, 3, 4, 5, 6]:
            breakdown.append("Straight 1–6 = 3000")
            return breakdown
        if sorted(counts.values()) == [3, 3]:
            breakdown.append("Two Triplets = 2500")
            return breakdown
        if sorted(counts.values()) == [2, 2, 2]:
            breakdown.append("Three Pairs = 1500")
            return breakdown
        if sorted(counts.values()) == [2, 4]:
            breakdown.append("Four of a kind + Pair = 1500")
            return breakdown
        if 6 in counts.values():
            breakdown.append("Six of a kind = 3000")
            return breakdown

        for num, count in counts.items():
            if count == 5:
                breakdown.append(f"Five of a kind ({num}s) = 2000")
            elif count == 4:
                breakdown.append(f"Four of a kind ({num}s) = 1000")
            elif count == 3:
                if num == 1:
                    breakdown.append("Three 1s = 1000")
                else:
                    breakdown.append(f"Three {num}s = {num * 100}")

        leftover = Counter(dice)
        for num, count in counts.items():
            if count >= 3:
                leftover[num] -= 3
            if count == 4:
                leftover[num] -= 1
            if count == 5:
                leftover[num] -= 2
            if count == 6:
                leftover[num] = 0

        if leftover[1] > 0:
            breakdown.append(f"{leftover[1]} single 1s = {leftover[1] * 100}")
        if leftover[5] > 0:
            breakdown.append(f"{leftover[5]} single 5s = {leftover[5] * 50}")

        return breakdown



class Analyzer:
    @staticmethod
    def get_scoring_dice(dice):
        counts = Counter(dice)
        values = list(counts.values())
        scoring_dice = []
        used = Counter()

        # Special combinations (no overlap allowed)
        if sorted(dice) == [1, 2, 3, 4, 5, 6]:
            return dice
        if sorted(values) == [3, 3]:
            for num, count in counts.items():
                if count == 3:
                    scoring_dice += [num] * 3
            return scoring_dice
        if sorted(values) == [2, 2, 2]:
            for num, count in counts.items():
                if count == 2:
                    scoring_dice += [num] * 2
            return scoring_dice
        if sorted(values) == [2, 4]:
            for num, count in counts.items():
                scoring_dice += [num] * count
            return scoring_dice
        if 6 in values:
            for num, count in counts.items():
                if count == 6:
                    return [num] * 6

        # General scoring (track what’s used so we don’t double count)
        temp_counts = counts.copy()

        for num in range(1, 7):
            count = temp_counts[num]

            if count >= 5:
                scoring_dice += [num] * 5
                temp_counts[num] -= 5
            elif count == 4:
                scoring_dice += [num] * 4
                temp_counts[num] -= 4
            elif count == 3:
                scoring_dice += [num] * 3
                temp_counts[num] -= 3

        # After sets are removed, check for single 1s and 5s
        scoring_dice += [1] * temp_counts[1]
        scoring_dice += [5] * temp_counts[5]

        return scoring_dice



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
            round_score = player_turn(player)
            player.score += round_score
            player.round_scores.append(round_score)
            print(f"\n{player.name}'s total score: {player.score}")


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

def player_turn(player):
    print(f"\n{player.name}'s turn begins!")
    num_dice = 6
    turn_points = 0

    while True:
        roll = [random.randint(1, 6) for _ in range(num_dice)]

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{player.name} rolled: {roll}\n")
        for line in zip(*(dice_drawing[d] for d in roll)):
            print("   ".join(line))

        scoring_dice = Analyzer.get_scoring_dice(roll)

        if not scoring_dice:
            print("Farkle! No scoring dice. Turn ends.")
            input("Press Enter to continue...")
            return 0

        roll_score = Scorer.calculate_score(scoring_dice)
        breakdown = Scorer.score_breakdown(scoring_dice)
        print("Breakdown:")
        for line in breakdown:
            print(f"  - {line}")

        turn_points += roll_score

        print(f"Scoring Dice: {scoring_dice}")
        print(f"Points this roll: {roll_score}")
        print(f"Turn total so far: {turn_points}")

        num_dice -= len(scoring_dice)
        if num_dice == 0:
            print("🔥 Hot dice! You get all 6 back.")
            num_dice = 6

        choice = input("Roll again or bank points? (r/b): ").strip().lower()
        if choice != 'r':
            print(f"{player.name} banks {turn_points} points.")
            return turn_points

roll_dice()