# https://dmoj.ca/problem/coci16c1p1

DATA_PLAN = int(input())
months = int(input())
carry = []
next_month = DATA_PLAN

for month in range(0, months):
    carry.append(DATA_PLAN - int(input()))
    next_month = next_month +  carry[month]

print(next_month)
