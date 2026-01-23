# https://dmoj.ca/problem/ecoo18r1p1
'''
INPUT:
    T N:
        T - integer (2 <= T <= 7), how many days Willow (cat) holds the box
        N - integer (1 <= N <= 365), lines of shopping habbis
    N-lines: either 'E' (empty handed) or 'B' (add box to the list)
'''

for _ in range(10):

    days_holding_box, num_shopping_days = map(int, input().split())
    days = []

    for _ in range(num_shopping_days):
        days.append(input())

    delay = 0

    for i in range(num_shopping_days):
        if days[i] == 'B':
            delay += days_holding_box
        
        if delay != 0:
            delay -= 1

    print(delay)
