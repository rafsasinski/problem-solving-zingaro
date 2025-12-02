# https://dmoj.ca/problem/coci06c5p1

movement = input()
bloc = 0

for move in movement:

    if move == 'A':
        if bloc == 0:
            bloc = 1
        elif bloc == 1:
            bloc = 0
    elif move == 'B':
        if bloc == 1:
            bloc = 2
        elif bloc == 2:
            bloc = 1
    elif move == 'C':
        if bloc == 0:
            bloc = 2
        elif bloc == 2:
            bloc = 0

print(bloc + 1)
