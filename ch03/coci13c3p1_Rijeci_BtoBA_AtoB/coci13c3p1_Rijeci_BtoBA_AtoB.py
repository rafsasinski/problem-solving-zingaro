# https://dmoj.ca/problem/coci13c3p1
runs = int(input())
a = 1
b = 0

for i in range(runs):
    next_a = b
    next_b = a + b

    a = next_a
    b = next_b

print(f"{a} {b}")



'''
*                       As  Bs
A                       1   0   
B                       0   1
BA                      1   1
BAB                     1   2
BABBA                   2   3
BABBABAB                3   5
BABBABABBABBA           5   8
BABBABABBABBABABBABAB   8   13

A = 1
B = 0

nA = B
nB = A + B

'''
