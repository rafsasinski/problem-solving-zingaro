# https://dmoj.ca/problem/ecoo17r3p1
'''
INPUT:
    F   D:
        F - integer (4 <= F <= 130),  Number of ranchises (columns)
        D - integer (2 <= D <= 4745), Number of days (rows)
    Dn - lines where (Fi, Dj) - number of baked goods
'''


for _ in range(10):
    shops, days = map(int, input().split())
    dataset = []
    across_shops = []
    across_days = []

    for i in range(days):
        # row = map(int, input().split())
        row = input().split()
        row = [int(r) for r in row]
        across_shops.append(sum(row))

        # dataset.append([int(x) for x in input().split()])
        if len(row) != len(across_days):
            across_days = [0 for _ in row]

        for j in range(len(row)):
            across_days[j] += row[j]


    # print(f"across D: {across_days}")
    # print(f"across S: {across_shops}")

    across_days = [int(d / 13) if not d % 13 else 0 for d in across_days]
    across_shops = [int(d / 13) if not d % 13 else 0 for d in across_shops]

    print(sum([sum(across_days), sum(across_shops)]))
