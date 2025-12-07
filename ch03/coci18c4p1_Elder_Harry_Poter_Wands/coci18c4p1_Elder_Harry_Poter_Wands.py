# https://dmoj.ca/problem/coci18c4p1

'''
Elder Wand
A Elder Wand (obeys) defeated by B
B Elder Wand (obeys)

N duels
Questions:
    Wchich wizzad did the wand obey after all N duels
    How many different wizards did the wand obey
Input:
    Wizzard that the wnad obyed at the start
    N - number of duels
    Nrows of Z1 Z2 - Z1 defeated Z2
Output:
    2 lines of questions from above

'''

wand_wizzard = input()
obeyed_wizzards = wand_wizzard
duels = int(input())


for _ in range(duels):
    duel = input()

    if duel[2] == wand_wizzard:
        wand_wizzard = duel[0]

        if wand_wizzard not in obeyed_wizzards:
            obeyed_wizzards = obeyed_wizzards + wand_wizzard

print(wand_wizzard)
print(len(obeyed_wizzards))
