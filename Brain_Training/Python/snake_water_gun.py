import random as r

# C:        S W G
# P:    S   D W L
# P:    W   L D W
# P:    G   W L D



win_matrix= [
    ["Draw","Win","Loss"],
    ["Loss","Draw","Win"],
    ["Win","Loss","Draw"],
]
# print(win_matrix[1][2])

def get_symbol(num):
    if num==0:
        symbol="Snake"
    elif num==1:
        symbol="Water"
    else:
        symbol="Gun"
    return symbol


while 1==1:
    computer_choice = r.choice(range(0, 3))
    human_choice = int(input("\nPlease insert a number of your choice\n 0 for Snake\n 1 for Water\n 2 for Gun\n Press any other number for exit-->"))
    if human_choice  in range(0,3):
        # print(f"Computer choice: {computer_choice}, Human choice: {human_choice} ")
        print(f"Computer choice: {get_symbol(computer_choice)}, Human choice: {get_symbol(human_choice)} ")
        print(f"Result :{win_matrix[human_choice][computer_choice]}")
    else:
        print("Invalid choice, try again..")
        break