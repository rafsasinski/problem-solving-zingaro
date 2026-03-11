# https://dmoj.ca/problem/wac3p3

S = input()
M = int(input())
combos = []
combos_points = []
combos_count = []
combos_first = []
for _ in range(M):
    line = input().split()
    combos.append(line[0])
    combos_points.append(int(line[1]))
    combos_count.append(0)
    combos_first.append(-1)

#combos.sort(key=lambda val: len(val[0]), reverse=True)

for c in range(len(combos)):
    combo = combos[c]
    i = 0
    while i < len(S):
        combo_ch_match = 0
        for j in range(len(combo)):
            if not i+j >= len(S):
                if combo[j] == S[i+j]:
                    combo_ch_match += 1
                
                if j == len(combo)-1 and combo_ch_match == len(combo):
                    combos_count[c] += 1
                    if combos_first[c] == -1:
                        combos_first[c] = i
                    i += j
        i+=1

combined = list(zip(  list(map(lambda c: len(c), combos)), combos_first, combos_count, combos_points, combos))
combined.sort(key=lambda x: (x[0], -x[1]), reverse=True)
winner = combined[0]

answer = len(S) + winner[3] * winner[2]
print(answer)
