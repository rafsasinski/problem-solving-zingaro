# https://dmoj.ca/problem/ccc18s1
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
