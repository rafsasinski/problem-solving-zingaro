# https://dmoj.ca/problem/ecoo15r1p1

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
    smartie = ""

    while smartie != "end of box" :
        smartie = input()

        if smartie != "end of box":
            hand[smartie] = hand[smartie] + 1

    for s in hand:
        if s == "red":
            total_time = total_time + (hand[s] * 16)
        else:
            hand_of_smarties = (hand[s] + 6) // 7
            total_time = total_time + hand_of_smarties * 13

    print(total_time)
