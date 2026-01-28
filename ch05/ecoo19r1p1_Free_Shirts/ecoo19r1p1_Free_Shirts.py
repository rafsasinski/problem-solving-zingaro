# https://dmoj.ca/problem/ecoo19r1p1

for _ in range(10):
    shirts, events, days = map(int, input().split())
    event_days = [int(i) for i in input().split()]

    dirty_shirts = 0
    laundry_count = 0

    for i in range(days):

        if shirts == 0:
            laundry_count += 1
            shirts = dirty_shirts
            dirty_shirts = 0

        if i in event_days:
            new_shirts = event_days.count(i)
            shirts += new_shirts

        shirts -= 1
        dirty_shirts += 1

    print(laundry_count)


'''
NOTES:
Ian is a slob, he goes to events to get free t-shirts to avoid laundry lol!
Ian starts with N clean shirts.
Ian wears one clean shirt every day (after which it becomes dirty)
If he has not clean shirts (beginning of the day) before events, he will do laundry (all shirts)
In the event he will receive clean shirt.

Task: Given N clean shirts, and the schedule of events fot the next D days, how many times
Ian will do the laundry in the next D days.

INPUT - 10 datasets!
N, M, D - (1 <= N,M <= 100; 1 <= D <= 1000) Where:
    N - number (initial) of clean shirts
    M - number of events coming up
    D - numer of days

    Next Line:
    M integers - Ai (1 <= Ai <= D), the days on which there are events
        There might be multiple events in a single day

Sample
TC01:
1 1 10
10
OUTPUT:
9

TC02:
1 3 10
2 9 5
OUTPUT:
4

TC03:
1 3 10
2 2 5
OUTPUT:
4
'''
