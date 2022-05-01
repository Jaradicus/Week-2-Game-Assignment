#Week 2 Tic-Tac-Toe
#Jared Hogan


grid_bones = {
    0 : "error",
    1 : 1,
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5,
    6 : 6,
    7 : 7,
    8 : 8,
    9 : 9
}

game_active = 1
active_player = "X"
selected_tile = 0

def take_tile(tile):
    global active_player
    grid_bones[tile] = active_player

def take_turns():
    global active_player, selected_tile    
    game_active = 1
    while game_active == 1:
        get_grid()
        
        selected_tile = int(input(f"{active_player}'s turn. Which tile would you like to take?\n"))
        if grid_bones[selected_tile] == selected_tile:
            take_tile(selected_tile)
            game_active = end_check()
            if active_player == "X":
                active_player = "O"
            else:
                active_player ="X"
        else :
            print("That tile's taken!")

def get_grid():
    print(f"{grid_bones[1]}|{grid_bones[2]}|{grid_bones[3]}\n-----\n{grid_bones[4]}|{grid_bones[5]}|{grid_bones[6]}\n-----\n{grid_bones[7]}|{grid_bones[8]}|{grid_bones[9]}\n")

def end_check():
    if grid_bones[1] == grid_bones[2] == grid_bones[3] or grid_bones[1] == grid_bones [4] == grid_bones[7] or grid_bones[1] == grid_bones[5] == grid_bones[9] or grid_bones[2] == grid_bones[5] == grid_bones[8] or grid_bones[3] == grid_bones[6] == grid_bones[9] or grid_bones[3] == grid_bones[5] == grid_bones[7] or grid_bones[4] == grid_bones[5] == grid_bones[6] or grid_bones[7] == grid_bones[8] == grid_bones[9]:
        print(f"{active_player} wins!")
        get_grid()
        return 0
    elif grid_bones[1] != 1 and grid_bones[2] != 2 and grid_bones[3] != 3 and grid_bones[4] != 4 and grid_bones[5] != 5 and grid_bones[6] != 6 and grid_bones[7] != 7 and grid_bones[8] != 8 and grid_bones[9] != 9:
        print("Draw!")
        get_grid()
        return 0
    else:
        return 1
    


def main():
    global game_active, active_player
    ready = input("Are you ready to start? \nY/N\n")
    if ready == "Y":
        take_turns()
    elif ready == "N":
        game_active = 0
    else:
        print("game start error")
main()
