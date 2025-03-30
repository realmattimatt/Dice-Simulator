import random
import time
import os

def roll_dice():
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

    roll = input("Roll the dice? (Yes or No): ")
    while roll.strip().lower() in ("yes", "y"):
        # Dice roll animation
        for _ in range(5):
            temp1 = random.randint(1, 6)
            temp2 = random.randint(1, 6)
            temp3 = random.randint(1, 6)
            temp4 = random.randint(1, 6)
            os.system('cls' if os.name == 'nt' else 'clear')  # clear screen
            print("Rolling...")
            for l1, l2, l3, l4 in zip(dice_drawing[temp1], dice_drawing[temp2], dice_drawing[temp3], dice_drawing[temp4]):
                print(f"{l1}   {l2}   {l3}   {l4}")
            time.sleep(0.2)

        # Final result
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice3 = random.randint(1, 6)
        dice4 = random.randint(1, 6)

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"You rolled: {dice1}, {dice2}, {dice3}, {dice4}\n")
        for l1, l2, l3, l4 in zip(dice_drawing[dice1], dice_drawing[dice2], dice_drawing[dice3], dice_drawing[dice4]):
            print(f"{l1}   {l2}   {l3}   {l4}")

        roll = input("\nRoll again? (Yes / No): ")

    print("\nThanks for playing!")

roll_dice()
