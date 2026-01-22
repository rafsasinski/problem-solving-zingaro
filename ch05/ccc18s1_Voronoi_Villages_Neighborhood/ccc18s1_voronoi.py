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

total_villages = int(input())
villages = []

for i in range(total_villages):
    villages.append(int(input()))
    

villages.sort()

# +Infinity float
min_neighborhood = float('inf')


for i in range(1, len(villages) - 1):
    left    = (villages[i] - villages[i-1]) / 2
    right   = (villages[i+1] - villages[i]) / 2
    size = left + right

    if size < min_neighborhood:
        min_neighborhood = size


# enforce the correct notation
print(f"{min_neighborhood:.1f}")
