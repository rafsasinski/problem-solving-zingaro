# https://dmoj.ca/problem/coci19c5p1
'''
INPUT
    N M (1 <= N, M <= 100)
'''

# Rows, Columns
rc = [int(value) for value in input().split()]
N = rc[0]
# M = rc[1]

boundaries = []
rectangles_count = 0

for _ in range(N):
    line = input()
    same_rect = False

    for x in range(len(line)):
        ch = line[x]

        if ch == '.':
            same_rect = False
            if x in boundaries:
                boundaries.remove(x)

        if ch == '*':
            if x not in boundaries:
                boundaries.append(x)
                if not same_rect:
                    rectangles_count += 1
                same_rect = True


print(rectangles_count)