# https://dmoj.ca/problem/ecoo17r3p1
'''
INPUT:
    F   D:
        F - integer (4 <= F <= 130),  Number of ranchises (columns)
        D - integer (2 <= D <= 4745), Number of days (rows)
    Dn - lines where (Fi, Dj) - number of baked goods
EXAMPLE:
    4 2
    4 4 4 1
    1 1 3 4
'''


for _ in range(10):
    shops, days = map(int, input().split())
    across_shops = []
    across_days = []

    if len(across_days) != shops:
        across_days = [0] * shops

    for i in range(days):
        row = [int(r) for r in input().split()]

        across_shops.append(sum(row))

        for j in range(shops):
            across_days[j] += row[j]


    across_days = [int(d / 13) if not d % 13 else 0 for d in across_days]
    across_shops = [int(d / 13) if not d % 13 else 0 for d in across_shops]

    print(sum([sum(across_days), sum(across_shops)]))
