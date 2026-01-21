# https://dmoj.ca/problem/ccc18s1
'''
N total_villages in line
16
Ignore is right most

0
Ignore left most

10
LM = 4
RM = 15
(10 - 4)/2 = 6/2 = 3
(15 - 10)/2 = 5/2 = 2.5
3 + 2.5 = 5.5

4
LM = 0
RM = 10
(0-4)/2 = 2
(10-4)/2 = 6/2 = 3
5

15
LM = 10
RM = 16
(15-10)/2 = 5/2 = 2.5
(16-15)/2 = 1/2 = 0.5
3.0

'''

max_village = 0
min_village = 0
total_villages = int(input())
villages = []
neighbours = []

for i in range(total_villages):
    candidate = int(input())
    
    if i == 0:
        max_village = candidate
        min_village = candidate
    
    if candidate < min_village:
        min_village = candidate
    elif candidate > max_village:
        max_village = candidate

    villages.append(candidate)


for village in villages:
    if village == max_village or village == min_village:
        continue

    left    = min_village
    right   = max_village

    for candidate in villages:
        # left
        if candidate > left and candidate < village:
            left = candidate
        if candidate < right and candidate > village:
            right = candidate

    size = ((village - left) / 2) + ((right - village) / 2)
    neighbours.append(size)

print(min(neighbours))
