import random

game_keys = ["*", "*", "*", "*", "*", "*", "*", "*", "*", ]


def is_player_win(player):
    if game_keys[0] == player and game_keys[1] == player and game_keys[2] == player:
        return True
    elif game_keys[3] == player and game_keys[4] == player and game_keys[5] == player:
        return True
    elif game_keys[6] == player and game_keys[7] == player and game_keys[8] == player:
        return True
    elif game_keys[0] == player and game_keys[3] == player and game_keys[6] == player:
        return True
    elif game_keys[1] == player and game_keys[4] == player and game_keys[7] == player:
        return True
    elif game_keys[2] == player and game_keys[5] == player and game_keys[8] == player:
        return True
    else:
        return False


print("Welcome to TicToc Toe game.")
keys = ["O", "X"]

for i in range(3):
    print(f"{random.choice(keys)} | {random.choice(keys)} | {random.choice(keys)}")
    if i < 2:
        print("---------")

game_on = False
start_game = input("\nWrite 'S' to start the game.").lower()
if start_game == "s":
    game_on = True
    for i in range(3):
        print(f"* | * | * ")
        if i < 2:
            print("---------")
    print("Game is start between 'X' and 'O'.")
    player_number = 1
    player_name = "X"
    while game_on:
        if player_number % 2 == 0:
            player_name = "O"
        else:
            player_name = "X"

        answer = input(f"Player {player_name} - Choose 1-9.. ")
        player_number += 1
        index = int(answer)
        if not game_keys[index-1] == "*":
            print("This box already tapped. please try again.")
        else:
            game_keys[index - 1] = player_name

        print(f"{game_keys[0]} | {game_keys[1]} | {game_keys[2]} ")
        print("-----------")
        print(f"{game_keys[3]} | {game_keys[4]} | {game_keys[5]} ")
        print("------------")
        print(f"{game_keys[6]} | {game_keys[7]} | {game_keys[8]} ")

        if is_player_win(player_name):
            print(f"wwwwwwooooooowwwwwww {player_name} win the game.")
            game_on = False
        elif not game_keys.__contains__("*"):
            print("Game Draw ")
            game_on = False
