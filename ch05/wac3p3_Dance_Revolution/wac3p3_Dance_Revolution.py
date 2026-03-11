# https://dmoj.ca/problem/wac3p3

S = input()
M = int(input())
combos = []
combos_points = []
for _ in range(M):
    line = input().split()
    combos.append(line[0])
    combos_points.append(int(line[1]))

scored_points = 0
i = 0

while i < len(S):
    best_points = 0
    longest_match = 0
    for c in range(len(combos)):
        combo_ch_match = 0
        combo = combos[c]
        if len(combo) < longest_match:
            continue
        for j in range(len(combo)):
            if not i + j >= len(S):
                if combo[j] == S[i + j]:
                    combo_ch_match += 1
                    if j == len(combo) - 1 and combo_ch_match == len(combo):
                        longest_match = len(combo)
                        best_points = combos_points[c]

    if longest_match > 0:
        # Combo found move i + len(combo)
        i += longest_match
        scored_points += best_points
    else:
        # No combo found move 1
        i += 1

answer = len(S) + scored_points
print(answer)
