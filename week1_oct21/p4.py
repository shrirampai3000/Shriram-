import random 
game_number = random.randint(0, 9)
player_choice = int(input('Enter a number of your choice between 0 to 9: '))
if player_choice == game_number:
    print("Congratulations! You guessed it right.")
else:
    print(f"Sorry, the correct number was {game_number}.")

                  
