grid = {
    0 : ["error"],
    1 : [0],
    2 : [0],
    3 : [0],
    4 : [0],
    5 : [0],
    7 : [0],
    8 : [0],
    9 : [0]
}

game_active = 1
active_player = "X"
selected_tile = 0

#def take_tile(tile):
    

def take_turns():
    while game_active == 1:
        selected_tile = int(input(f"{active_player}'s turn. Which tile would you like to take?\n"))
        if selected_tile == 0:
            take_tile(selected_tile)
            break
        else :
            print("That tile is already taken!")
            break

def main():
    global game_active, active_player, selected_tile
    while game_active == 1:
        ready = input("Are you ready to start? \nY/N\n")
        if ready == "Y":
            take_turns()
        elif ready == "N":
            game_active = 0
        else:
            print("game start error")
main()