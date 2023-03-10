import random 

print("\n\n...rock...")
print("...paper...")
print("...scissors...")

valid_choice = ('rock','paper','scissors')
beats_vc = ('scissors','rock','paper')
run = True
quitter = "\nPlayer quit the game.\n"

try:
    while run:   
        pc_wins = 0
        player_wins = 0
        draws = 0

        games_to_play = input("\nLET'S PLAY!\nBest Of? (bye to exit): ").lower()
        if games_to_play == 'bye':
            print(quitter)
            break

        else:
            games_to_play = int(games_to_play)
            
            for x in range(0,(games_to_play)):
                pc_int = random.randint(0,2)
                pc_pick = valid_choice[pc_int]

                player_pick = input("\nEnter Your Pick (bye to exit): \n").lower()
                if player_pick == 'bye':
                    print(quitter)
                    break
                else:
                    if pc_pick == player_pick:
                        message = f"\nComputer picked {pc_pick}.\nIt's a draw!\n"
                        draws += 1
                    if valid_choice.index(player_pick) == beats_vc.index(pc_pick):
                        message = f"\nComputer picked {pc_pick}.\nYou won!\n"
                        player_wins += 1
                    if valid_choice.index(pc_pick) == beats_vc.index(player_pick):
                        message = f"\nComputer picked  {pc_pick}.\nYou lost!\n"
                        pc_wins += 1
                    print(message)

        if  pc_wins > player_wins:
             message = f"\nComputer won {pc_wins} out of {games_to_play} games\nTotal draws = {draws}\nBetter luck next time."
        if  pc_wins < player_wins:
             message = f"\nPlayer won {player_wins} out of {games_to_play} games\nTotal draws = {draws}\nYou crunshed it!"
        if  pc_wins == player_wins:
             message = f"\nComputer won {pc_wins} and Player won {player_wins} out of {games_to_play} games\nTotal draws = {draws}\nYou've met your match it seems."
        print(message)

        keep_playing = input("\nKeep playing (Y/N)?: ").lower()
        if keep_playing == 'y':
            run = True
        if keep_playing == 'n':
            run = False
            print("\nBye :)\n")

except:
    print("\nSomething went wrong. Reload game.\n")
