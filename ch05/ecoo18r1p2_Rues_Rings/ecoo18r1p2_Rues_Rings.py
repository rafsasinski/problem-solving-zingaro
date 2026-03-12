# https://dmoj.ca/problem/ecoo18r1p2
'''
    N - roundabout-filled routes (from start to end point)
    Analyze different routes to find out which route (or routes)
    could generate the most issues

INPUT: 10 datasets
    N - (2 <= N <= 700) - number of routes
    ID R D
        ID - The ID of the route
        R (1 <= R <= 70) Number of roundabouts
        D (1 <= D <= 70000) each roundabout along the route
OUTPUT
For each dataset, output minimum roundabout diameter along a route
followed by, brace-encosed, sorted list of route IDs

EXAMPLE:
    INPUT
        3
        1 6 4 5 2 6 3 2
        2 3 2 3 4
        3 4 2 3 2 4
    OUTPUT:
        2 {1,2,3}
        1 {4}

Parsing the example:
N = 3
1. ID = 1, R = 6, D = [4, 5, 2, 6, 3, 2]
2. ID = 2, R = 3, D = [2, 3, 4]
3. ID = 3, R = 4, D = [2, 3, 2, 4]
'''

for _ in range(10):
    N = int(input())


    smallest_diameter = float('inf')
    smallest_routes = []

    for _ in range(N):
        line = [int(value) for value in input().split()]
        ID = line[0]
        R = line[1]
        D = line[2:]
        d = min(D)

        if d < smallest_diameter:
            smallest_diameter = d
            smallest_routes = []
            smallest_routes.append(ID)
        elif d == smallest_diameter:
            smallest_routes.append(ID)

    smallest_routes.sort()
    print(f"{smallest_diameter} {{{",".join(map(str, smallest_routes))}}}")

