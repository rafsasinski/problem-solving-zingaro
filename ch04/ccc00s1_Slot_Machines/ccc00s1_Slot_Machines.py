# https://dmoj.ca/problem/ccc00s1

payout_interval = [35, 100, 10]
payout_amounts = [30, 60, 9]
turns_since_payout = [0, 0, 0]
current_machine = 0
play_cost = 1

wallet = int(input())
turns_since_payout[0] = int(input())
turns_since_payout[1] = int(input())
turns_since_payout[2] = int(input())

total_plays = 0

while wallet > 0:
    wallet = wallet - play_cost
    total_plays = total_plays + 1

    # Got stuck on an OFF-BY-ONE: this turn can already be the winning one (hence the -1)
    if turns_since_payout[current_machine] >= payout_interval[current_machine]-1:
        turns_since_payout[current_machine] = 0
        wallet = wallet + payout_amounts[current_machine]
    else:
        turns_since_payout[current_machine] = turns_since_payout[current_machine] + 1

    if current_machine < len(turns_since_payout)-1:
        current_machine = current_machine + 1
    else:
        current_machine = 0


print(f"Martha plays {total_plays} times before going broke.")

'''
Machines:
    1. 30q every 35th
    2. 60q every 100th
    3. 9q every 10th

INPUT:
    - Marthas wallet (quarters)
    - n times machine 1 was played
    - n times machine 2 was played
    - n times machine 3 was played

OUTPUT:
    - Martha machines X times before going broke.

TEST CASES:
TC0
    48  3  10  4
    Outcome:
        Martha plays 66 times before going broke.

TC1
    3  30  90  7
    Outcome:
        Martha plays 3 times before going broke.
'''
