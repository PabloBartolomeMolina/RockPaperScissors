from random import randint

# List of play options
options = ["Paper", "Rock", "Scissors"]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        game = input("Do you want to play (y/n) ?")
        if game == "y" or game == "Y":
            continue
        elif game == "n" or game == "N":
            print("See you soon !!")
            break
        else:
            print("Invalid answer, please limit it to characters 'y' OR 'n'...")
