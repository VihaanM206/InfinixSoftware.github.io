# Text Adventure Game: The Lost Kingdom of Eldoria (With NPCs and Bug Fixes)

def start_game():
    print("Welcome to The Lost Kingdom of Eldoria!")
    print("You are a brave adventurer seeking the lost kingdom, said to hold untold treasures and ancient secrets.")
    print("Your choices will determine your fate. Choose wisely!\n")
    forest_of_whispers()

def forest_of_whispers():
    print("\nYou stand at the edge of the Forest of Whispers, a dark and eerie place.")
    print("Three paths lie before you:")
    print("1. Take the left path.")
    print("2. Take the middle path.")
    print("3. Take the right path.")

    choice = input("What do you do? (1/2/3): ")

    if choice == "1":
        left_path()
    elif choice == "2":
        middle_path()
    elif choice == "3":
        right_path()
    else:
        print("Invalid choice. Try again.")
        forest_of_whispers()

def left_path():
    print("\nYou take the left path and encounter a mysterious old woman.")
    print("She offers you a potion, claiming it will protect you from harm.")
    choice = input("Do you accept the potion? (yes/no): ").lower()

    if choice == "yes":
        print("\nYou drink the potion and feel a surge of energy.")
        print("The old woman smiles and vanishes into the shadows.")
        river_of_decisions(has_potion=True)
    elif choice == "no":
        print("\nYou decline the potion and continue on your journey.")
        river_of_decisions(has_potion=False)
    else:
        print("Invalid choice. Try again.")
        left_path()

def middle_path():
    print("\nYou take the middle path and find a hidden cave.")
    print("Inside, there’s a chest and a strange symbol on the wall.")
    choice = input("Do you open the chest or inspect the symbol? (chest/symbol): ").lower()

    if choice == "chest":
        print("\nYou open the chest and find a pile of gold coins!")
        print("But as you take the gold, the symbol on the wall glows brightly.")
        print("You feel a strange sensation...")
        ending_curse_of_greed()
    elif choice == "symbol":
        print("\nYou inspect the symbol and realize it’s a warning.")
        print("You leave the chest untouched and exit the cave safely.")
        mountains_of_despair()
    else:
        print("Invalid choice. Try again.")
        middle_path()

def right_path():
    print("\nYou take the right path and hear growling in the distance.")
    print("A pack of wolves approaches!")
    choice = input("Do you fight the wolves or try to sneak past them? (fight/sneak): ").lower()

    if choice == "fight":
        print("\nYou bravely fight the wolves but are overwhelmed by their numbers.")
        print("You barely escape with your life, injured and exhausted.")
        swamp_of_illusions()
    elif choice == "sneak":
        print("\nYou quietly sneak past the wolves, avoiding detection.")
        print("You continue your journey unscathed.")
        mountains_of_despair()
    else:
        print("Invalid choice. Try again.")
        right_path()

def river_of_decisions(has_potion):
    print("\nYou reach the River of Decisions. A rickety bridge spans the river, and a boat is tied to the shore.")
    print("1. Cross the bridge.")
    print("2. Take the boat.")

    choice = input("What do you do? (1/2): ")

    if choice == "1":
        cross_bridge(has_potion)
    elif choice == "2":
        take_boat(has_potion)
    else:
        print("Invalid choice. Try again.")
        river_of_decisions(has_potion)

def cross_bridge(has_potion):
    print("\nYou attempt to cross the rickety bridge.")
    print("Halfway across, the bridge collapses!")

    if has_potion:
        print("\nYou use the potion’s energy to leap to safety.")
        temple_of_eldoria()
    else:
        print("\nYou fall into the river and are swept away by the current.")
        ending_lost_in_river()

def take_boat(has_potion):
    print("\nYou take the boat, but it starts leaking.")
    print("You see a hole and a bucket.")
    choice = input("Do you bail water or patch the hole? (bail/patch): ").lower()

    if choice == "bail":
        print("\nYou try to bail water, but the leak is too large.")
        print("The boat sinks, and you are lost in the river.")
        ending_lost_in_river()
    elif choice == "patch":
        print("\nYou use your cloak to patch the hole and safely reach the other side.")
        temple_of_eldoria()
    else:
        print("Invalid choice. Try again.")
        take_boat(has_potion)

