# https://dmoj.ca/problem/coci06c5p1

movement = input()
bloc = 0

trans = {
        'A': {0: 1, 1: 0, 2: 2},
        'B': {0: 0, 1: 2, 2: 1},
        'C': {0: 2, 1: 1, 2: 0}
        }

for move in movement:
    bloc = trans[move][bloc]

print(bloc + 1)
