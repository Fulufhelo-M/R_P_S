import random 

print("...rock...")
print("...paper...")
print("...scissors...")

pc_int = random.randint(0,2)
valid_choice = ('rock','paper','scissors')
beats_vc = ('scissors','rock','paper')
pc_pick = valid_choice[pc_int]

try:
    player_pick = input("\nEnter Your Pick (Bye to exit): \n").lower()
    if player_pick == 'bye':
        print("Goodbye :)")
    elif pc_pick == player_pick:
        print(f"\nComputer picked " + pc_pick + ".\n\nIt's a draw!\n")
    elif valid_choice.index(player_pick) == beats_vc.index(pc_pick):
        print(f"\nComputer picked " + pc_pick + ".\n\nYou won!\n")
    elif valid_choice.index(player_pick) != beats_vc.index(pc_pick):
        print(f"\nComputer picked " + pc_pick + ".\n\nYou lost!\n")
except: 
    print("Oops. Try again.")