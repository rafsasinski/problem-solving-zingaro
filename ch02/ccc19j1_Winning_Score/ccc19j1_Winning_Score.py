# https://dmoj.ca/problem/ccc19j1

points_A = int(input()) * 3 + int(input()) * 2 + int(input())
points_B = int(input()) * 3 + int(input()) * 2 + int(input())

if points_A > points_B:
    print('A')
elif points_A < points_B:
    print('B')
else:
    print('T')
