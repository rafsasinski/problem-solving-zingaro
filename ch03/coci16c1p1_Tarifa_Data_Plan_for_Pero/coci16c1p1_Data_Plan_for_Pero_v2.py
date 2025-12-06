# https://dmoj.ca/problem/coci16c1p1

DATA_PLAN = int(input())
months = int(input())
usage = 0

for month in range(0, months):
    usage = usage + int(input())

next_month = (DATA_PLAN * (months + 1)) - usage
print(next_month)
