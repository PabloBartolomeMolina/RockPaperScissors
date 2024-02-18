from random import randint

# List of play options
options = ["Paper", "Rock", "Scissors"]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    outer_flag = True
    while outer_flag:
        game = input("Do you want to play (y/n) ?")
        if game == "y" or game == "Y":
            inner_flag = True
            while inner_flag:
                player = input("Please, select your option to play. You can also quit by writing 'quit'.")
                if player == "quit":
                    inner_flag = False  # Exit the inner loop
                else:
                    continue
            else:
                outer_flag = False  # Exit the outer loop
                print("See you soon !!")
        elif game == "n" or game == "N":
            print("See you soon !!")
            break
        else:
            print("Invalid answer, please limit it to characters 'y' OR 'n'...")
