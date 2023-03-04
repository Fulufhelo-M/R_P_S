import random 

print("...rock...")
print("...paper...")
print("...scissors...")

valid_choice = ('rock','paper','scissors')
beats_vc = ('scissors','rock','paper')
pc_int = random.randint(0,2)
pc_pick = valid_choice[pc_int]

try:
    player_pick = input("\nEnter Your Pick (Bye to exit): \n").lower()

    if player_pick == 'bye':
        message = "Goodbye :)"
    elif pc_pick == player_pick:
        message = f"\nComputer picked {pc_pick}.\n\nIt's a draw!\n"
    elif valid_choice.index(player_pick) == beats_vc.index(pc_pick):
        message = f"\nComputer picked {pc_pick}.\n\nYou won!\n"
    else:
        message = f"\nComputer picked  {pc_pick}.\n\nYou lost!\n"
except: 
    message = "Oops. Try again."

print(message)