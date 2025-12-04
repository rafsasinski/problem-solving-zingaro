# https://dmoj.ca/problem/ccc18j2

parking_size = int(input())
a = input()
b = input()
shared = 0

for lot in range(0, parking_size):
    if (a[lot] == 'C' and b[lot] == 'C'):
        shared += 1

print(shared)
