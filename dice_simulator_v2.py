import random
# Symbols to make dice
# Alt 196 ─
# Alt 217 ┘
# Alt 218 ┌
# Alt 191 ┐
# Alt 192 └
# Alt 179 │
# Alt 9   ○ 

def roll_dice():
    dice_drawing = {
        1: (
            "┌─────────┐",
            "│    1    │",
            "│    ○    │",
            "│         │",
            "└─────────┘",
        ),
        2: (
            "┌─────────┐",
            "│  ○      │",
            "│    2    │",
            "│      ○  │",
            "└─────────┘",
        ),
        3: (
            "┌─────────┐",
            "│  ○ 3    │",
            "│    ○    │",
            "│      ○  │",
            "└─────────┘",
        ),
        4: (
            "┌─────────┐",
            "│  ○   ○  │",
            "│    4    │",
            "│  ○   ○  │",
            "└─────────┘",
        ),
        5: (
            "┌─────────┐",
            "│  ○ 5 ○  │",
            "│    ○    │",
            "│  ○   ○  │",
            "└─────────┘",
        ),    
        6: (
            "┌─────────┐",
            "│  ○   ○  │",
            "│  ○ 6 ○  │",
            "│  ○   ○  │",
            "└─────────┘",
        )
    }
    roll = input("Roll the dice? (Yes or No): ")
    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dice3 = random.randint(1,6)
        print(f"dice rolled: {dice1} and {dice2} and {dice3}")
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))
        print("\n".join(dice_drawing[dice3]))
        roll = input("Roll again? (Yes / NO): ")

        
roll_dice()