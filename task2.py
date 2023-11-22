import time

def introduction():
    print("Welcome to the Text Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious room.")

def choose_path():
    print("Choose your path:")
    print("1. Open the door on the left.")
    print("2. Examine the painting on the wall.")
    return input("Enter 1 or 2: ")

def left_door():
    print("You open the door on the left and find a treasure chest.")
    time.sleep(1)
    print("Congratulations! You've found a treasure!")

def examine_painting():
    print("You examine the painting and notice a hidden switch.")
    time.sleep(1)
    print("Do you want to:")
    print("1. Press the switch.")
    print("2. Ignore the switch.")
    return input("Enter 1 or 2: ")

def secret_room():
    print("You press the switch and a secret door opens.")
    time.sleep(1)
    print("You discover a hidden room filled with rare artifacts.")

def main():
    introduction()
    choice1 = choose_path()

    if choice1 == "1":
        left_door()
    elif choice1 == "2":
        choice2 = examine_painting()
        if choice2 == "1":
            secret_room()
        elif choice2 == "2":
            print("You continue exploring the room.")

if __name__ == "__main__":
    main()
