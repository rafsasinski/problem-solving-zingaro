(N, H) = (int(x) for x in input().split())

players_HP = [H, H]
players_move = [[], []]

for n in range(N*2):
    move_type, move_power = input().split()
    if n < N:
        players_move[0].append((move_type, int(move_power)))
    else:
        players_move[1].append((move_type, int(move_power)))

i = 0
player_id = 0
previous_move = None # FALSE

while i < N and min(players_HP) > 0:

    # Select current move for player
    move = players_move[player_id][i]
    move_type = move[0]
    move_power = move[1]

    # Activate the move
    if move_type == "A":
        if not previous_move or previous_move[0] != "D":
            players_HP[player_id ^ 1] -= move_power
    elif move_type == "D":
        if previous_move and previous_move[0] == "D":
            players_HP[player_id ^ 1] -= previous_move[1]

    # This might be the last round check for self harm
    if i == N-1 and player_id == 1:
        if move_type == "D":
            players_HP[player_id] -= move_power


    # Prepare for next turn
    previous_move = move
    player_id += 1

    if player_id > 1:
        i += 1
        player_id = 0

if players_HP[0] <= 0:
    print("DEFEAT")
elif players_HP[1] <= 0:
    print("VICTORY")
else:
    print("TIE")