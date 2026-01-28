# https://dmoj.ca/problem/coci18c2p1

GAME_DURATION = 4*12*60
total_points = 0
score_timestamp_tracker = []

total_points = int(input())
for _ in range(total_points):
    seconds = int(input())
    score_timestamp_tracker.append(['A', seconds])

total_points = int(input())
for _ in range(total_points):
    seconds = int(input())
    score_timestamp_tracker.append(['B', seconds])

score_timestamp_tracker.sort(key=lambda elm: elm[1])

total_score_before_half_time = 0
total_turnarounds = 0 
points_a = 0
points_b = 0
leader = None


for elm in score_timestamp_tracker:
    team_name = elm[0]
    score_timestamp = elm[1]

    if team_name == 'A':
        points_a += 1
    else:
        points_b += 1

    if points_a > points_b:
        if leader != "A" and leader is not None:
            total_turnarounds +=1
        leader = "A"
    elif points_a < points_b:
        if leader != "B" and leader is not None:
            total_turnarounds +=1
        leader = "B"

    if score_timestamp <= GAME_DURATION/2:
        total_score_before_half_time += 1



print(total_score_before_half_time)
print(total_turnarounds)

'''
Team A, Team B.
Points socred on both teams A and B, and the exact second of it
Within 1 sec you can not score more than 1 point

1. How many score_timestamp have been scored in the first half-time
Entire game is 4 x 12 min

2. How many turnarounds happend during the match.
i.e. how many times team come from loosing to leading one

INPUT
    A - (1 <= A <= 2879)
'''
