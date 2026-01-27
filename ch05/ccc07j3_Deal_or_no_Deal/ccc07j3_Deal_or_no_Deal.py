# https://dmoj.ca/problem/ccc07j3
'''
10 briefcases with cash inside:
    [100, 500, 1000 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
Contestant selects 1 briefcases as his/hers
Next some of the briefcases get's elimintated

At one point "Banker" will ofer cash to Contestant in exchange for
their briefcase

Contestant says "Deal" or "No Deal"

INPUT
    n - (1 <= n <= 10) how many cases have been open
    ni - list of (n) integers each between 1 and 10
    Bankers ofer
EXAMPLE
2
3
8
198000
'''


CASE_AMOUNTS = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
winning_total = sum(CASE_AMOUNTS)
case_opened_count = int(input())

for i in range(case_opened_count):
    case = int(input())
    winning_total -= CASE_AMOUNTS[case - 1]

bank_offer = int(input())
average_winning = winning_total // (10 - case_opened_count)

if bank_offer > average_winning:
    print("deal")
else:
    print("no deal")
