# https://dmoj.ca/problem/coci16c1p1

DATA_PLAN = int(input())
months = int(input())
next_month = DATA_PLAN

for _ in range(0, months):
    carry = DATA_PLAN - int(input())
    next_month = next_month + carry

print(next_month)
