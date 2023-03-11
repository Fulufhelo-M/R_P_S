import random 

print("...rock...")
print("...paper...")
print("...scissors...")

valid_choice = ('rock','paper','scissors')
beats_vc = ('scissors','rock','paper')
run = True

pc_int = random.randint(0,2)
pc_pick = valid_choice[pc_int]

try:
    while run:
        player_pick = input("\nEnter Your Pick (Bye to exit): \n").lower()
    
        if pc_pick == player_pick:
            message = f"\nComputer picked {pc_pick}.\n\nIt's a draw!\n"
        elif valid_choice.index(player_pick) == beats_vc.index(pc_pick):
            message = f"\nComputer picked {pc_pick}.\n\nYou won!\n"
        elif valid_choice.index(player_pick) != beats_vc.index(pc_pick):
            message = f"\nComputer picked  {pc_pick}.\n\nYou lost!\n"
        print(message)
except:
    run = False
    message = "Bye :)\n"
    print(message)