# This is a simple text-based 'Escape the Room' game where the player must interact with objects to find a key and escape.

def describe_room():
    # Displays the initial room description with interactive elements.
    print("You are in a dimly lit room. You see a dusty bookshelf, a locked drawer, and a window.")

def get_user_input():
    # Prompts the player to enter an action and returns the input in lowercase for easy comparison.
    return input("What do you want to do? (open drawer/examine bookshelf/look out window/): ").strip().lower()

def check_action(action, inventory):
    # Handles user actions based on input and modifies the game state accordingly.
    if action == "examine bookshelf":
        print("The bookshelf is filled with old collections, a number of soft and hard-bound books. One book seems odd.")
        choice = input("Would you investigate the book? (yes/no): ").strip().lower()
        if choice == "yes":
            print("You successfully got the key!!")
            inventory.add("key")
    elif action == "open drawer":
        if "key" in inventory:
            print("Congratulations! You managed to escape the room!")
            return True  # Ends the game when the player successfully escapes.
        else:
            print("The drawer is locked.")
    elif action == "look out window":
        print("You see a gloomy hallway.")
    else:
        print("Beware! Make sure to check your spelling.")
    return False  # The game continues until the player escapes.

def play_game():
    # Main game loop where the player interacts until they escape.
    inventory = set()
    describe_room()
    while True:
        action = get_user_input()
        if check_action(action, inventory):
            break  # Exits the loop once the player wins.

# Starts the game.
play_game()