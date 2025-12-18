# https://dmoj.ca/problem/ecoo15r1p1

'''
No thappy about this one, but it gives the right answer
'''

for dataset in range(10):
    hand = {
            "red"	    : 0,
            "blue"	    : 0,
            "brown"     : 0,
            "green"	    : 0,
            "orange"	: 0,
            "pink"      : 0,
            "violet"	: 0,
            "yellow"	: 0
            }

    total_time = 0
    treshold = 7
    smartie = ""

    while True:
        smartie = input()

        if smartie == "red":
            total_time = total_time + 16
            continue

        if smartie == "end of box":
            treshold = 1

        if smartie in hand:
            hand[smartie] = hand[smartie] + 1

        for s in hand:
            if hand[s] >= treshold:
                hand[s] = 0
                total_time = total_time + 13

        if treshold == 1:
            break

    print(total_time)
