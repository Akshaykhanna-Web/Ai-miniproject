def display_rules():
    print("\n===== NIM GAME RULES =====")
    print("1. There are multiple piles of stones.")
    print("2. Each player can choose any one pile in their turn.")
    print("3. From that pile, they can remove one or more stones.")
    print("4. The player forced to take the last stone loses the game.\n")
    print("===========================\n")

def display_piles(piles):
    print("Current piles status:")
    for i, pile in enumerate(piles, 1):
        print(f"Pile {i}: {'●' * pile} ({pile} stones)")
    print()

def nim_game():
    print("Welcome to the Nim Game!")
    display_rules()

    piles = [3, 4, 5]
    player = 1

    while any(piles):
        display_piles(piles)
        print(f"--> Player {player}'s turn <--")

        try:
            pile = int(input("Choose a pile number (1-3): ")) - 1
            remove = int(input("Enter how many stones to remove: "))
        except ValueError:
            print("⚠ Invalid input! Please enter numbers only.\n")
            continue

        if pile < 0 or pile >= len(piles):
            print("⚠ Invalid pile number! Choose again.\n")
            continue
        if remove <= 0 or remove > piles[pile]:
            print("⚠ Invalid number of stones to remove! Try again.\n")
            continue

        piles[pile] -= remove
        print(f"Player {player} removed {remove} stone(s) from Pile {pile + 1}.\n")

        if not any(piles):
            print(f"🎉 Player {player} wins the game! 🎉")
            break

        player = 2 if player == 1 else 1  # switch turns

    print("\nGame Over. Thanks for playing!")

# Run the game
nim_game()
