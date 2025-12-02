# https://dmoj.ca/problem/coci18c3p1

word = input()
honi_count = 0

'''
0 H
1 O
2 N
3 I
'''
honi = 0 

for ch in word:
    

    if not honi and ch == 'H':
        honi += 1
    elif not honi and ch == 'O':
        honi += 1
    elif not honi and ch == 'N':
        honi += 1
    elif not honi and ch == 'I':
        honi_count += 1
        honi = 0

print(honi_count)

