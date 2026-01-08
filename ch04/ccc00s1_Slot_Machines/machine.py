'''
Each play cost 1 quarter
Machine 1 PAYS 30 Q every 35th
Machine 2 PAYS 60 Q every 100th
Machine 3 PAYS  9 Q every 10th

INPUT
Marta Q in a jar
M1 last pay
M2 last pay
M3 last pay
'''

jar = int(input())
machine_turns = [int(input()), int(input()), int(input())]
machine_limit = [35, 100, 10]
machine_pays = [30, 60, 9]
plays = 0
machine = 0

while jar > 0:
    jar -= 1
    machine = plays % 3
    plays += 1

    print(f"machine: {machine}")

    if machine_turns[machine] >= machine_limit[machine]-1:
        machine_turns[machine] = 0
        jar += machine_pays[machine]
    else:
        machine_turns[machine] += 1


print(f"Martha plays {plays} times before going broke.")