def mountains_of_despair():
    print("\nYou arrive at the Mountains of Despair, a treacherous range with icy peaks.")
    print("You see two paths:")
    print("1. Climb the icy cliffs.")
    print("2. Go through the dark cave.")

    choice = input("What do you do? (1/2): ")

    if choice == "1":
        print("\nYou attempt to climb the icy cliffs.")
        print("The climb is perilous, and you slip multiple times.")
        print("At the top, you find a hidden shrine with a glowing artifact.")
        print("You take the artifact and feel its power.")
        temple_of_eldoria()
    elif choice == "2":
        print("\nYou enter the dark cave and are immediately surrounded by bats!")
        print("You must decide:")
        print("1. Fight the bats.")
        print("2. Use a torch to scare them away.")

        choice = input("What do you do? (1/2): ")

        if choice == "1":
            print("\nYou fight the bats but are overwhelmed and injured.")
            ending_lost_in_mountains()
        elif choice == "2":
            print("\nYou light a torch and scare the bats away.")
            print("You safely exit the cave and continue your journey.")
            temple_of_eldoria()
        else:
            print("Invalid choice. Try again.")
            mountains_of_despair()
    else:
        print("Invalid choice. Try again.")
        mountains_of_despair()

def swamp_of_illusions():
    print("\nYou enter the Swamp of Illusions, a misty and confusing place.")
    print("You see three paths:")
    print("1. Follow the glowing lights.")
    print("2. Take the muddy path.")
    print("3. Climb a tree to get a better view.")

    choice = input("What do you do? (1/2/3): ")

    if choice == "1":
        print("\nYou follow the glowing lights, but they lead you in circles.")
        print("You are lost in the swamp forever.")
        ending_lost_in_swamp()
    elif choice == "2":
        print("\nYou take the muddy path and encounter a friendly guide.")
        print("The guide leads you safely out of the swamp.")
        temple_of_eldoria()
    elif choice == "3":
        print("\nYou climb a tree and spot a hidden path.")
        print("You follow the path and find a shortcut to the temple.")
        temple_of_eldoria()
    else:
        print("Invalid choice. Try again.")
        swamp_of_illusions()

def temple_of_eldoria():
    print("\nYou finally reach the Temple of Eldoria!")
    print("Inside, you find three doors, each with a riddle.")
    print("You must solve the riddles to proceed.")

    # Riddle 1
    print("\nDoor 1: I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?")
    answer1 = input("Your answer: ").lower()

    if answer1 != "echo":
        print("\nIncorrect! The door remains locked.")
        ending_fools_end()
        return

    # Riddle 2
    print("\nDoor 2: The more you take, the more you leave behind. What am I?")
    answer2 = input("Your answer: ").lower()

    if answer2 != "footsteps":
        print("\nIncorrect! The door remains locked.")
        ending_fools_end()
        return

    # Riddle 3
    print("\nDoor 3: I am not alive, but I grow; I don’t have lungs, but I need air; I don’t have a mouth, but water kills me. What am I?")
    answer3 = input("Your answer: ").lower()

    if answer3 != "fire":
        print("\nIncorrect! The door remains locked.")
        ending_fools_end()
        return

    # All riddles solved
    print("\nAll doors open! You find the treasure of Eldoria!")
    ending_heros_triumph()

# Endings
def ending_heros_triumph():
    print("\nYou have found the treasure of Eldoria and become a legend!")
    print("Congratulations, you have achieved the best ending!")
    play_again()

def ending_curse_of_greed():
    print("\nYou are cursed for your greed and trapped in the temple forever.")
    print("This is the Curse of Greed ending.")
    play_again()

def ending_lost_in_river():
    print("\nYou are lost in the river and never seen again.")
    print("This is the Lost in River ending.")
    play_again()

def ending_fools_end():
    print("\nYou failed to solve the riddles and are lost in the temple forever.")
    print("This is the Fool’s End ending.")
    play_again()

def ending_lost_in_mountains():
    print("\nYou are lost in the Mountains of Despair and perish from the cold.")
    print("This is the Lost in Mountains ending.")
    play_again()

def ending_lost_in_swamp():
    print("\nYou are lost in the Swamp of Illusions and never escape.")
    print("This is the Lost in Swamp ending.")
    play_again()

def play_again():
    choice = input("\nDo you want to play again? (yes/no): ").lower()
    if choice == "yes":
        start_game()
    else:
        print("Thank you for playing The Lost Kingdom of Eldoria!")

# Start the game
start_game()
