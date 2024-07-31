'''
1 for snake
2 for water
3 for gun
'''
import random

print("Welcome to Snake, Water, and Gun game!!")

while True:  
    game = input("Enter S to start or Q to quit: ").lower()
    
    if game == "q":
        print("Thanks for playing! Goodbye!")
        break
    elif game != "s":
        print("Invalid choice. Please enter 'S' to start or 'Q' to quit.")
        continue

    while game == "s":
        computer = random.choice([1, 2, 3])

        player_input_str = input("Enter your choice (S for Snake, W for Water, G for Gun): ").lower()
        player_dict = {"s": 1, "w": 2, "g": 3}
        reverse_dict = {1: "Snake", 2: "Water", 3: "Gun"}

        # To check if the player's input is valid
        if player_input_str not in player_dict:
            print("Invalid input. Please enter S, W, or G.")
            continue

        player = player_dict[player_input_str]

        print(f"You chose {reverse_dict[player]}\nComputer chose {reverse_dict[computer]}")

        if computer == player:
            print("It's a draw!")
        else:
            if(computer ==1 and player == 2):
                print("Computer wins!")
            elif(computer == 1 and player == 3):
                print("Player wins!")
            elif(computer == 2 and player == 1):
                print("Player wins!")
            elif(computer == 2 and player == 3):
                print("Computer wins!")
            elif(computer == 3 and player == 1):
                print("Computer wins!")
            elif(computer == 3 and player == 2):
                print("Player wins!")
            else:
                print("Something went wrong...")
                
        # If player wants to play again
        game = input("Enter S to play again or Q to quit: ").lower()
        if game not in ["s", "q"]:
            print("Invalid input. Please enter S or Q.")
            continue
        
        if game == "q":
            break
    
    if game == "q":
            print("Thanks for playing! Goodbye!")
            break
